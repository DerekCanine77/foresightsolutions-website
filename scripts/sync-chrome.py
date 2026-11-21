#!/usr/bin/env python3
"""Stamp shared header, footer, and social tags into committed HTML.

Run this locally after editing partials/header.html or partials/footer.html:

    python3 scripts/sync-chrome.py

GoDaddy serves the committed HTML. Do not run this on the server, and do not
add a build step to the host. Pages outside this list, including docs/, are
left alone.
"""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HEADER = (ROOT / "partials" / "header.html").read_text()
FOOTER = (ROOT / "partials" / "footer.html").read_text()

# filename, aria-current key, link prefix ("" at site root, "/" for the 404
# document, which Apache serves under the visitor's missing path)
PAGES = [
    ("index.html", "home", ""),
    ("solutions.html", "solutions", ""),
    ("services.html", "services", ""),
    ("palantir-foundry.html", "foundry", ""),
    ("aip-readiness.html", "", ""),
    ("ontology-workflow.html", "", ""),
    ("delivery-pods.html", "", ""),
    ("industries.html", "industries", ""),
    ("how-it-works.html", "how", ""),
    ("about.html", "about", ""),
    ("privacy.html", "privacy", ""),
    ("contact.html", "contact", ""),
    ("thank-you.html", "", ""),
    ("404.html", "", "/"),
]

ARIA_KEYS = [
    "home",
    "solutions",
    "services",
    "foundry",
    "industries",
    "how",
    "about",
    "contact",
    "privacy",
]

OG_IMAGE = "https://foresightsolutions.io/og-image.png"
OG_ALT = "Foresight Solutions. Technology and execution partner for clearer operating decisions."

CANONICAL_RE = re.compile(r'<link\s+rel="canonical"\s+href="([^"]+)"\s*/?>', re.I)
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S)
DESC_RE = re.compile(r'<meta\s+name="description"\s+content="([^"]*)"\s*/?>', re.I)
SOCIAL_RE = re.compile(
    r"[ \t]*<meta\s+(?:property=\"og:[^\"]+\"|name=\"twitter:[^\"]+\")[^>]*>[ \t]*\n",
    re.I,
)
HEADER_RE = re.compile(r"<header class=\"site-header\">.*?</header>", re.S)
FOOTER_RE = re.compile(r"<footer class=\"site-footer\">.*?</footer>", re.S)


def render(template: str, prefix: str, current: str) -> str:
    rendered = template.replace("{{ROOT}}", prefix)
    for key in ARIA_KEYS:
        token = "{{ARIA:%s}}" % key
        value = ' aria-current="page"' if key == current else ""
        rendered = rendered.replace(token, value)
    if "{{" in rendered:
        raise SystemExit("Unresolved template token in chrome partials")
    return rendered.strip("\n")


def canonical_for(name: str, existing: str | None) -> str:
    if existing:
        return existing
    if name == "index.html":
        return "https://foresightsolutions.io/"
    return "https://foresightsolutions.io/" + name


def social_block(title: str, description: str, url: str) -> str:
    lines = [
        f'<meta property="og:site_name" content="Foresight Solutions">',
        f'<meta property="og:type" content="website">',
        f'<meta property="og:url" content="{url}">',
        f'<meta property="og:title" content="{title}">',
        f'<meta property="og:description" content="{description}">',
        f'<meta property="og:image" content="{OG_IMAGE}">',
        f'<meta property="og:image:width" content="1200">',
        f'<meta property="og:image:height" content="630">',
        f'<meta property="og:image:alt" content="{OG_ALT}">',
        f'<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{title}">',
        f'<meta name="twitter:description" content="{description}">',
        f'<meta name="twitter:image" content="{OG_IMAGE}">',
        f'<meta name="twitter:image:alt" content="{OG_ALT}">',
    ]
    return "\n  ".join(lines)


def stamp(name: str, current: str, prefix: str) -> None:
    path = ROOT / name
    html = path.read_text()
    title_match = TITLE_RE.search(html)
    desc_match = DESC_RE.search(html)
    if not title_match or not desc_match:
        raise SystemExit(f"{name} is missing a title or meta description")
    title = " ".join(title_match.group(1).split())
    description = " ".join(desc_match.group(1).split())

    html = SOCIAL_RE.sub("", html)
    canon_match = CANONICAL_RE.search(html)
    url = canonical_for(name, canon_match.group(1) if canon_match else None)
    block = "  " + social_block(title, description, url)
    if canon_match:
        html = html[: canon_match.end()] + "\n" + block + html[canon_match.end() :]
    else:
        canonical = f'  <link rel="canonical" href="{url}">\n{block}'
        html = DESC_RE.sub(lambda m: m.group(0) + "\n" + canonical, html, count=1)

    header = render(HEADER, prefix, current)
    footer = render(FOOTER, prefix, current)
    html, n_header = HEADER_RE.subn(header, html, count=1)
    html, n_footer = FOOTER_RE.subn(footer, html, count=1)
    if n_header != 1 or n_footer != 1:
        raise SystemExit(f"{name} header/footer replacements: {n_header}/{n_footer}")
    if not html.endswith("\n"):
        html += "\n"
    path.write_text(html)
    print(f"updated {name}")


def main() -> None:
    for name, current, prefix in PAGES:
        stamp(name, current, prefix)


if __name__ == "__main__":
    main()
