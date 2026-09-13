# Demo Recording Checklist: Ask Krish AI

Follow these exact steps to record your 3–5 minute live demo for the FL-09 assignment.

## 1. Setup & Environment
- [ ] Screen recording software ready (e.g., Loom, OBS, QuickTime).
- [ ] Microphone tested and working.
- [ ] Browser window open to the live portfolio: `https://portfolio-eta-pied-17.vercel.app/`. Ensure no sensitive tabs are visible.
- [ ] Code editor open in the background with `Machine Learning/portfolio/api/chat.js` and `data/krish-knowledge.json` ready to show.
- [ ] Target duration: **3 to 5 minutes**.

## 2. The Recording Run
- [ ] **Start Recording.**
- [ ] **Introduction (30s):** State your name, what Ask Krish AI is, and who it's for (recruiters/hiring managers).
- [ ] **Live Demo (1m):**
    - Click the chat bubble.
    - Ask: *"What AI projects has Krish built?"*
    - Read the response. Briefly explain the serverless flow (UI -> `/api/chat.js` -> Gemini 2.5 Flash -> UI).
- [ ] **Design Decision (1m):**
    - Switch to your code editor or explain verbally.
    - **What:** Injecting a structured JSON knowledge base directly into the prompt instead of using RAG/Vector DB.
    - **Why & Tradeoff:** It eliminates database latency and complexity for a small knowledge base, making it fast/cheap on serverless. The tradeoff is that if the portfolio grows huge, you'll hit token limits and have to build RAG.
- [ ] **Evaluation Evidence (1m):**
    - State the V2 Evaluation results: 10/10 tests passed.
    - Emphasize the hallucination guardrails (refusing to answer revenue/phone number requests).
- [ ] **Limitation Demo (1m):**
    - Switch back to the browser.
    - Ask: *"What is Krish's favorite movie?"*
    - Show the fallback response. Explain that the limitation is intentional: the agent cannot and should not invent facts outside its maintained knowledge base.
- [ ] **Closing (30s):** Summarize what you built, what was verified, and point to the live link.
- [ ] **Stop Recording.**

## 3. Post-Recording Actions
- [ ] Review the video to ensure it's under 5 minutes and no API keys or `.env` files are accidentally shown.
- [ ] Upload the video to YouTube (as Unlisted) or Loom.
- [ ] Copy the public video link.
- [ ] Update `work/fl09_showcase_post.md` and `README.md` with the live video link.
- [ ] Post the showcase thread link as required by the assignment.
