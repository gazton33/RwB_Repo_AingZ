# Universal MIDI Drum Generator desde Markdown - Versión mejorada (manejo de errores)
# By Gastón & ChatGPT

from midiutil import MIDIFile
import os
import re

def safe_search(pattern, text, default, as_type=int):
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        try:
            return as_type(match.group(1))
        except:
            return default
    return default

# --- PARSER ROBUSTO DE MD ESTRUCTURADO ---
def parse_md(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()
    bpm = safe_search(r'BPM:?[\s\-]*(\d+)', text, 72)
    channel = safe_search(r'channel:?[\s\-]*(\d+)', text, 9)
    volume = safe_search(r'volume:?[\s\-]*(\d+)', text, 100)
    # Drum map
    drum_map = {}
    for match in re.finditer(r'-\s*(\w+):\s*(\d+)', text):
        drum_map[match.group(1)] = int(match.group(2))
    # Patterns
    patterns = {}
    for patt_header in re.finditer(r'###\s*(\w+)', text):
        patt_name = patt_header.group(1)
        # Buscar desde el header hasta el próximo header o final
        patt_start = patt_header.end()
        next_header = re.search(r'^(###\s*\w+)', text[patt_start:], re.MULTILINE)
        patt_end = patt_start + next_header.start() if next_header else len(text)
        patt_block = text[patt_start:patt_end]
        notes = re.findall(r'\{\s*"note":\s*"(\w+)",\s*"time":\s*([\d\.]+),\s*"velocity":\s*(\d+)\s*\}', patt_block)
        patterns[patt_name] = [{"note": n, "time": float(t), "velocity": int(v)} for n, t, v in notes]
    # Sections
    sections = []
    for match in re.finditer(r'-\s*name:\s*(\w+)\n\s*start:\s*(\d+)\n\s*pattern:\s*(\w+)\n\s*length:\s*(\d+)\n\s*compas:\s*(\d+)', text):
        sections.append({
            "name": match.group(1),
            "start": int(match.group(2)),
            "pattern": match.group(3),
            "length": int(match.group(4)),
            "compas": int(match.group(5))
        })
    return {
        "bpm": bpm, "channel": channel, "volume": volume, "drum_map": drum_map, "patterns": patterns, "sections": sections
    }

# --- GENERACIÓN MIDI ---
def generate_midi(pattern_dict, output_midi):
    bpm = pattern_dict.get('bpm', 100)
    track = 0
    channel = pattern_dict.get('channel', 9)
    volume = pattern_dict.get('volume', 100)
    ticks_per_quarter = 960
    mf = MIDIFile(1, file_format=1, ticks_per_quarternote=ticks_per_quarter)
    mf.addTempo(track, 0, bpm)
    drum_map = pattern_dict['drum_map']
    sections = pattern_dict['sections']
    patterns = pattern_dict['patterns']
    for section in sections:
        start_time = section['start']
        patt = patterns[section['pattern']]
        length = section.get('length', 1)
        for i in range(length):
            for step in patt:
                mf.addNote(track, channel, drum_map[step['note']],
                    start_time + step['time'] + i * section.get('compas', 4), 0.10, step.get('velocity', volume))
    with open(output_midi, 'wb') as f:
        mf.writeFile(f)
    print(f"\n¡Archivo MIDI generado: {output_midi}!")

# --- INTERFAZ ---
if __name__ == '__main__':
    files = [f for f in os.listdir('.') if f.endswith('.md')]
    if not files:
        print('No hay archivos .md en la carpeta.')
        exit(1)
    print('\nTemplates MD disponibles:')
    for i, f in enumerate(files):
        print(f"[{i+1}] {f}")
    sel = int(input('\nSelecciona el número del template a procesar: '))
    selected = files[sel-1]
    data = parse_md(selected)
    nombre_salida = os.path.splitext(selected)[0] + '_out.mid'
    generate_midi(data, nombre_salida)
