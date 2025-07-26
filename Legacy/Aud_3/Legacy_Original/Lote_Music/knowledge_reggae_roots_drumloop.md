# Knowledge – Drum Loop Reggae Roots (Versión enriquecida para workflow MD)

## Patrón de referencia – One Drop (Reggae Roots Jamaica)
- **BPM típico:** 68–75 (según referencia original)
- **Compás:** 4/4, hi-hat en corcheas
- **Hi-hat:** siempre presente, acentos dinámicos en contratiempos y (2)/(4)
- **One Drop:** bombo y rimshot/caixa en el tercer tiempo (beat 3), dejando el primer golpe vacío (clave del feel roots)
- **Aperturas:** breve apertura de hi-hat, usualmente al final del compás (ej. 3.75)
- **Fills:** preferentemente en los toms, usando semicorcheas o tresillos para suavidad y “respuesta”

### Ejemplo de loop (MD compatible):

#### Groove Settings
- BPM: 72
- channel: 9
- volume: 100

#### Drum Map
- kick: 36
- rimshot: 37
- snare: 38
- closed_hat: 42
- open_hat: 46
- low_tom: 45
- mid_tom: 47
- high_tom: 50
- crash: 49

#### Patterns
##### onedrop_main
{ "note": "closed_hat", "time": 0.0, "velocity": 68 }
{ "note": "closed_hat", "time": 0.5, "velocity": 76 }
{ "note": "closed_hat", "time": 1.0, "velocity": 72 }
{ "note": "closed_hat", "time": 1.5, "velocity": 85 }
{ "note": "closed_hat", "time": 2.0, "velocity": 70 }
{ "note": "closed_hat", "time": 2.5, "velocity": 80 }
{ "note": "closed_hat", "time": 3.0, "velocity": 70 }
{ "note": "closed_hat", "time": 3.5, "velocity": 88 }
{ "note": "open_hat", "time": 3.75, "velocity": 100 }
{ "note": "kick", "time": 2.0, "velocity": 95 }
{ "note": "rimshot", "time": 2.0, "velocity": 108 }

##### fill_triplet
{ "note": "high_tom", "time": 2.5, "velocity": 80 }
{ "note": "mid_tom", "time": 2.75, "velocity": 75 }
{ "note": "low_tom", "time": 3.0, "velocity": 82 }
{ "note": "crash", "time": 3.25, "velocity": 98 }

#### Sections
- name: main_loop
  start: 0
  pattern: onedrop_main
  length: 4
  compas: 4
- name: fill1
  start: 16
  pattern: fill_triplet
  length: 1
  compas: 4

### Procedimiento iterativo para relevar grooves reggae (y otros estilos)
1. **Analizar canciones referencia**: identificar BPM, estructura de compás, patrón principal y fills.
2. **Armar patrón MIDI**: crear archivo `.md` con mapeo GM, hi-hat, acentos, fills y secciones.
3. **Probar loop** en DAW con sampler estándar o custom.
4. **Iterar**: ajustar velocities, swing, fills, humanización, aperturas, etc.
5. **Documentar**: agregar a este knowledge patrón, variante, fuentes, y observaciones sobre feel/expresividad.
6. **Repetir** para nuevos grooves, siempre anexando al knowledge.

---

**Fuentes clave:** The Gladiators, Israel Vibration, The Congos, The Wailers (Carlton Barrett: pionero del One Drop)
- Recursos: [MusicRadar](https://www.musicradar.com/how-to/how-to-program-a-typical-one-drop-reggae-beat-and-add-fills), [Bax-Shop Drum Reggae](https://www.bax-shop.co.uk/blog/drums/reggae-drumming-rhythms-sounds-and-cues/), [YouTube](https://www.youtube.com/watch?v=zQlxxVumqlY)

