# FL-07: Break Your Own Site

## 1. Assignment Overview
This document serves as evidence for the "Break Your Own Site" assignment, detailing the break-testing, auditing, and hardening performed on the portfolio site.

## 2. Live URL
https://portfolio-eta-pied-17.vercel.app/

## 3. Tests Performed
- **Ask Krish AI Input Tests:** Submitted empty string, whitespace-only, very long text (500 chars), and rapid double submission.
- **Link & Navigation Tests:** Clicked through GitHub profile, LinkedIn, Resume, email contact, and project demo/repo links.
- **Findability/Meta Tests:** Audited `<head>` for `<title>`, `<meta name="description">`, and `og:` metadata.
- **Speed & Performance:** Monitored console for runtime errors and manually observed loading of assets (including interactive 3D WebGL).

## 4. What Actually Broke / Findings Log
1. **Ask Krish AI (Input Validation):** Submitting empty strings or whitespace-only inputs produced no user feedback or error states (it failed silently).
2. **Ask Krish AI (Length Limit):** Submitting 500-character single-word strings failed silently without character limit warnings.
3. **Ask Krish AI (Double Submission):** Double submission protection worked correctly; inputs were cleared synchronously on the first click.
4. **Links:** All links successfully verified (no 404s).
5. **Metadata:** `<title>`, `<meta name="description">`, `og:title`, `og:description`, and `og:image` were successfully verified to be present in the source code.
6. **Performance:** Console logs were 100% clean (0 errors), and 3D rendering performed smoothly.

## 5. FIX-NOW Findings
- **Ask Krish AI Form Acceptance:** Form silently accepted (and then ignored) invalid empty/whitespace inputs.
- **Ask Krish AI Length Limitation:** No UI feedback when submitting excessively long text strings that break the bot payload.

## 6. KNOWN LIMITATIONS
- **Performance Tooling:** Formal Lighthouse measurement was not available in the current automated browser testing environment; basic loading/performance was manually checked via the Network and Console tabs.
- **Search Engine Indexing:** True ranking for specific queries cannot be verified immediately as Google indexing takes time.
- **Vercel API Limits:** Ask Krish AI depends on the availability of the Vercel Serverless Function and Google Gemini API.

## 7. Fixes Implemented
- **`agent.js`:** Added UI validation to `sendMessage()`. Empty/whitespace submissions now trigger a red border on the input field for 2 seconds. Submitting strings longer than 300 characters now renders an inline bot message: "Message too long. Please keep it under 300 characters."

## 8. Before/After Evidence
- **Before:** Submitting empty text in Ask Krish AI did nothing; the user was left confused as to why the button wasn't working.
- **After:** Submitting empty text highlights the input box with a red border (`1px solid #ff4444`) to provide clear visual validation feedback.

## 9. SEO/Meta Checks
- `<title>`: Present ("Krish Hitendra Mistry — Full Stack Developer")
- `<meta name="description">`: Present
- `og:title`: Present
- `og:description`: Present
- `og:image`: Present

## 10. Speed/Performance Check
- Clean console (0 errors).
- All standard assets loaded successfully without blocking resources.
- Interactive WebGL rendered at full frame rate.

## 11. Navigation/Link Checks
- **Result:** PASSED. All GitHub and Vercel/Render demo URLs are valid.

## 12. Mobile Checks
- **Result:** PASSED. Previous mobile fixes (hero section, Ask Krish AI 100dvh modal, footer padding) remained intact during the audit.

## 13. Final Validation
- Repeated Ask Krish AI empty input tests and verified the red border appears.
- Repeated long string test and verified the 300-character limit warning appears.
- Site deployed functionality remains stable.

## 14. Tests That Could Not Be Performed
- True Lighthouse audit was unavailable in the browser subagent environment.
- Live Google Search indexing ranking verification (not yet indexed).
