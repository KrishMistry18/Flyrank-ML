# 3–5 Minute Live Demo: Ask Krish AI

## 0:00–0:30 — What it is
"Hi, I'm Krish, and this is 'Ask Krish AI'. It's a context-aware personal assistant embedded directly into my engineering portfolio. I built it specifically for recruiters and hiring managers who visit my site and want targeted answers—like 'what is your tech stack?' or 'what impact did you have at FlyRank?'—without having to scroll through static pages."

## 0:30–1:30 — Normal live run
*(Action: Open the deployed portfolio at https://portfolio-eta-pied-17.vercel.app/)*
*(Action: Click the chat bubble to open Ask Krish AI)*
"Let's see it in action. I'll ask it: 'What AI projects has Krish built?'"
*(Action: Type the question and hit send. Wait for response.)*
"As you can see, it responds instantly with facts about ImpactGlobe and FlyRank. Technically, the frontend sends this query to a Vercel serverless function (`/api/chat.js`), which combines the question with a strict system prompt and my local knowledge base JSON, and streams it to Google's Gemini 2.5 Flash model via REST API."

## 1:30–2:30 — Architecture/design decision
"A key engineering decision I made was **using a structured JSON knowledge base instead of a separate RAG pipeline or putting facts directly in prompts.**"
*(Action: Show the code for `data/krish-knowledge.json` or `api/chat.js` if possible)*
"**Why?** Because my portfolio content is currently small enough to fit within the Gemini context window. 
**The Tradeoff:** This massively simplified the architecture. It eliminated the need for a vector database and reduced latency, ensuring the agent is fast and cheap to run on serverless. The tradeoff is that if my portfolio grows to thousands of pages, I will eventually hit token limits and need to migrate to RAG. But for V1, this was the right engineering choice."

## 2:30–3:30 — Evaluation
"I didn't just deploy this; I tested it. We ran a V2 evaluation suite consisting of 10 targeted questions. 
- 5 general questions passed.
- 3 project-specific questions passed.
- Most importantly, 2 'hallucination-bait' questions passed. When asked for my exact revenue or my phone number, the agent successfully refused to answer and provided my public email address instead.
Overall, the agent achieved a 100% pass rate on these core guardrails."

## 3:30–4:30 — Limitation
"But I want to be honest about its limitations. The agent can only reliably answer information represented in its maintained knowledge base; it should not invent information outside that source."
*(Action: Type: 'What is Krish's favorite movie?' into the chat)*
"If I ask it something entirely unrelated to my professional profile, watch what happens."
*(Action: Show the fallback response)*
"It explicitly states it doesn't have that information. This is intentional. I explicitly instructed the model not to hallucinate or invent facts to fill the void, ensuring recruiters only get verified data."

## 4:30–5:00 — Closing
"To summarize, I built a serverless AI assistant that reliably answers professional questions using a structured knowledge base, verified it against hallucination tests, and maintained architectural simplicity. While it's limited by its current static context window, it perfectly solves the immediate problem of helping recruiters find information faster. 

You can try it live at `portfolio-eta-pied-17.vercel.app`!"
