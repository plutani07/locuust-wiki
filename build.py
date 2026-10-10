"""Writes the site from wiki.src.html: one file per page, index.html, 404.html.

Run from this folder:  python build.py
GitHub Pages serves projects.html at /projects, so a page is a real file with
a real address, and 404.html answers everything else.
"""
import re

PAGES = ['home', 'projects', 'goals', 'android', 'ios', 'misspelling', 'notfound']      # the ids of the pages (<article class="pg" id="...">); "notfound" is 404.html
SRC = open("wiki.src.html", encoding="utf8").read()


def with_page_on(pid):
    marker = '<article class="pg" id="%s"' % pid
    assert marker in SRC, pid
    out = SRC.replace(marker, '<article class="pg on" id="%s"' % pid, 1)
    m = re.search(r'<article class="pg on" id="%s"[\s\S]*?<h1 class="title">(.*?)</h1>' % pid, out)
    if m and pid != "home":
        out = out.replace("<title>Locuust Wiki</title>", "<title>%s - Locuust Wiki</title>" % re.sub("<.*?>", "", m.group(1)), 1)
    return out


for pid in PAGES:
    name = {"home": "index.html", "notfound": "404.html"}.get(pid, pid + ".html")
    open(name, "w", encoding="utf8", newline="\n").write(with_page_on(pid))
    print("wrote", name)
