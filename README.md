# Gridiron QB

A 3D quarterback game in the browser. Pick a play from the playbook, read the coverage, then **press to aim and release to fire**.

**Play it:** https://rsissons.github.io/gridiron-qb/

## Modes
- **Game:** 3 drives. Move the chains, score touchdowns, kick extra points, and try field goals on 4th down.
- **Two-minute drill:** two minutes on the clock. Score as many points as you can.
- **Field goals:** kicks from farther and farther back, with wind. Three misses and you're out.
- **Target toss:** ten throws through rings. Far rings and moving rings score more.

## How it plays
- **The playbook:** 8 plays built from slant, out, curl, post, corner, go, drag and wheel routes. Three receivers (A, B, C) run them against man coverage and a deep safety.
- **The players:** real animated, rigged athletes in helmets, pads and your team colors. They crouch in their stances, block, run their routes, dive into tackles and celebrate touchdowns.
- **The camera:** over the quarterback's throwing shoulder, with your name and number on his back. After the throw it pulls up to follow the ball.
- **Throwing:** press and hold on a receiver's letter (or anywhere) and slide the target circle to where he's headed. The circle shrinks while you hold, so let go when it's small and green. Let go early and the ball can go wide. Hold too long and it grows again.
- **Kicking:** hold to power up, drag to aim into the wind, and let go at the top of the power bar.
- **The pass rush:** a pocket clock. Throw before it fills up or you get sacked.
- **Stadiums:** Pro Stadium, Friday Night Lights, Snow Bowl and Desert Dome.
- **Difficulty:** Rookie (route lines, aim that pulls toward open receivers, slower defenders), Pro, and All-Pro (no help).

Best scores are saved in the browser. There's no sign-in, no network data, and no tracking.

## Build
`python source/build.py` embeds the sound clips in `source/game_src.html`, writes `site/index.html` and copies the player models to `site/models/`. three.js 0.169 loads from jsDelivr. The models are Quaternius CC0 packs, trimmed and meshopt-compressed with glTF-Transform.

## Credits
- **Players and animations:** [Quaternius](https://quaternius.com) Universal Base Characters and Universal Animation Library (CC0).
- **Sounds:** CC0 recordings from Freesound. See `data/sounds/CREDITS.md`.
- **Code:** MIT licensed.
