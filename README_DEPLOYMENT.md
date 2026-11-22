# Foresight Solutions Website Deployment

Production static website for Foresight Solutions LLC.

## Folder Contents

The deployable files are at the repository root. The documented release process is a manual upload to GoDaddy `public_html`. The repository has no deployment workflow, and the server does not run a build.

```text
repository root/
├── .htaccess
├── 404.html
├── 404.shtml
├── about.html
├── apple-touch-icon.png
├── assets/logo.svg
├── assets/logo-header.svg
├── assets/logo-mark.svg
├── aip-readiness.html
├── assessment.html
├── contact.html
├── delivery-pods.html
├── favicon-32.png
├── favicon.ico
├── favicon.svg
├── how-it-works.html
├── index.html
├── industries.html
├── og-image.png
├── ontology-workflow.html
├── palantir-foundry.html
├── privacy.html
├── robots.txt
├── services.html
├── site.js
├── sitemap.xml
├── solutions.html
├── thank-you.html
└── styles.css
```

Upload only the files listed above. Do not upload Git metadata, `docs/`, `partials/`, `scripts/`, or the Markdown notes.

`docs/` holds the internal style guide and Webflow build guide. `robots.txt` disallows `/docs/`. Those pages are also marked `noindex`.

Shared header, footer, and social tags are already written into the HTML. If you edit `partials/header.html` or `partials/footer.html`, regenerate locally with:

```text
python3 scripts/sync-chrome.py
```

Then commit the HTML. Do not run that script on GoDaddy.

The site uses a local favicon, a local Open Graph image, and a local stylesheet. Pages use the system font stack. No external font, framework, or Foresight-owned analytics script is included.

## GoDaddy Upload Instructions

1. Log in to GoDaddy.
2. Open the hosting product for `foresightsolutions.io`.
3. Open File Manager.
4. Navigate to `public_html`.
5. Upload the production files listed above directly into `public_html`, including `.htaccess` and `og-image.png`.
6. Confirm `index.html` is directly inside `public_html`.
7. Confirm `styles.css`, `robots.txt`, `sitemap.xml`, `404.html`, `404.shtml`, `.htaccess`, and `og-image.png` are also directly inside `public_html`.
8. Visit `https://foresightsolutions.io/` after upload.
9. Test the main navigation, mobile menu, CTA buttons, email link, AI Scale Diagnostic form, a missing URL (custom 404), `http://` and `www` redirects, and response headers.

`.htaccess` sends HTTP and `www` to `https://foresightsolutions.io`, sets `ErrorDocument 404 /404.html`, and adds security and cache headers. GoDaddy's server also serves `404.shtml` for missing URLs and that file overrides `ErrorDocument`, so `404.shtml` is an exact copy of `404.html` and must be uploaded with it. Confirm GoDaddy allows `.htaccess` overrides for this host. If a redirect loops, the HTTPS rule is written to stop when `X-Forwarded-Proto` is already `https`.

## Contact Configuration

Primary contact email is live and visible on `contact.html`:

- `Derek.Canine@foresightsolutions.io`

Phone number:

- `248-703-4466` is visible on `contact.html` and links to `tel:+12487034466`.
- The homepage Organization JSON-LD includes `"telephone": "+1-248-703-4466"`.

Scheduling link:

- No scheduling URL exists in this repository.
- `contact.html` has an HTML comment, `TODO(Derek): add a real scheduling URL`, where a link would go.
- Leave that comment in place until a real URL is available. Do not publish a placeholder link.

Form endpoint:

- File: `contact.html`
- Element: AI Scale Diagnostic `<form>`
- Endpoint: `https://formspree.io/f/xeagagkw`
- The form uses `method="POST"` and includes a `_gotcha` honeypot spam field.
- Name, work email, and company are required. Role, primary constraint, and message are optional.
- A hidden `_next` field points to `https://foresightsolutions.io/thank-you.html`.

Redirect behavior:

- `thank-you.html` exists as the post-submit confirmation page.
- `thank-you.html` is marked `noindex` and is excluded from `sitemap.xml`.
- Formspree may ignore `_next` until a paid plan or a dashboard setting allows custom redirects. Confirm that before expecting the thank-you page.
- The same URL can be set in Formspree Settings if the dashboard is the source of truth for the plan.
- After upload, verify receipt and redirect behavior with one authorized test submission.

## Tracking And Verification

Foresight Solutions does not include its own analytics or advertising tags.

GoDaddy may still inject its own traffic and performance script on live pages, at `https://img1.wsimg.com/traffic-assets/js/tccl.min.js`. That script is not in this repository. It can send data to `https://csp.secureserver.net`. `privacy.html` discloses this. The account owner can ask GoDaddy to disable the injected script.

`.htaccess` allows that script and its beacon in the Content Security Policy so the host injection does not break the page. The policy also allows the diagnostic form to post to `https://formspree.io`.

If Foresight later adds Google Analytics, Search Console verification, or a LinkedIn Insight Tag, update `privacy.html` first. The current notice says those tags are not on the site.

## Hosting Notes

- The site is fully static HTML/CSS.
- No build step is required on the server.
- A small deferred script, `site.js`, adds scroll reveal, the homepage illustration, and the self-assessment. The pages remain readable without it.
- No database is required.
- No package manager or dependency install is required.
- The AI Scale Diagnostic form is static-hosting compatible and posts to Formspree.
- CSS, favicon, and images are cached for 7 days by `.htaccess`.

## Public Navigation

The public navigation includes:

- Solutions
- Services
- Foundry
- Industries
- How It Works
- About
- Request AI Scale Diagnostic

Privacy is linked in footer navigation only.

The footer states that Palantir, Foundry, AIP, and Workshop are trademarks of Palantir Technologies Inc., and that Foresight Solutions is not affiliated with or endorsed by Palantir.
