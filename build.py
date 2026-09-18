#!/usr/bin/env python3
"""Static site generator for thomasbiegert.github.io.

Stdlib only (no Hugo/Node dependency). Edit content.py, then run:

    python3 build.py

This writes the rendered site into ../thomasbiegert.github.io/.
"""
import shutil
from pathlib import Path

from content import PAGES, NOT_FOUND_PAGE, NAV, SOCIAL_LINKS, SITE

ROOT_DIR = Path(__file__).parent
OUT_DIR = ROOT_DIR.parent / "thomasbiegert.github.io"

TEMPLATE = (ROOT_DIR / "templates" / "base.html").read_text()


def render_nav(active_href):
    items = []
    for label, href in NAV:
        cls = ' class="active"' if href == active_href else ""
        items.append(f'<li{cls}><a href="{href}">{label}</a></li>')
    return "\n                ".join(items)


def render_social():
    links = []
    for label, url, svg in SOCIAL_LINKS:
        links.append(
            f'<a class="icon-link" href="{url}" aria-label="{label}" '
            f'target="_blank" rel="noopener">{svg}</a>'
        )
    return "\n            ".join(links)


def render_page(page):
    html = TEMPLATE
    html = html.replace("{{TITLE}}", page["title"])
    html = html.replace("{{DESCRIPTION}}", page.get("description", SITE["description"]))
    html = html.replace("{{NAV}}", render_nav(page["nav_href"]))
    html = html.replace("{{SOCIAL}}", render_social())
    html = html.replace("{{CONTENT}}", page["content"].strip())
    html = html.replace("{{YEAR}}", SITE["year"])
    # Site is served from the domain root, so {{ROOT}} always resolves to "/".
    html = html.replace("{{ROOT}}", "/")
    return html


def write(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    print("wrote", path.relative_to(OUT_DIR.parent))


def main():
    for slug, page in PAGES.items():
        out_path = OUT_DIR / slug / "index.html" if slug else OUT_DIR / "index.html"
        write(out_path, render_page(page))

    write(OUT_DIR / "404.html", render_page(NOT_FOUND_PAGE))

    # Redirect for the retired /about/ URL (About is now merged into Home).
    redirect_html = (
        "<!DOCTYPE html><html><head><meta charset=\"utf-8\">"
        "<meta http-equiv=\"refresh\" content=\"0; url=/\">"
        "<link rel=\"canonical\" href=\"https://thomasbiegert.github.io/\">"
        "</head><body>This page has moved to <a href=\"/\">thomasbiegert.github.io</a>.</body></html>"
    )
    write(OUT_DIR / "about" / "index.html", redirect_html)

    # static assets
    css_out = OUT_DIR / "css" / "style.css"
    css_out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(ROOT_DIR / "static" / "css" / "style.css", css_out)
    print("copied", css_out.relative_to(OUT_DIR.parent))

    img_out = OUT_DIR / "img" / "thomas-gears.jpg"
    img_out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(ROOT_DIR / "static" / "img" / "thomas-gears.jpg", img_out)
    print("copied", img_out.relative_to(OUT_DIR.parent))

    pdf_out = OUT_DIR / "files" / "cv_tbiegert.pdf"
    pdf_out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(ROOT_DIR / "static" / "files" / "cv_tbiegert.pdf", pdf_out)
    print("copied", pdf_out.relative_to(OUT_DIR.parent))

    # sitemap
    slugs = [s for s in PAGES if isinstance(s, str)]
    urls = [f"{SITE['base_url']}/{slug}/" if slug else f"{SITE['base_url']}/" for slug in slugs]
    sitemap = ['<?xml version="1.0" encoding="utf-8" standalone="yes"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sitemap.append(f"  <url><loc>{u}</loc></url>")
    sitemap.append("</urlset>\n")
    write(OUT_DIR / "sitemap.xml", "\n".join(sitemap))


if __name__ == "__main__":
    main()
