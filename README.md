# website

Source for [thomasbiegert.github.io](https://thomasbiegert.github.io). A small
dependency-free Python static-site generator — no Hugo/Node toolchain required.

## Structure

- `content.py` — all page text, nav, and social links. Edit this to update copy.
- `templates/base.html` — shared page shell (nav, footer). Rarely needs changes.
- `static/` — CSS, the hero image, and the published CV PDF.
- `build.py` — renders `content.py` through the template and writes the result
  into `../thomasbiegert.github.io/`.
- `cv/cv.tex` — LaTeX source for the CV (replaces the old lost Markdown+pandoc
  source; built with `moderncv`, style `classic`/`red`). Compile with
  `pdflatex`, then copy the result into `static/files/cv_tbiegert.pdf` before
  running `build.py`.

## Editing the site

1. Edit `content.py` (text/links) and/or `static/` (CSS, image). To update
   the CV, edit `cv/cv.tex`, then:

   ```bash
   cd cv && pdflatex -interaction=nonstopmode cv.tex && pdflatex -interaction=nonstopmode cv.tex
   cp cv.pdf ../static/files/cv_tbiegert.pdf
   cd ..
   ```

2. Run:

   ```bash
   python3 build.py
   ```

3. Preview locally, e.g.:

   ```bash
   python3 -m http.server 8073 --directory ../thomasbiegert.github.io
   ```

4. Commit and push changes in **both** repos: this one (source) and
   `thomasbiegert.github.io` (published output — GitHub Pages serves directly
   from its root).

## Notes

- Publication list content is carried over as-is from the previous site; a
  fuller revision of `PUBLICATIONS_CONTENT` in `content.py` is planned
  separately.
- `/about/` redirects to `/` since the About page was merged into Home.
- The CV's "Research visits", "Teaching", and "Service" sections still
  reflect July 2024; updates to those are planned separately.
