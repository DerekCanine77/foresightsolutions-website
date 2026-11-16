# Foresight Solutions Website Deployment

Production static website for Foresight Solutions LLC.

## Folder Contents

The deployable files are at the repository root. The documented release process is a manual upload to GoDaddy `public_html`. The repository has no deployment workflow.

```text
repository root/
├── 404.html
├── about.html
├── aip-readiness.html
├── contact.html
├── delivery-pods.html
├── favicon.ico
├── how-it-works.html
├── index.html
├── industries.html
├── ontology-workflow.html
├── palantir-foundry.html
├── privacy.html
├── robots.txt
├── services.html
├── sitemap.xml
├── solutions.html
├── thank-you.html
└── styles.css
```

Upload only the files listed above. Exclude Git metadata, documentation, and the internal style and Webflow guides. The site uses a local favicon and stylesheet, with no build step or external font, script, or framework dependencies.

## GoDaddy Upload Instructions

1. Log in to GoDaddy.
2. Open the hosting product for `foresightsolutions.io`.
3. Open File Manager.
4. Navigate to `public_html`.
5. Upload the production files listed above directly into `public_html`.
6. Confirm `index.html` is directly inside `public_html`.
7. Confirm `styles.css`, `robots.txt`, `sitemap.xml`, and `404.html` are also directly inside `public_html`.
8. Visit `https://foresightsolutions.io/` after upload.
9. Test the main navigation, mobile menu, CTA buttons, email link, and AI Scale Diagnostic form.

## Contact Configuration

Primary contact email is live and visible on `contact.html`:

- `Derek.Canine@foresightsolutions.io`

Phone number location:

- File: `contact.html`
- Section: `Contact Foresight Solutions`
- Current behavior: phone row is intentionally hidden.
- When a real phone number is ready, add a visible `.contact-method` row near the existing email row.

Scheduling link location:

- File: `contact.html`
- Section: `Contact Foresight Solutions`
- Current behavior: scheduling row is intentionally hidden.
- When a real scheduling URL is ready, add a visible `.contact-method` link near the existing email row.

Form endpoint location:

- File: `contact.html`
- Element: AI Scale Diagnostic `<form>`
- Endpoint: `https://formspree.io/f/xeagagkw`
- The form uses `method="POST"` and includes a `_gotcha` honeypot spam field.

Redirect behavior:

- `thank-you.html` exists as the post-submit confirmation page.
- `thank-you.html` is marked `noindex` and intentionally excluded from `sitemap.xml`.
- If the Formspree plan supports a custom redirect, configure `https://foresightsolutions.io/thank-you.html` in Formspree Settings.
- After upload, verify receipt and redirect behavior with one authorized test submission.

## Tracking And Verification

No live analytics or tracking scripts are included.

When ready, add verification/tracking through the selected deployment process:

- Google Search Console verification
- Google Analytics 4
- LinkedIn Insight Tag

Confirm privacy and consent requirements before adding live tracking.

## Hosting Notes

- The site is fully static HTML/CSS.
- No build step is required.
- No JavaScript is required.
- No database is required.
- No package manager or dependency install is required.
- The AI Scale Diagnostic form is static-hosting compatible and posts to Formspree.

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

Keep `style-guide.html` and `webflow-build-guide.html` out of the upload.
