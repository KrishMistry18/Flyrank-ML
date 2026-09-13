# FlyRank ML Internship

This repository documents my comprehensive work throughout the FlyRank Machine Learning Internship. It showcases a full arc of work spanning from foundational machine learning data tasks to AI fluency exercises, portfolio development, workflow automation, MCP (Model Context Protocol) integration, and the design and implementation of a personal AI agent.

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
├── work/
│   ├── fl04_automation_walkthrough.md
│   ├── fl04_automation_runs.md
│   ├── claude_project_instructions.md
│   ├── fl05_agent_mcp_explainer.md
│   ├── fl05_mcp_runs.md
│   ├── fl05_explain_it_like_i_built_it.md
│   ├── fl06_personal_agent_spec.md
│   ├── fl07_build_log.md
│   ├── fl07_evidence/
│   │   └── fl07_raw_agent_run.mp4
│   └── week04_three_roads.md
└── AI Fluency/
    └── flyrank-ml-portfolio-case.md
```

- `Machine Learning/`: Contains all foundational ML coursework, Jupyter notebooks, datasets, model metrics, and capstone work.
- `work/`: Contains all AI Fluency assignments, system architectures, MCP runs, agent specifications, and evidence for automation workflows.
- `AI Fluency/`: Contains prompt engineering iterations and portfolio case study drafts.

## Machine Learning Work

This repository contains rigorous logic-based signal analysis and predictive modeling for business search ranking.

- **Week-4 Baseline:** [work/notebooks/w04_baseline_score.ipynb](Machine Learning/work/notebooks/w04_baseline_score.ipynb)
- **Week-5 Model:** [work/notebooks/w05_model.ipynb](Machine Learning/work/notebooks/w05_model.ipynb)

## ML-09 — Validation Audit

Audited the week 5 model against target leakage and data snooping. Group-split validation isolated clients correctly and revealed the true honest performance (51% Precision@100). The `impressions_prev_30d` feature was flagged as a strict target leak and safely removed.
- **Audit Notebook:** [Machine Learning/work/notebooks/w06_validation_audit.ipynb](Machine Learning/work/notebooks/w06_validation_audit.ipynb)
- **Metrics JSON:** [Machine Learning/work/outputs/w06_validation_audit_metrics.json](Machine Learning/work/outputs/w06_validation_audit_metrics.json)

## ML-10 — Content Action Playbook

Constructed an actionable, non-production Content Action Playbook based solely on the safely validated W06 group-split model (51% Precision@100). The playbook explicitly defines strict boundaries (no automated deletions or unreviewed publishes) and generates a ranked review queue for human SEO/Content teams.
- **Playbook Notebook:** [Machine Learning/work/notebooks/w07_action_playbook.ipynb](Machine Learning/work/notebooks/w07_action_playbook.ipynb)
- **Ranked Action Queue:** [Machine Learning/work/outputs/w07_ranked_action_queue.csv](Machine Learning/work/outputs/w07_ranked_action_queue.csv)
- **Distribution Figure:** [Machine Learning/work/figures/w07_priority_distribution.png](Machine Learning/work/figures/w07_priority_distribution.png)

**Verified Evaluation Results:**
- Week-4 baseline Precision@100: **54.55%**
- Random Forest Precision@100: **64.00%**
- Improvement: **+9.45 percentage points**

*(Note: This is an observed evaluation result on a strict holdout split, not a causal claim.)*

**Supporting Artifacts:**
- Metrics: [w05_model_metrics.json](Machine Learning/work/outputs/w05_model_metrics.json)
- Feature Importance: [w05_feature_importance.json](Machine Learning/work/outputs/w05_feature_importance.json)

## AI Fluency Work

| Assignment | Work | Evidence |
|---|---|---|
| Prompt Iteration | Detailed progression of prompt engineering and model interactions. | [`AI Fluency/flyrank-ml-portfolio-case.md`](AI Fluency/flyrank-ml-portfolio-case.md) |
| Stack Selection | Technical evaluation of three distinct web stacks for my portfolio. | [`work/week04_three_roads.md`](work/week04_three_roads.md) |
| FL-04 Automation | Design and execution of a robust no-code weekly industry brief workflow. | [`work/fl04_automation_walkthrough.md`](work/fl04_automation_walkthrough.md) |
| FL-05 MCP Concepts | Explainer on agents vs workflows, and execution of local MCP tasks. | [`work/fl05_agent_mcp_explainer.md`](work/fl05_agent_mcp_explainer.md) |
| FL-05 Explain It Like I Built It | Technical explanation of Ask Krish AI's backend knowledge injection mechanism. | [`work/fl05_explain_it_like_i_built_it.md`](work/fl05_explain_it_like_i_built_it.md) |
| FL-06 Personal Agent Design | Detailed design specification and architecture for the Ask Krish AI agent. | [`work/fl06_personal_agent_spec.md`](work/fl06_personal_agent_spec.md) |
| FL-07 Build the Agent | End-to-end testing, mock refinement, and build log for the Ask Krish AI agent. | [`work/fl07_build_log.md`](work/fl07_build_log.md) |

## FL-04 — Automation Workflow

This assignment documents a robust no-code AI workflow for synthesizing a weekly developer industry brief. The pipeline follows a strict four-step process: Gather, Synthesize, Draft, and Review/Format.

- [Walkthrough & Architecture](work/fl04_automation_walkthrough.md)
- [Workflow Runs](work/fl04_automation_runs.md)
- [Engine Instructions](work/claude_project_instructions.md)

## FL-05 — MCP

This module dives into the transition from static LLM workflows to active Agent architectures utilizing the Model Context Protocol (MCP). It covers the distinction between a Workflow and an Agent, MCP concepts, Stitch MCP connection details, and execution of verifiable tasks against a local MCP server.

- [Concepts & Explainer](work/fl05_agent_mcp_explainer.md)
- [MCP Task Runs](work/fl05_mcp_runs.md)
- Evidence: `work/fl05_evidence/`

## FL-06 — Personal Agent Design

Ask Krish AI was designed around one focused job:
"Answer questions from recruiters and hiring managers about Krish's projects, skills, experience, and technical background."

- [Personal Agent Spec](work/fl06_personal_agent_spec.md)

## FL-07 — Build the Agent

This assignment implements and refines the Ask Krish AI implementation based on the FL-06 design. It documents the serverless API architecture, the local portfolio knowledge source (Context Stuffing), end-to-end testing, guardrails, and mock fallback mechanisms. 

- [Build Log](work/fl07_build_log.md)
- Raw Run Evidence: [work/fl07_evidence/fl07_raw_agent_run.mp4](work/fl07_evidence/fl07_raw_agent_run.mp4)

## FL-07 — Mobile & Accessibility Audit

A comprehensive mobile-first audit was performed on the live portfolio to ensure responsiveness across devices (320px to 768px+). Key fixes include wrapping grid overflow in the hero section, fixing horizontal scroll issues on skill tags and footer links, and ensuring the Ask Krish AI interface fits cleanly within small mobile viewports without overflowing.

- **Mobile Fix Log:** [work/fl07_mobile_fix_log.md](work/fl07_mobile_fix_log.md)

## FL-07 — Break Your Own Site
Conducted a structured audit to break the deployed portfolio. Tested form validation, double submissions, meta tags (Findability), and speed. Discovered that the Ask Krish AI agent silently accepted empty strings and excessively long inputs. Fixed these vulnerabilities with UI feedback boundaries.
- **Live Portfolio:** [https://portfolio-eta-pied-17.vercel.app/](https://portfolio-eta-pied-17.vercel.app/)
- **Evidence Document:** [work/fl07_break_your_own_site.md](Machine Learning/work/fl07_break_your_own_site.md)
- **Known Limitations:** True Lighthouse audits are environment-dependent, and Google Search indexing is a gradual external process.

## FL-08 — Dynamic Portfolio Feature (Ask Krish AI)

The "Ask Krish AI" agent is the dynamic, interactive feature of my portfolio, designed to answer recruiter and hiring manager questions. It grounds all responses using a local JSON knowledge base containing my verified experience and skills. It features server-side API handling via Vercel Edge functions, secure hidden API keys, and intelligent fallback for unknown information.

This feature is fully deployed on the free tier and successfully tested end-to-end against the live API.

- **Live Portfolio:** [https://portfolio-eta-pied-17.vercel.app/](https://portfolio-eta-pied-17.vercel.app/)
- **Architecture Explainer:** [work/fl08_dynamic_feature.md](work/fl08_dynamic_feature.md)
- **Live End-to-End Test Record:** [work/fl08_evidence/fl08_test.md](work/fl08_evidence/fl08_test.md)

## Portfolio

**Live URL:** [https://portfolio-eta-pied-17.vercel.app/](https://portfolio-eta-pied-17.vercel.app/)

The portfolio demonstrates my ability to build modern, responsive web applications using Next.js and Vercel. It features professional case studies, project links, and the natively integrated "Ask Krish AI" agent.

## Capstone

The capstone documentation details the architecture, design choices, and ML grounding strategy of the Ask Krish AI agent, providing a deep dive into the system's token strategy and failure-mode handling.

- [Capstone Document](Machine Learning/CAPSTONE.md)
- [Capstone Notebook](Machine Learning/work/notebooks/capstone_refresh_opportunity.ipynb)

## Reproducibility

The Jupyter notebooks in `Machine Learning/work/notebooks/` can be executed locally using standard scientific Python tooling (`pandas`, `scikit-learn`, `jupyter`). No exotic infrastructure is required. The automation workflows and agent instructions are thoroughly documented in markdown files so they can be reproduced in standard AI interfaces.

## Security

This repository does not contain hardcoded API keys, tokens, passwords, or `.env` files. All live secrets (such as `GEMINI_API_KEY`) are managed strictly via external CI/CD environment variables and should never be committed.

## Author

# Krish Mistry

- Portfolio: [https://portfolio-eta-pied-17.vercel.app/](https://portfolio-eta-pied-17.vercel.app/)
- GitHub: [https://github.com/KrishMistry18/Flyrank-ML](https://github.com/KrishMistry18/Flyrank-ML)
