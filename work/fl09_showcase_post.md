# Showcase Thread Post: Ask Krish AI

**Project:** Ask Krish AI – A Context-Aware Personal Portfolio Assistant
**Live Demo:** [https://portfolio-eta-pied-17.vercel.app/](https://portfolio-eta-pied-17.vercel.app/)
**Repository & README:** [https://github.com/KrishMistry18/Flyrank-ML](https://github.com/KrishMistry18/Flyrank-ML)

**DEMO VIDEO:** [ADD AFTER RECORDING]

## What I Built
I built "Ask Krish AI", a native, serverless AI assistant embedded directly into my engineering portfolio. It helps recruiters and hiring managers get instant, factual answers about my skills, projects, and FlyRank ML internship experience without digging through static pages.

## Design Decision
For V1, I decided to use a structured JSON knowledge base injected directly into the Gemini 2.5 Flash system prompt, rather than building a complex RAG pipeline. This massively reduced latency and simplified the architecture for serverless execution. The tradeoff is hitting token limits if the portfolio grows exponentially in the future.

## Key Limitation
The agent is explicitly constrained to a verified knowledge base. It is designed *not* to hallucinate answers. If you ask it about my favorite movie or exact project revenues, it will intentionally fall back and provide my contact email rather than inventing facts.
