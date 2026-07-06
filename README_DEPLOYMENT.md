# Foresight Solutions Website Deployment

Production static website for Foresight Solutions LLC.

## Folder Contents

Upload the contents of this folder directly into the GoDaddy `public_html` directory.

```text
updated_site_package/
├── 404.html
├── README_DEPLOYMENT.md
├── LAUNCH_CHECKLIST.md
├── CHANGELOG.md
├── about.html
├── aip-readiness.html
├── contact.html
├── delivery-pods.html
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

There is no assets folder because the production site currently uses CSS-only visuals and has no image, font, JavaScript, or framework dependencies.

## GoDaddy Upload Instructions

1. Log in to GoDaddy.
2. Open the hosting product for `foresightsolutions.io`.
3. Open File Manager.
4. Navigate to `public_html`.
5. Upload the contents of this folder, not the folder itself.
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
- Future value marker in source comment: `[PHONE TO BE PROVIDED BEFORE DEPLOYMENT]`
- When a real phone number is ready, add a visible `.contact-method` row near the existing email row.

Scheduling link location:

- File: `contact.html`
- Section: `Contact Foresight Solutions`
- Current behavior: scheduling row is intentionally hidden.
- Future value marker in source comment: `[CALENDLY URL TO BE PROVIDED BEFORE DEPLOYMENT]`
- When a real scheduling URL is ready, add a visible `.contact-method` link near the existing email row.

Form endpoint location:

- File: `contact.html`
- Element: AI Scale Diagnostic `<form>`
- Current placeholder endpoint: `https://formspree.io/f/XXXXXXXX`
- Before launch, replace the placeholder endpoint with the live Formspree endpoint for this project.
- The form uses `method="post"` and includes a `_gotcha` honeypot spam field.

Redirect behavior:

- `thank-you.html` exists as the post-submit confirmation page.
- `thank-you.html` is marked `noindex` and intentionally excluded from `sitemap.xml`.
- The form includes Formspree-compatible `_next` redirect intent pointing to `https://foresightsolutions.io/thank-you.html`.
- Also confirm redirect behavior inside the Formspree project settings after replacing the placeholder endpoint.

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
- Do not deploy the form for active lead capture until `https://formspree.io/f/XXXXXXXX` is replaced.

## Public Navigation

The public navigation includes:

- Solutions
- Services
- Foundry
- Industries
- How It Works
- Request Diagnostic

Privacy is linked in footer navigation only.

Internal `style-guide.html` and `webflow-build-guide.html` pages are not included in this production package and are not exposed in navigation.
