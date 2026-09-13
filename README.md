# FlyRank ML Internship

This repository contains my completed coursework, projects, and portfolio materials for the FlyRank Machine Learning Internship.

## About

This repository showcases a full arc of work from foundational ML and data tasks to applied agent automation workflows and frontend deployment. It demonstrates my ability to not only build and evaluate machine learning concepts but also to deploy practical AI engineering solutions in a modern web environment.

## Repository Structure

```text
/
├── README.md
├── Machine Learning/
│   ├── CAPSTONE.md
│   ├── data/
│   └── work/
│       ├── notebooks/
│       └── outputs/
├── AI Fluency/
│   ├── flyrank-ml-portfolio-case.md
│   └── FL-01_Workflow_Audit.docx
├── work/
│   ├── week04_three_roads.md
│   ├── fl04_automation_walkthrough.md
│   ├── fl04_automation_runs.md
│   ├── claude_project_instructions.md
│   ├── fl05_agent_mcp_explainer.md
│   ├── fl05_mcp_runs.md
│   └── fl05_evidence/
└── Flyrank Progress report.pdf
```

## Completed Work

| Assignment | Description | Evidence |
| :--- | :--- | :--- |
| **Baseline/Action Scoring** | Computed baseline models and evaluated logic signals for business cases. | [`Machine Learning/work/notebooks/w04_baseline_score.ipynb`](Machine Learning/work/notebooks/w04_baseline_score.ipynb) |
| **AI Fluency Prompt Iteration** | Detailed progression of prompt engineering and model interactions. | [`AI Fluency/flyrank-ml-portfolio-case.md`](AI Fluency/flyrank-ml-portfolio-case.md) |
| **Stack Selection** | Technical evaluation of three distinct web stacks for my portfolio. | [`work/week04_three_roads.md`](work/week04_three_roads.md) |
| **FL-04 Automation Workflow** | Design, prompt engineering, and runs of an AI-powered weekly industry brief workflow. | [`work/fl04_automation_walkthrough.md`](work/fl04_automation_walkthrough.md) |
| **FL-05 Agent & MCP** | Explainer on agents vs workflows, and execution of local MCP tasks. | [`work/fl05_agent_mcp_explainer.md`](work/fl05_agent_mcp_explainer.md) |
| **Capstone** | System architecture and ML documentation for the portfolio's Ask Krish AI. | [`Machine Learning/CAPSTONE.md`](Machine Learning/CAPSTONE.md) |

## FL-04 — Automation Workflow

This assignment documents a robust no-code AI workflow for synthesizing a weekly developer industry brief. The pipeline follows a strict four-step process:

1. **Gather:** Extract metadata and summaries from source URLs.
2. **Synthesize:** Identify thematic links and trace claims to sources.
3. **Draft:** Produce the weekly newsletter structure.
4. **Review/Format:** QA the output and clean up formatting.

The documentation includes five successful historical runs.
- [Walkthrough & Architecture](work/fl04_automation_walkthrough.md)
- [Workflow Runs](work/fl04_automation_runs.md)
- [Engine Instructions](work/claude_project_instructions.md)

## FL-05 — Agent Concepts and MCP

This module dives into the transition from static LLM workflows to active Agent architectures utilizing the Model Context Protocol (MCP).

It covers:
- The distinction between a Workflow (like FL-04) and an autonomous Agent.
- What MCP is and how tools, resources, and prompts are structured.
- Execution of three distinct, verifiable tasks against a local UI prototyping MCP server (`stitch`).
- A proposal to upgrade the FL-04 workflow into a true agent.

**Documentation:**
- [Concepts & Explainer](work/fl05_agent_mcp_explainer.md)
- [MCP Task Runs](work/fl05_mcp_runs.md)
- [Screenshots & Evidence Directory](work/fl05_evidence/)

## Portfolio

My live portfolio is built with Next.js and deployed on Vercel. 
**Live URL:** [https://portfolio-eta-pied-17.vercel.app/](https://portfolio-eta-pied-17.vercel.app/)

It includes professional case studies, project links, and an integrated AI assistant.

## Ask Krish AI

A central feature of the portfolio is "Ask Krish AI", a personal portfolio agent. It features:
- A strictly grounded knowledge base preventing hallucinations.
- Server-side API handling via Vercel Edge functions.
- Secure, hidden API keys.
- Intelligent fallback for unknown information.
- Markdown response rendering.

## Capstone

The capstone documentation details the architecture, design choices, and ML grounding strategy of the Ask Krish AI agent, providing a deep dive into the system's token strategy and failure-mode handling.

- [Capstone Document](Machine Learning/CAPSTONE.md)
- [Capstone Notebook](Machine Learning/work/notebooks/capstone_refresh_opportunity.ipynb)

## Reproducibility

The Jupyter notebooks in `Machine Learning/work/notebooks/` can be executed locally using standard scientific Python tooling (`pandas`, `scikit-learn`, `jupyter`). No exotic infrastructure is required. The automation workflows are thoroughly documented with their exact system prompts so they can be reproduced in any standard LLM chat interface.

## Security

This repository does not contain hardcoded API keys, tokens, passwords, or `.env` files. All live secrets (such as `GEMINI_API_KEY`) are managed strictly via external CI/CD environment variables in the Vercel dashboard.

## Author

**Krish Mistry**
- Portfolio: [https://portfolio-eta-pied-17.vercel.app/](https://portfolio-eta-pied-17.vercel.app/)
- GitHub: [https://github.com/KrishMistry18/Flyrank-ML](https://github.com/KrishMistry18/Flyrank-ML)
