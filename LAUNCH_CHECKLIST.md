# Foresight Solutions Launch Checklist

## Pre-Upload

- [ ] Confirm `Derek.Canine@foresightsolutions.io` is the correct public contact email.
- [ ] Replace `https://formspree.io/f/XXXXXXXX` with the live Formspree endpoint.
- [ ] Confirm the AI Scale Diagnostic form posts successfully to Formspree.
- [ ] Confirm Formspree forwards submissions to the correct inbox.
- [ ] Confirm the `_gotcha` honeypot field is present and hidden.
- [ ] Confirm Formspree redirects successful submissions to `thank-you.html`.
- [ ] Confirm the phone row is hidden until a real phone number is available.
- [ ] Confirm the scheduling row is hidden until a real scheduling URL is available.
- [ ] Confirm no live analytics or tracking scripts are present.
- [ ] Confirm no internal style guide or Webflow build guide files are included.
- [ ] Add a real `favicon.ico` file at the site root if favicon display is required at launch.

## GoDaddy Upload

- [ ] Upload the contents of the deployment folder into `public_html`.
- [ ] Confirm `index.html` is at the root of `public_html`.
- [ ] Confirm `styles.css` is at the root of `public_html`.
- [ ] Confirm `robots.txt` is at the root of `public_html`.
- [ ] Confirm `sitemap.xml` is at the root of `public_html`.
- [ ] Confirm `404.html` is at the root of `public_html`.

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
- [ ] Public navigation does not include `style-guide.html`.
- [ ] Public navigation does not include `webflow-build-guide.html`.
- [ ] Privacy appears in footer navigation only.

## CTA QA

- [ ] Homepage primary CTA routes to `contact.html`.
- [ ] Homepage secondary CTA routes to `services.html`.
- [ ] Services CTA routes to `contact.html`.
- [ ] Solution page CTAs route correctly.
- [ ] Topic page CTAs route correctly.
- [ ] Contact email link opens an email draft.
- [ ] AI Scale Diagnostic form posts to Formspree.
- [ ] Successful form submission lands on `thank-you.html`.

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
- [ ] No live tracking scripts are present.
