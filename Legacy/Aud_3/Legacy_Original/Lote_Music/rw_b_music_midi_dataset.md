# RwB Music_Midi_Dataset (Actualizado para workflows con Markdown)

## Objetivo
Centralizar todo el conocimiento y procedimientos relacionados con el relevamiento, mapeo y workflow para la creación, documentación y ampliación de pistas MIDI de batería y percusión en Studio One (y otros DAWs compatibles con GM/Presence XT), siguiendo la metodología iterativa RwB, ahora soportando plantillas y loops en formato Markdown estructurado.

---

## 1. Infraestructura de trabajo
- **DAW:** Studio One 3.5 (Presonus) y compatibles
- **Samplers/Instrumentos virtuales:** Presence XT (y otros)
- **Herramientas de edición MIDI:** piano roll, cuantización, scripts Python/MIDIUtil
- **Preset base:** Large Kit, pero expandible a cualquier kit personalizado
- **Soporte extendido:** Plantillas y datasets en `.md` para mejor trazabilidad, edición y versionado

## 2. Procedimiento para creación de pistas MIDI
1. **Definir groove y estructura:** Decidir estilo, BPM, secciones (intro, verso, estribillo, fills, outro, etc.)
2. **Generar el patrón:** Puede hacerse manualmente (piano roll) o automatizadamente (script Python + MIDIUtil, ahora soportando `.md`)
3. **Exportar/importar:** Llevar el archivo MIDI al DAW y asignar instrumento
4. **Verificar el mapeo:** Chequear que las notas MIDI activan los sonidos correctos del drum kit cargado
5. **Editar, duplicar, personalizar:** Sumar fills, cambiar velocities, subdividir grilla (1/16 para detalles)
6. **Guardar y documentar:** Cada groove, kit y mapeo debe documentarse para referencia futura y escalabilidad, usando el dataset `.md` como repositorio vivo

## 3. Mapeo y paneo de instrumentos (Presence XT y estándar GM)
### a. Mapeo General MIDI (GM)
| Nota MIDI | Nombre estándar | Ejemplo (Presence XT)         |
|-----------|-----------------|-------------------------------|
| C1 (36)   | Acoustic Bass Drum | Acoustic Bass Drum         |
| D1 (38)   | Acoustic Snare  | Acoustic Snare                |
| D#1 (39)  | Electric Snare  | Electric Snare                |
| E1 (40)   | Side Stick      | Side Stick                    |
| F1 (41)   | Clap            | Acoustic Clap                 |
| F#1 (42)  | Closed Hi-hat   | Closed Hi-hat                 |
| G1 (43)   | Low Floor Tom   | Low Floor Tom                 |
| G#1 (44)  | Pedal Hi-hat    | Pedal Hi-hat                  |
| A1 (45)   | Low Tom         | Low Tom                       |
| A#1 (46)  | Open Hi-hat     | Open Hi-hat                   |
| B1 (47)   | Low-Mid Tom     | Low-Mid Tom                   |
| C2 (48)   | High-Mid Tom    | High-Mid Tom                  |
| C#2 (49)  | Crash Cymbal 1  | Crash Cymbal 1                |
| D2 (50)   | High Tom        | High Tom                      |
| D#2 (51)  | Ride Cymbal 1   | Ride Cymbal 1                 |
| ...       | ...             | ...                           |

### b. Paneo extendido por preset
- Tomar el listado lateral del piano roll y registrar, para cada kit:
  - Nota MIDI
  - Nombre del instrumento asignado
  - (Opcional) Sonido/variación específica (congas, cowbells, blocks, perc latinas, fx, etc.)

## 4. Relevamiento y ampliación del dataset
### a. Para cada drum kit utilizado:
1. Abrir el sampler/instrumento virtual en el DAW
2. Tomar una captura o anotar el listado lateral de instrumentos y sus notas en el piano roll
3. Integrar al presente documento la tabla extendida (Nota ↔ Instrumento)
4. Si hay sonidos fuera del estándar GM, agregarlos con nombre y nota específica
5. Repetir el procedimiento para cada kit, manteniendo histórico y compatibilidad

### b. Instrucciones de ampliación
- Copiar la tabla modelo y agregar los datos del nuevo kit debajo de la existente
- Documentar cualquier diferencia importante: por ejemplo, si un kit invierte el orden de los toms, o suma percusiones latinas exclusivas
- Señalar si algún groove/script requiere adaptación especial para ese kit

## 5. Tips de workflow iterativo y documentación
- Guardar cada groove/script y su mapeo como plantilla reutilizable (preferiblemente `.md`)
- Mantener este archivo como “dataset vivo”, actualizando cada vez que se trabaje con un nuevo preset o instrumento
- Usar versiones o checkpoints si se requiere trazabilidad en la evolución del workflow

---

**Este archivo integra las mejores prácticas y estructura la base de conocimiento MIDI para RwB, garantizando compatibilidad, escalabilidad y documentación sólida en el tiempo para la creación de pistas de batería profesionales en formato markdown.**

