# Next Piece of Work

## Project
Ask Krish AI V2: Vector RAG Migration

## Why This Is Next
During the FL-09 demo, I explicitly documented the limitation of the current V1 architecture: it injects the entire portfolio knowledge base directly into the Gemini prompt. As I add more detailed ML case studies (like the Content Decay work), I will hit token limits and cost constraints. Moving to a Retrieval-Augmented Generation (RAG) system is the most logical backend engineering task because it solves a concrete, self-identified bottleneck while demonstrating advanced full-stack AI engineering.

## First Milestone
Build a local Python script to chunk the `krish-knowledge.json` and markdown files, generate embeddings, and query them locally.

## Success Evidence
1. A Python script (`scratch/build_vector_db.py`) that successfully splits the text and generates vectors.
2. A local SQLite or JSON-based vector store containing the embeddings.
3. A successful test query that retrieves only the exact chunk needed (e.g., retrieving the ML-11 precision score without loading the ImpactGlobe data).
