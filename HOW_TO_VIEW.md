# How to view `index.html`

GitHub's web UI does **not** render HTML — it shows source code. You
have to serve the file with an actual HTTP server (or enable GitHub
Pages). Three options:

## Local (fastest)

```bash
cd eth
python3 -m http.server
# open http://localhost:8000
```

## GitHub Pages

1. Repo → **Settings** → **Pages**
2. **Source**: Deploy from a branch
3. **Branch**: `claude/enteric-translation-hypothesis-EQsVH` (or merge to `main`)
4. **Folder**: `/ (root)`
5. Save · wait ~60 seconds
6. Open `https://<owner>.github.io/<repo>/`

The `.nojekyll` marker is already committed so Pages won't try to
process files with Jekyll.

## HTML preview service (no setup)

Paste a raw-file URL into https://htmlpreview.github.io/ — limited
support for fetch/assets but the toggle button will render.

## The toggle button

Once the page renders, you'll see **two** toggles:

- **Inline** · top-right of the page header, in normal document flow
- **Floating** · fixed to the top-right corner, visible on scroll

Both flip the entire page between kotoba (dense glyphs) and plain
English readings. They're wired to the same handler; click either.
