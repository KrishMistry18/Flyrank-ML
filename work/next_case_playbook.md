# How to Add My Next Case Study

## Next Case
Ask Krish AI V2: Vector RAG Migration

## Three-Beat Shape

### 1. Problem
The V1 "Ask Krish AI" portfolio agent injects the entire structured JSON knowledge base directly into the prompt context window. As I add more case studies, projects, and detailed blog posts, this will hit token limits, increase API costs, and slow down response times.

### 2. What I Did
I migrated the agent's backend from full-context injection to a Retrieval-Augmented Generation (RAG) pipeline. I built an ingestion script to chunk my markdown case studies, generate embeddings, and store them in a lightweight vector database (e.g., ChromaDB/Pinecone). The serverless API now embeds the user's query, retrieves only the top-K relevant chunks, and feeds those to the LLM.

### 3. What Came of It
- Deployed V2 backend supporting infinitely scalable portfolio content.
- Performance measurement showing reduced token usage per query.
- Automated tests proving the agent still passes the 10-question hallucination suite.

## Case Study Workflow

1. Define the scaling problem (token limits).
2. Build the smallest useful version: a local script to chunk and embed `krish-knowledge.json`.
3. Test it with real edge cases (queries that require combining two chunks).
4. Record technical/design decisions (e.g., choice of embedding model and vector DB).
5. Capture evidence (token usage comparison, test pass rates).
6. Deploy/publish the updated Vercel function.
7. Write the case study using the Problem → What I Did → What Came of It format.
8. Add it to the portfolio.

## Reusable Build Context

To make building this next case a short conversation rather than a rebuild, I will reuse:
- **Claude Project/context:** My existing AI agent prompt containing my tone, voice (direct, honest), and the strict instruction to never invent metrics.
- **Identity Kit:** The existing vanilla CSS/JS chat UI on `portfolio-eta-pied-17.vercel.app` (no need to redesign the frontend).
- **Technical Conventions:** Keep it serverless on Vercel (`api/chat.js`), using standard Node.js without bloat.
- **Evidence Requirements:** Reuse the exact same `scratch/test_agent.py` script to verify that V2 doesn't regress on the hallucination guardrails.
