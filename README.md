# Locuust Wiki

A fake wiki for Locuust, in one plain HTML file. No build step, no framework.

- `index.html` - the whole wiki (four main pages, example pages, a not-found page)
- `background.webp` - the background picture; keep it beside `index.html`

Edit the words in `index.html`. To add a page, copy an `<article class="pg">`
block, give it a new `id`, and link to it with `#that-id`.
