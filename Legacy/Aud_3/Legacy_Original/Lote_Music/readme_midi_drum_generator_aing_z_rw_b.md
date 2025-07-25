# README – Universal MIDI Drum Generator (Versión MD)

Este sistema permite crear pistas MIDI de batería de forma modular y escalable usando plantillas `.md` (markdown estructurado) y un generador universal en Python.

## ¿Cómo funciona?

1. **Define tu groove:**
   - Crea o edita un archivo `.md` siguiendo la plantilla modelo (`template_midi_drum_groove.md`).
   - Configura BPM, mapeo de sonidos, patrones y secciones (intro, groove, fills, etc.) en formato markdown, fácilmente editable y legible.

2. **Ejecuta el generador:**
   - Copia el script `universal_midi_drum_generator_md.py` en la carpeta de los `.md`.
   - Corre el script. Se listan automáticamente los archivos `.md` disponibles.
   - Selecciona el número correspondiente a la plantilla que quieras procesar.
   - El archivo MIDI se genera con el mismo nombre, terminando en `_out.mid`.

3. **Importa y edita en tu DAW:**
   - Abre el `.mid` generado en Studio One, Presence XT, Reaper, Ableton, etc.
   - Ajusta, duplica, personaliza y añade nuevos patrones desde el piano roll si lo deseas.

---

## Estructura del archivo `.md`

```
# Template MIDI Drum Groove (Markdown)

## Groove Settings
- BPM: 72
- channel: 9
- volume: 100

## Drum Map
- kick: 36
- snare: 38
- ...

## Patterns
### main_groove
{ "note": "kick", "time": 2.0, "velocity": 98 }
{ "note": "snare", "time": 2.0, "velocity": 110 }
...

## Sections
- name: groove_loop
  start: 0
  pattern: main_groove
  length: 8
  compas: 4
...
```

- **Drum map:** Nombre de instrumento ↔ número de nota MIDI.
- **Patterns:** Lista de golpes por patrón (nombre, tiempo relativo y velocity).
- **Sections:** Qué patrón usar, dónde comienza y cuántas repeticiones/compases.

Ver el archivo `template_midi_drum_groove.md` incluido.

---

## Ejemplo de ampliación
- Para sumar un nuevo kit de batería o sampler, adapta el drum map según el paneo/orden de notas del kit cargado en tu DAW.
- Puedes crear archivos `.md` para diferentes estilos, compases, grooves o presets.
- El sistema es **100% reutilizable y escalable**.

---

## Integración en AingZ_RwB
- Guarda este README junto con los scripts y plantillas.
- Agrega nuevos grooves y documenta los mapeos para mantener compatibilidad futura.
- Puedes conectar este sistema con otros scripts o flujos de trabajo en el repo AingZ_RwB, para crear datasets, loops o paquetes de grooves MIDI personalizados.

---

**Contacto:** Para dudas, mejoras o nuevas features, consulta el dataset `RwB_Music_Midi_Dataset.md` y el knowledge de grooves correspondiente.

