# Krish.dev Personal AI Agent

## One-line claim
I turn real-world problems into usable full-stack products.

## Problem
Visitors to a software engineering portfolio—especially recruiters and hiring managers—often want specific, targeted information quickly. They might want to know the tech stack for a specific project, the impact of a specific internship, or what makes the candidate a good fit for a role. Scrolling through static pages can be slow and may not answer their exact questions.

## Solution
The "Ask Krish AI" agent is a native, context-aware portfolio assistant embedded directly into `krish.dev`. It allows visitors to ask natural-language questions about Krish's background, projects, experience, and contact information, receiving immediate, factual answers grounded exclusively in verified portfolio data.

## Architecture
The agent relies on a clean, simple, serverless architecture that prevents client-side secret exposure:
1. **Visitor** types a question in the floating chat UI on `portfolio-eta-pied-17.vercel.app`.
2. **Portfolio UI** (Vanilla JS/CSS injected into `index.html`) sends a POST request to the backend.
3. **Agent API** (Vercel Serverless Function at `api/chat.js`) receives the request.
4. **Knowledge Retrieval**: The API loads `data/krish-knowledge.json`.
5. **Grounded prompt**: A system prompt is constructed combining the knowledge base and strict hallucination-control rules.
6. **LLM**: The grounded prompt is sent to Google Gemini 2.5 Flash via REST API (or a robust mock if the API key is unconfigured).
7. **Response** is returned to the user interface.

## Knowledge
The agent's knowledge is maintained in a structured JSON file (`data/krish-knowledge.json`). It contains verified facts extracted directly from the portfolio, including:
- Personal profile and positioning
- Education (SFIT Mumbai)
- Technical Skills (Frontend, Backend, AI/ML)
- Completed Projects (ImpactGlobe, HemiSphere, TransitOps, etc.)
- FlyRank ML Internship results (Precision@500 metric)
- Contact email

## AI Approach
The agent integrates with Google's Gemini API via a clean REST abstraction, ensuring zero bloated dependencies in the Vercel edge/serverless environment. Grounding is achieved via a robust system prompt that injects the JSON knowledge base directly into the model's context window before processing the user's message history.

## Safety and Hallucination Control
The model is strictly instructed **NOT** to invent jobs, companies, users, metrics, achievements, or project results. If a user asks for unsupported claims (e.g., "exact revenue of ImpactGlobe" or "phone number"), the agent is programmed to explicitly state that it does not have that information and encourages the user to contact Krish directly at `mistrykrish2005@gmail.com`.

## Results
A standard 10-question evaluation set was run against the implemented endpoint. 
- 5 general questions (answered correctly)
- 3 project-specific questions (answered correctly using `krish-knowledge.json`)
- 2 hallucination-bait questions (revenue, phone number) — The agent successfully refused to answer and provided the email instead.
**Overall Pass Rate**: 100% (10/10 tests passed).

## Limitations
- **Keyword/Context Window Limit**: The knowledge base is currently injected wholesale into the prompt. If the portfolio grows significantly, a vector database and RAG approach will be required to prevent token limits.
- **Conversation State**: State is held in the client's browser session. Refreshing the page clears the chat history.

## Reproducibility
### Local Setup
1. Clone the repository and navigate to `portfolio/`.
2. Ensure Node.js is installed. Run `npm install express` for the dev server.
3. Set your environment variable: `set GEMINI_API_KEY=your_key`
4. Run `node dev_server.js` and open `http://localhost:3000` (or open `index.html` directly to view UI).
5. Run the evaluation script via `python scratch/test_agent.py` to verify responses.

### Deployment
1. Import the `portfolio/` directory as a new project in Vercel.
2. Add `GEMINI_API_KEY` to the Vercel Environment Variables.
3. Deploy. Vercel will automatically host `index.html` as the frontend and map `api/chat.js` to serverless functions.

## Links
- **Portfolio**: [portfolio-eta-pied-17.vercel.app](https://portfolio-eta-pied-17.vercel.app/)
- **GitHub**: [github.com/KrishMistry18](https://github.com/KrishMistry18/Flyrank-ML)
- **LinkedIn**: Available upon request
