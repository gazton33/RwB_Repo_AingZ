# Template MIDI Drum Groove (Markdown)

## Groove Settings
- BPM: 72
- channel: 9
- volume: 100

## Drum Map
- kick: 36
- snare: 38
- rimshot: 37
- closed_hat: 42
- open_hat: 46
- low_tom: 45
- mid_tom: 47
- high_tom: 50
- ride: 51
- crash: 49
- clap: 39
- cowbell: 56
- clave: 75
- tambourine: 54
- shaker: 82
- block: 76

## Patterns
### main_groove
{ "note": "kick", "time": 2.0, "velocity": 98 }
{ "note": "snare", "time": 2.0, "velocity": 110 }
{ "note": "closed_hat", "time": 0.0, "velocity": 75 }
{ "note": "closed_hat", "time": 0.5, "velocity": 80 }
{ "note": "closed_hat", "time": 1.0, "velocity": 85 }
{ "note": "closed_hat", "time": 1.5, "velocity": 78 }
{ "note": "closed_hat", "time": 2.0, "velocity": 90 }
{ "note": "closed_hat", "time": 2.5, "velocity": 86 }
{ "note": "closed_hat", "time": 3.0, "velocity": 82 }
{ "note": "closed_hat", "time": 3.5, "velocity": 88 }
{ "note": "open_hat", "time": 3.75, "velocity": 98 }
{ "note": "shaker", "time": 0.25, "velocity": 60 }
{ "note": "shaker", "time": 1.25, "velocity": 68 }
{ "note": "tambourine", "time": 2.75, "velocity": 72 }

### fill_triplet
{ "note": "high_tom", "time": 2.5, "velocity": 80 }
{ "note": "mid_tom", "time": 2.75, "velocity": 75 }
{ "note": "low_tom", "time": 3.0, "velocity": 82 }
{ "note": "crash", "time": 3.25, "velocity": 98 }
{ "note": "snare", "time": 3.5, "velocity": 90 }

### break_block
{ "note": "block", "time": 1.0, "velocity": 82 }
{ "note": "block", "time": 1.5, "velocity": 70 }
{ "note": "block", "time": 2.5, "velocity": 74 }
{ "note": "crash", "time": 3.0, "velocity": 99 }

### latin_perc
{ "note": "clave", "time": 0.0, "velocity": 95 }
{ "note": "clave", "time": 1.5, "velocity": 80 }
{ "note": "cowbell", "time": 2.0, "velocity": 88 }
{ "note": "shaker", "time": 2.5, "velocity": 65 }

## Sections
- name: groove_loop
  start: 0
  pattern: main_groove
  length: 8
  compas: 4
- name: fill_intro
  start: 32
  pattern: fill_triplet
  length: 1
  compas: 4
- name: block_break
  start: 36
  pattern: break_block
  length: 1
  compas: 4
- name: latin_flavour
  start: 40
  pattern: latin_perc
  length: 4
  compas: 4

