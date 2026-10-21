# Black Box Trivia

Multiplayer trivia in a classic black-and-white desktop style. One person hosts and gets a **6-digit code**. Up to **7 friends** join from their own phones or computers. The host picks the number of questions, categories, difficulty, question type (A–D multiple choice, fill in the blank, or mixed) and time limit.

- 6 Trivial-Pursuit-style categories, each with a 1-bit pattern. Each player has a six-piece cube; a correct answer fills in that category's piece.
- Fill-in answers forgive spelling ("Tchaikovsky" / "chaikovsky", "Brasília" / "brazilia"). A guess that is exactly a *different* real answer (Austria vs Australia) doesn't count.
- Retro sound effects are synthesized in the browser, so there are no audio files.
- Works on phones and desktop. If a player refreshes or drops, they rejoin automatically.
- **Pass & Play**: 2–8 people share one phone, taking turns with a "pass the phone to…" screen so nobody sees the others' answers.
- Solo practice mode runs fully in the browser.
- Ad slots for Google AdSense (lobby, final scores, and optionally between questions).

---

## Run it on your computer

You need Node.js 18 or newer (https://nodejs.org).

```bash
npm install
npm start
# open http://localhost:3000
```

Open a second browser window (or your phone on the same Wi-Fi at `http://<your-computer-ip>:3000`) to join your own game. On localhost the ad slots show as striped placeholders so you can see where ads will go.

---

## Put it online (Render — about 10 minutes)

1. Make a free GitHub account and upload this folder as a new repository. (GitHub Desktop is the easiest way: *File → Add local repository → Publish*.)
2. Sign up at **render.com** and connect GitHub.
3. Click **New + → Blueprint** and pick the repository. Render reads `render.yaml` and sets everything up.
4. When it finishes you get a URL like `https://black-box-trivia.onrender.com`. Share that with friends.
5. Optional: buy a domain (e.g. from Namecheap or Cloudflare, ~$15/yr) and add it under *Settings → Custom Domains* in Render. You need your own domain for AdSense.

**Plan:** the free tier sleeps after 15 minutes idle (the first visitor waits ~30 s) and is fine for testing. Use the **Starter** plan (~US$7/month) once real people are playing.

Other hosts that work: Railway, Fly.io, DigitalOcean App Platform, or any VPS (a `Dockerfile` is included). The host must support WebSockets (all of these do).

> Game rooms live in server memory, so run **one** instance. One small instance can handle a few hundred simultaneous games. If you outgrow that, rooms would need to move to Redis. That's a later problem.

---

## Making money with ads

1. Get the site live on your own domain with a few pages of real content. The privacy page is at `/privacy.html`; edit the contact email in that file.
2. Apply at **https://adsense.google.com**. Approval usually takes a few days to a few weeks.
3. Once approved, create three **Display ad units** in AdSense (e.g. "Lobby", "Final", "Reveal") and copy each unit's *data-ad-slot* number.
4. In Render → *Environment*, set:

   | Variable | Example |
   |---|---|
   | `ADSENSE_CLIENT` | already built in (`ca-pub-8705243334753575`); set it to blank to turn ads off |
   | `AD_SLOT_LOBBY` | `1234567890` |
   | `AD_SLOT_FINAL` | `2345678901` |
   | `AD_SLOT_REVEAL` | *(optional – ads between questions)* |
   | `SITE_NAME` | `Black Box Trivia` (or your own name) |

5. The server automatically serves `/ads.txt` from `ADSENSE_CLIENT`.
6. In AdSense go to **Privacy & messaging** and turn on the consent message for EEA/UK visitors (required by Google; no code needed).

Ads sit in their own "Advertisement" window and never appear while a question is being answered. That keeps the game fair and follows AdSense placement policy. Web game portals that specialize in game ads (AdinPlay, Venatus) are alternatives if AdSense declines.

---

## The question bank

`server/questions.json` is generated. **Don't edit it by hand.** Sources live in `data/`:

| File | What it is |
|---|---|
| `data/raw/opentdb.js` | Your original 25k-line file (1,989 unique questions; the rest were repeats) |
| `data/raw/tm.tsv` | Your spreadsheet |
| `data/tm_fixes.json` | Corrections/removals for spreadsheet rows (typos, out-of-date or wrong answers) |
| `data/gk_categories.json` | Which category each "General Knowledge" question belongs in |
| `data/new/*.txt` | New question packs |

Pack format, one question per line:

```
cat|difficulty|question|answer|wrong1;wrong2;wrong3|alternate1;alternate2
geo|3|What is the capital of Australia?|Canberra|Sydney;Melbourne;Perth
```

`cat` is one of `geo ent his art sci spo`. Difficulty is 1 (easy) to 5 (hard). Wrong answers are optional; without them the question is fill-in-only. Alternates are extra accepted spellings or names.

Rebuild after any change:

```bash
npm run build:questions
```

The build removes exact and near-duplicates, decodes HTML entities, auto-adds sensible alternates (surnames for "Who…" questions, "Superior" for "Lake Superior"), and decides which questions work as fill-in-the-blank.

### Growing toward 20,000

`tools/generate-questions.js` drafts new packs with the Claude API for you to **review**:

```bash
ANTHROPIC_API_KEY=sk-ant-... node tools/generate-questions.js --cat his --count 150 --topic "Canadian history 1867-1945"
```

Drafts land in `data/drafts/`. Check the facts, then move the file to `data/new/` and rebuild. Narrow topics give fewer duplicates.

**Licence note:** questions from the original 25k file come from the Open Trivia Database (opentdb.com, CC BY-SA 4.0). Commercial use is allowed with attribution, which is on the About screen. Keep it there.

---

## Project layout

```
server/index.js        Express + Socket.IO server, rooms, 6-digit codes, ads config
server/questions.json  Built question bank
public/index.html      The page
public/js/engine.js    Game rules (shared by server and solo mode)
public/js/match.js     Spelling-tolerant answer checking (shared)
public/js/app.js       Screens, menus, networking
public/js/art.js       Pixel icons, category patterns, the six-piece cube
public/js/sounds.js    Synthesized retro sounds
public/css/retro.css   The 1-bit look
public/fonts/          ChicagoFLF (public-domain recreation of the classic system font)
tools/                 Question build + generator scripts
```

Scoring: 100 for a correct multiple-choice answer, 150 for fill-in, plus up to 50 for speed, +10 per difficulty level above 1, and +25 when you're on a streak of 3 or more.
