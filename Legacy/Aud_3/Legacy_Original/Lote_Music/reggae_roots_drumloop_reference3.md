# Reggae Roots Drumloop Reference

## Groove Settings
- BPM: 72
- channel: 9
- volume: 100

## Drum Map
- kick: 36
- snare: 38
- ghost_snare: 37
- rimshot: 37
- closed_hat: 42
- open_hat: 46
- low_tom: 45
- mid_tom: 47
- high_tom: 50
- crash: 49

## Patterns
### onedrop_main
{ "note": "closed_hat", "time": 0.5, "velocity": 75 }
{ "note": "closed_hat", "time": 1.5, "velocity": 80 }
{ "note": "closed_hat", "time": 2.5, "velocity": 78 }
{ "note": "closed_hat", "time": 3.5, "velocity": 82 }
{ "note": "kick", "time": 2.0, "velocity": 95 }
{ "note": "snare", "time": 2.0, "velocity": 110 }
{ "note": "open_hat", "time": 3.75, "velocity": 100 }

### fill_triplet
{ "note": "high_tom", "time": 2.5, "velocity": 85 }
{ "note": "mid_tom", "time": 2.75, "velocity": 72 }
{ "note": "low_tom", "time": 3.0, "velocity": 80 }
{ "note": "crash", "time": 3.25, "velocity": 105 }
{ "note": "snare", "time": 3.5, "velocity": 88 }

### big_fill
{ "note": "mid_tom", "time": 1.5, "velocity": 76 }
{ "note": "ghost_snare", "time": 1.75, "velocity": 45 }
{ "note": "high_tom", "time": 1.75, "velocity": 90 }
{ "note": "snare", "time": 2.0, "velocity": 92 }
{ "note": "closed_hat", "time": 2.25, "velocity": 73 }
{ "note": "open_hat", "time": 2.5, "velocity": 100 }
{ "note": "low_tom", "time": 3.0, "velocity": 77 }
{ "note": "crash", "time": 3.25, "velocity": 112 }

## Sections
- name: main_loop
  start: 0
  pattern: onedrop_main
  length: 8
  compas: 4
- name: fill1
  start: 32
  pattern: fill_triplet
  length: 1
  compas: 4
- name: fill2
  start: 36
  pattern: big_fill
  length: 1
  compas: 4

