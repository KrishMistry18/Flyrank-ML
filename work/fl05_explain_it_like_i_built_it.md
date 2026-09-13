# Explain It Like I Built It

## What I Chose

The backend knowledge injection for the "Ask Krish AI" portfolio agent.

## How It Works

When a visitor types a question into the chat on my portfolio, the frontend sends those messages to my serverless API route (`/api/chat`). 

Before I send the conversation to the AI model, my server reads a local JSON file (`data/krish-knowledge.json`) that contains all my verified portfolio details, skills, and contact info. I stringify this entire JSON object and inject it directly into a strict system prompt. I then send this combined prompt and the user's conversation to the Gemini 2.5 Flash model using a standard REST API fetch call. The model generates a response based solely on my provided JSON data, and my API sends the text back to the frontend to display.

## Why I Built It This Way

I chose to inject the entire JSON knowledge base directly into the prompt (a technique sometimes called "context stuffing") instead of building a complex RAG (Retrieval-Augmented Generation) system with a vector database. 

The reason I did this was simplicity and speed. My portfolio data is small enough to easily fit inside the model's context window. Building a RAG pipeline would have been over-engineering, adding unnecessary latency, infrastructure, and complexity without improving the actual answers. I also chose to make a raw REST API call using `fetch` rather than importing a heavy third-party SDK to keep the function lightweight and fast.

## What Happens When Something Goes Wrong

I implemented two main fallbacks:
1. **Missing Knowledge:** If a user asks for something not in the JSON (like my home address or exact salary), the system prompt has a strict rule forcing the model to reply exactly: *"I don't have that information in Krish's public profile."* This prevents the model from hallucinating or guessing.
2. **Missing API Keys:** If the environment variable containing my API key is missing (which happens during local testing without secrets), the API detects this and falls back to a hardcoded JavaScript mock. The mock uses simple keyword matching to return pre-written responses, ensuring the chat UI doesn't just crash.

## What I Learned

I learned that you don't always need complex architectures like vector databases to build effective AI features. For small, bounded datasets, giving the LLM raw structured data in the system prompt alongside strict behavioral rules is often the most reliable and performant approach. I also learned how to build robust graceful degradation so the app continues to function even if the external AI service isn't configured.

## Plain-English Explanation

"When a user asks my portfolio AI a question, my backend grabs a local file containing all my resume and project data, bundles it up with a set of strict rules, and hands it to the AI model in one go. Because my data is relatively small, I didn't need to build a complex search database—I just give the AI the exact facts and tell it never to guess. If the AI key is missing or the system fails, it gracefully falls back to a hardcoded mock so the user still gets an answer."
