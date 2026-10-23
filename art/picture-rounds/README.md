# Picture rounds

Generators for the 96×64 one-bit picture questions (flags are 8-bit colour).

1. `npm i` here (world-atlas, topojson-client, us-atlas, flag-icons, country-flag-icons, i18n-iso-countries), `pip install pillow cairosvg`
2. Draw: `python3 countries.py && python3 flags.py && python3 landmarks1.py && python3 landmarks2.py && python3 skylines_world.py && python3 skylines_china.py && python3 aircraft.py && python3 extras_maps_sky.py && python3 extras_objects.py`
3. Export to the game: `python3 build_pictures.py ../..` → writes `data/pictures.json` and `public/pics/`
4. `npm run build:questions` in the repo root merges them into `server/questions.json`.

Aircraft come from `aircraft3d.py` (side profiles traced from FlightGear 3D models; set FG_REPOS to a folder of FGMEMBERS clones). Paintings come from `paintings_nes.py` (NES-style 8-bit, from photos in `paintings_src/` plus hand-pixelled ones).

Small island nations, planets, sports gear and instruments are drawn but not exported to the game.
