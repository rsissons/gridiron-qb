"""Build the one-file game: embed the CC0 sound clips into the template.

python source/build.py  ->  site/index.html + site/models/*.glb (GitHub Pages)
"""
import base64, json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
src = (root / 'source' / 'game_src.html').read_text(encoding='utf-8')
clips = {p.stem: base64.b64encode(p.read_bytes()).decode() for p in sorted((root / 'data' / 'sounds').glob('*.mp3'))}
out = src.replace('/*__SOUNDS__*/', 'window.SOUND_CLIPS = ' + json.dumps(clips) + ';')
assert out != src, 'sound placeholder missing'
(root / 'site').mkdir(exist_ok=True)
(root / 'site' / 'index.html').write_text(out, encoding='utf-8')
(root / 'gridiron-qb.html').write_text(out, encoding='utf-8')
import shutil
(root / 'site' / 'models').mkdir(exist_ok=True)
for name in ('player', 'anims'):
    shutil.copyfile(root / 'data' / 'models' / f'{name}.opt.glb', root / 'site' / 'models' / f'{name}.glb')
print(f"built {len(out)//1024} KB with {len(clips)} clips")
