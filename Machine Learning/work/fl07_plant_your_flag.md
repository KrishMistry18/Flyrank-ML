# FL-07: Plant Your Flag — Domain + Badge

## 1. Assignment Overview
This document covers the "Plant Your Flag: Domain + Badge" assignment for FlyRank General AI Fluency Week 7. The goal is to harden the deployed portfolio with a proper domain/address, free analytics, launch hygiene (favicon, SEO meta, social share preview), and the FlyRank graduate badge.

## 2. Final Domain
**Live URL:** https://portfolio-eta-pied-17.vercel.app/

**Status:** The portfolio is deployed on Vercel's free tier with automatic HTTPS. A custom domain has not been purchased or configured because the budget is effectively zero. The Vercel-provided HTTPS URL serves as the clean fallback address.

**Custom Domain — Manual Steps Required:**
If I want to point a custom domain (e.g. `krishmistry.dev`) in the future:
1. Purchase a domain from Namecheap, Cloudflare, or Google Domains.
2. In the Vercel project dashboard → Settings → Domains → Add Domain.
3. Set DNS records at the registrar:
   - `A` record → `76.76.21.21` (Vercel)
   - `CNAME` for `www` → `cname.vercel-dns.com`
4. Vercel will automatically provision an SSL certificate.
5. Update `og:url` in `index.html` to the new domain.

## 3. Hosting Configuration
- **Platform:** Vercel (free tier)
- **Build:** Static HTML portfolio, no build step
- **API:** Serverless function at `/api/chat` (Gemini-powered Ask Krish AI)
- **HTTPS:** Automatic via Vercel

## 4. HTTPS Verification
- ✅ The site loads over HTTPS at `https://portfolio-eta-pied-17.vercel.app/`
- ✅ HTTP automatically redirects to HTTPS (Vercel default behavior)
- ✅ Valid SSL certificate issued by Let's Encrypt via Vercel

## 5. Analytics Implementation
- **Provider:** GoatCounter (https://goatcounter.com)
- **Why:** Free, open-source, privacy-friendly, no cookies, GDPR-compliant, lightweight (~3.5 KB script)
- **Implementation:** Single `<script>` tag added to `<head>`:
  ```html
  <script data-goatcounter="https://krishmistry.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
  ```
- **Dashboard:** https://krishmistry.goatcounter.com (after account signup)

## 6. Analytics Verification
**IMPORTANT:** GoatCounter requires a free account signup at https://goatcounter.com/signup to activate the `krishmistry.goatcounter.com` endpoint. The script tag is installed in the HTML, but the account must be created manually for data to be recorded.

**Manual step:** Sign up at https://goatcounter.com/signup with subdomain `krishmistry` to activate the analytics endpoint.

## 7. Page Title
- ✅ `<title>Krish Hitendra Mistry — Full Stack Developer</title>`

## 8. Meta Description
- ✅ `<meta name="description" content="Full Stack Developer · AI Systems · Mumbai. 8 production apps. Building reliable, scalable software with Next.js, Django, Flutter, and TensorFlow.">`

## 9. Open Graph / Share Preview Metadata
- ✅ `og:title`: "Krish Mistry — Full Stack Developer & AI Builder"
- ✅ `og:description`: Present and descriptive
- ✅ `og:url`: https://portfolio-eta-pied-17.vercel.app/
- ✅ `og:type`: website
- ✅ `og:image`: https://portfolio-eta-pied-17.vercel.app/assets/profile/My_profile_picture.jpeg
- ✅ `twitter:card`: summary_large_image
- ✅ `twitter:title`: Present
- ✅ `twitter:description`: Present
- ✅ `twitter:image`: Present

## 10. Favicon
- **Status:** Added
- **File:** `assets/profile/favicon.svg` — minimal SVG with "KM" initials on a dark background matching the portfolio's color identity (#0d0f1a background, #4f8ef7 accent).
- **HTML:** `<link rel="icon" type="image/svg+xml" href="assets/profile/favicon.svg">`

## 11. FlyRank Graduate Badge
- **Status:** Added to footer
- **Location:** Bottom of the `.footer-bar` section, after the visitor counter
- **Design:** Inline-styled `<a>` tag with a checkmark SVG icon and "FlyRank Graduate" text. Uses the portfolio's accent color (#4f8ef7) with a subtle border and background. Hover effect included.
- **Verification URL:** https://internship.flyrank.ai/verify
- **Opens in:** New tab (`target="_blank"`)

## 12. Badge Verification URL
https://internship.flyrank.ai/verify

## 13. Mobile Validation
- The badge is inline-flex with small padding (6px 14px) and 0.75rem font, so it wraps cleanly on narrow viewports.
- Previous mobile fixes (hero metrics, skill tags, footer, Ask Krish AI modal) remain intact.
- The `.footer-bar` already has `flex-wrap: wrap` which prevents horizontal overflow.

## 14. Limitations / Manual Steps Required

| Item | Status | Manual Action Required |
|------|--------|----------------------|
| Custom domain | NOT configured | Purchase domain + configure DNS (see Section 2) |
| GoatCounter account | Script installed, account NOT created | Sign up at https://goatcounter.com/signup with subdomain `krishmistry` |
| Social share preview test | Metadata verified in source | Test with https://opengraph.xyz or share the URL on LinkedIn/Twitter |
| Favicon rendering | SVG created and linked | Verify in browser tab after Vercel deployment |
| Badge verification | Links to official page | Verify credential is listed after FlyRank issues it |
