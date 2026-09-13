# FL-07: Mobile Audit & Fix Log

## Issues Found and Fixed

| Issue | Where | Why it was a problem | Fix |
|---|---|---|---|
| Hero Section Stat Cards Overflow | `#hero` / `.metrics` | The 4-column stat grid ("8 Production Apps", "9.2 CGPA", etc.) did not wrap on narrow screens, causing severe horizontal scrolling and cutoff text. | Added `@media (max-width: 768px)` to force `#hero` into a 1-column layout (`grid-template-columns: 1fr`) and `.metrics` into a vertical flex column (`flex-direction: column`). |
| Skills Tag Pills Overflow | `.tags` / `.skill-tags` | The language and technology tags inside the profile cards were forced onto a single line without wrapping, pushing outside the card boundaries on 375px screens. | Added `flex-wrap: wrap !important` to all `.tags` and tag pill containers on mobile to allow them to wrap naturally. |
| Footer Contact & Copyright Overflow | `.contact-line` / Footer | The contact action buttons (email, GitHub, LinkedIn) extended beyond the right viewport margin on narrow devices. | Added `flex-wrap: wrap` to `.contact-line` and related flex containers to stack cleanly. |
| Ask Krish AI Suggestion Chips Overflow | `#agent-suggestions` | The suggestion buttons ("What did Krish build?") inside the Ask Krish AI chat modal were cut off and couldn't be scrolled. | Applied `overflow-x: auto` and `white-space: nowrap` to the `#agent-suggestions` wrapper to allow horizontal swiping/scrolling of chips. |
| Ask Krish AI Chat Window Sizing | `#agent-modal` | The chat window was slightly too wide or tall for smaller screens, causing it to clip behind the browser URL bar. | Adjusted `.agent-container` max-width and max-height for mobile viewports using media queries. |

## Mobile Check

The portfolio was audited at common mobile widths (320px, 375px, 390px, 430px) and tablet widths (768px) using developer tools and browser subagents.

- [x] Mobile layout works
- [x] Text readable
- [x] No horizontal overflow
- [x] Images fit correctly
- [x] Buttons/links usable
- [x] Ask Krish AI usable
- [x] Navigation works
- [x] Important links work
