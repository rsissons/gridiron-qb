# Gridiron QB

A 3D quarterback game in the browser. Pick a play from the playbook, read the coverage, then **pull the ball back and let go** to throw, the same pull-back feel as the San Dimas Canyon golf game.

**Play it:** https://rsissons.github.io/gridiron-qb/

## Modes
- **Game:** 3 drives. Move the chains, score touchdowns, kick extra points, and try field goals on 4th down.
- **Two-minute drill:** two minutes on the clock. Score as many points as you can.
- **Field goals:** kicks from farther and farther back, with wind. Three misses and you're out.
- **Target toss:** ten throws through rings. Far rings and moving rings score more.

## How it plays
- **The playbook:** 8 plays built from slant, out, curl, post, corner, go, drag and wheel routes. Three receivers (A, B, C) run them against man coverage and a deep safety.
- **The camera:** a waist-high view from over the quarterback's throwing shoulder, with your name and number on the back of the jersey. The view turns toward wherever you aim.
- **Aiming:** tap a receiver's letter to aim at where he'll be, or drag anywhere to aim yourself.
- **Power:** pull straight back to **100%** to hit the spot. Less falls short, more sails long, and pulling sideways sprays the ball.
- **The pass rush:** a pocket clock. Throw before it fills up or you get sacked.
- **Stadiums:** Pro Stadium, Friday Night Lights, Snow Bowl and Desert Dome.
- **Difficulty:** Rookie (route lines, tracking aim, slower defenders), Pro, and All-Pro (no help).

Best scores are saved in the browser. There's no sign-in, no network data, and no tracking.

## Build
`python source/build.py` embeds the sound clips in `source/game_src.html` and writes `site/index.html`. three.js 0.169 loads from jsDelivr.

## Credits
Sounds are CC0 recordings from Freesound. See `data/sounds/CREDITS.md`. The code is MIT licensed.
