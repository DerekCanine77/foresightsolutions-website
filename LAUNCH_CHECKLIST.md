# Foresight Solutions Launch Checklist

## Pre-Upload

- [ ] Confirm `Derek.Canine@foresightsolutions.io` is the correct public contact email.
- [ ] Confirm the deployed form action is `https://formspree.io/f/xeagagkw`.
- [ ] Confirm the AI Scale Diagnostic form posts successfully to Formspree.
- [ ] Confirm Formspree forwards submissions to the correct inbox.
- [ ] Confirm the `_gotcha` honeypot field is present and hidden.
- [ ] Confirm the form includes `_next` set to `https://foresightsolutions.io/thank-you.html`.
- [ ] Confirm the Formspree plan or dashboard actually honors that redirect. Some plans ignore `_next` until it is enabled.
- [ ] Confirm no phone number is published.
- [ ] Confirm no scheduling link is published. A real URL is not in the repo. The TODO comment in `contact.html` stays until one exists.
- [ ] Confirm Foresight has not added its own analytics tags. GoDaddy may still inject `tccl.min.js`. `privacy.html` discloses that. Ask GoDaddy to disable it if it should not run.
- [ ] Confirm `docs/` (style guide and Webflow build guide) is not uploaded.
- [ ] Confirm `favicon.ico` and `og-image.png` are served from the site root.
- [ ] Confirm `.htaccess` is uploaded and that a missing URL returns `404.html`.

## GoDaddy Upload

- [ ] Upload the files listed in `README_DEPLOYMENT.md` into `public_html`.
- [ ] Confirm `index.html` is at the root of `public_html`.
- [ ] Confirm `styles.css` is at the root of `public_html`.
- [ ] Confirm `robots.txt` is at the root of `public_html`.
- [ ] Confirm `sitemap.xml` is at the root of `public_html`.
- [ ] Confirm `404.html`, `.htaccess`, and `og-image.png` are at the root of `public_html`.

## Page QA

- [ ] Homepage loads at `https://foresightsolutions.io/`.
- [ ] `solutions.html` loads.
- [ ] `services.html` loads.
- [ ] `palantir-foundry.html` loads.
- [ ] `aip-readiness.html` loads.
- [ ] `ontology-workflow.html` loads.
- [ ] `delivery-pods.html` loads.
- [ ] `industries.html` loads.
- [ ] `how-it-works.html` loads.
- [ ] `about.html` loads.
- [ ] `privacy.html` loads.
- [ ] `contact.html` loads.
- [ ] `thank-you.html` loads and is marked `noindex`.
- [ ] A nonexistent URL displays the 404 page or a GoDaddy 404 fallback.

## Navigation QA

- [ ] Desktop navigation links all route correctly.
- [ ] Mobile menu opens and closes.
- [ ] Mobile navigation links all route correctly.
- [ ] Footer links route correctly.
- [ ] Public navigation does not include `docs/style-guide.html`.
- [ ] Public navigation does not include `docs/webflow-build-guide.html`.
- [ ] Privacy appears in footer navigation only.

## CTA QA

- [ ] Homepage primary CTA routes to `contact.html`.
- [ ] Homepage secondary CTA routes to `services.html`.
- [ ] Services CTA routes to `contact.html`.
- [ ] Solution page CTAs route correctly.
- [ ] Topic page CTAs route correctly.
- [ ] Contact email link opens an email draft.
- [ ] AI Scale Diagnostic form posts to Formspree.
- [ ] Successful form submission lands on `thank-you.html` when the Formspree plan allows `_next`.

## SEO And Indexing

- [ ] Page titles appear correctly in browser tabs.
- [ ] Meta descriptions are present.
- [ ] Canonical URLs use `https://foresightsolutions.io`.
- [ ] `https://foresightsolutions.io/robots.txt` loads.
- [ ] `https://foresightsolutions.io/sitemap.xml` loads.
- [ ] `thank-you.html` is not included in `sitemap.xml`.
- [ ] Submit sitemap in Google Search Console after launch.

## Responsive QA

- [ ] Test homepage on mobile.
- [ ] Test contact page on mobile.
- [ ] Test services page on mobile.
- [ ] Confirm no horizontal scrolling.
- [ ] Confirm buttons fit within mobile viewport.
- [ ] Confirm text remains readable on mobile.

## Final Launch Checks

- [ ] HTTPS is active.
- [ ] Domain resolves correctly.
- [ ] No visible bracketed placeholders remain.
- [ ] No dummy phone number remains.
- [ ] No old `.com` Foresight domain references remain.
- [ ] Contact path is ready for real inquiries.
- [ ] No Foresight-owned tracking script is present. If GoDaddy still injects `tccl.min.js`, the privacy page describes it.
