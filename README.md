# Locuust Wiki

A fake wiki for Locuust. Plain HTML, no framework. Live at https://wiki.locuust.com

- `wiki.src.html` - the source. **Edit this one.**
- `build.py` - run `python build.py` after editing. It writes one file per page
  (`projects.html` is served at `/projects`), `index.html` for the front page and
  `404.html` for every address that is not a page.
- `background.webp` - the background picture.

Every address is a real file, so `/projects` works when typed, shared or
refreshed. To add a page: copy an `<article class="pg">` block in
`wiki.src.html`, give it an id, link to it as `href="/that-id"`, add the id to
`PAGES` in `build.py`, and build.
