# AI Fluency Assignment: Prompt Ladder

This document contains the actual executed prompt ladder for the **README / documentation generation for GitHub repos** task identified in the FL-01 Workflow Audit. 

All 6 versions were run against the appropriate AI model available in this workspace (Antigravity/Gemini). 

---

## The 6-Version Prompt Ladder

### Version 0: Naive Baseline
**Added Technique**: None

**Prompt**:
```text
Write a README for my FlyRank ML project.
```

**Actual Output**:
```markdown
# FlyRank ML Project

Welcome to the FlyRank ML project! This repository contains the machine learning pipeline for FlyRank.

## Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation
1. Clone the repository.
2. Run `pip install -r requirements.txt`.

### Usage
Run the main script to start the pipeline.

## License
MIT
```

**Analysis**:
- **What changed**: (Baseline, initial state).
- **What actually improved in the output**: (Baseline). It generated standard GitHub boilerplate.
- **What still failed**: It is completely generic and hallucinated prerequisites (Python 3.8) and generic usage instructions ("Run the main script"). It provides no real value to an intern cloning the specific FlyRank repository.
- **Why the next technique was selected**: The output sounds like a robot. We need to assign a professional role so the model adopts a developer-centric tone.

---

### Version 1: Role Assignment
**Added Technique**: Role Assignment

**Prompt**:
```text
Act as a Senior Developer Advocate. Write a README for my FlyRank ML project.
```

**Actual Output**:
```markdown
# 🚀 FlyRank ML

Welcome to the official repository for **FlyRank ML**! As a developer advocate, I'm thrilled to introduce you to our state-of-the-art machine learning pipeline designed to elevate your search ranking analytics. 

## 🌟 What is FlyRank ML?
FlyRank ML is a robust, scalable machine learning framework built to process, analyze, and predict search performance metrics. Whether you're a data scientist or an ML engineer, this repo provides the tools you need to get started quickly.

## 🛠️ Quick Start

### Prerequisites
Ensure you have Python 3.9+ installed.

### Setup
```bash
git clone https://github.com/flyrank/flyrank-ml.git
cd flyrank-ml
pip install -r requirements.txt
```

### Running the Pipeline
```bash
python main.py
```

## 🤝 Contributing
We love community contributions! Please check out our `CONTRIBUTING.md` guidelines.

Happy coding! Let's build something amazing together. 🚀
```

**Analysis**:
- **What changed**: Added the "Senior Developer Advocate" persona.
- **What actually improved in the output**: The tone shifted dramatically. It became enthusiastic, included emojis, and structured the introduction to sound like a public open-source project pitch.
- **What still failed**: While the tone changed, it is completely misaligned with our internal use-case. It added unnecessary sections like "Contributing" and hallucinated fake repo URLs (`github.com/flyrank/flyrank-ml.git`).
- **Why the next technique was selected**: The model doesn't understand the internal context or audience. We need to give it the specific motivation and target audience.

---

### Version 2: Context and Motivation
**Added Technique**: Context and Motivation

**Prompt**:
```text
Act as a Senior Developer Advocate. Write a README for my FlyRank ML project. We need this so junior interns can quickly clone the repository and run the entire data pipeline without having to ask me any clarifying questions about dependencies or commands.
```

**Actual Output**:
```markdown
# FlyRank ML: Intern Quickstart Guide 🚀

Welcome to the FlyRank ML team! This repository contains our core machine learning data pipeline. 

This README is designed specifically for you. By following these steps, you will be able to clone the repository, install all necessary dependencies, and run the complete data pipeline entirely on your own. 

## 🛠️ System Requirements
Before you begin, ensure you have the following installed on your machine:
- **Python 3.10+** (Verify with `python --version`)
- **Git**

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-org/flyrank-ml.git
   cd flyrank-ml
   ```

2. **Create a virtual environment (Highly Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Running the Data Pipeline

Once your environment is set up, you can execute the full data pipeline with a single command:

```bash
python run_pipeline.py
```

This script will automatically ingest the raw data, process the features, and output the final model metrics into the `/outputs` directory.

If you encounter any errors during these steps, please double-check your Python version and ensure your virtual environment is activated before reaching out! Welcome aboard!
```

**Analysis**:
- **What changed**: Added the target audience (junior interns) and the success metric (running without clarifying questions).
- **What actually improved in the output**: The text became highly targeted ("Intern Quickstart Guide"). It proactively anticipated intern issues by adding virtual environment setup instructions and troubleshooting tips.
- **What still failed**: It is still hallucinating the exact commands (`python run_pipeline.py` and `your-org/flyrank-ml.git`). An intern would immediately fail and have to ask clarifying questions.
- **Why the next technique was selected**: We must anchor the model to reality by showing it the exact, correct commands to run.

---

### Version 3: Few-Shot Examples
**Added Technique**: Few-Shot Examples

**Prompt**:
```text
Act as a Senior Developer Advocate. Write a README for my FlyRank ML project. We need this so junior interns can quickly clone the repository and run the entire data pipeline without having to ask me any clarifying questions about dependencies or commands. 

Here is an example of what a good Installation section looks like for a similar project:
` ` `
## Installation
1. Clone the repo: `git clone https://github.com/KrishMistry18/flyrank-ml-internship-starter`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the pipeline: `python scripts/run_all.py`
` ` `
```

**Actual Output**:
```markdown
# FlyRank ML Pipeline

Welcome to the FlyRank ML project! This repository contains the data pipeline for our machine learning internship track. This guide will walk you through exactly how to set up your environment and run the code end-to-end.

## Overview
This project processes search console data and trains a model to identify content refresh opportunities.

## Installation
1. Clone the repo: `git clone https://github.com/KrishMistry18/flyrank-ml-internship-starter`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the pipeline: `python scripts/run_all.py`

## Next Steps
After running the pipeline, check the `outputs/` directory for your generated reports and models. 

If you followed the 3 installation steps above, the entire pipeline should run seamlessly without any further configuration!
```

**Analysis**:
- **What changed**: Added a concrete example block of the exact commands needed.
- **What actually improved in the output**: The hallucinations stopped! The installation block is exactly correct and runnable.
- **What still failed**: The model still included conversational filler ("Welcome to the FlyRank ML project!") and "Next Steps", which makes the document longer than necessary. 
- **Why the next technique was selected**: We need to force strict formatting constraints to strip out the fluff and control the exact sections generated.

---

### Version 4: Output Structure
**Added Technique**: Output Structure

**Prompt**:
```text
Act as a Senior Developer Advocate. Write a README for my FlyRank ML project. We need this so junior interns can quickly clone the repository and run the entire data pipeline without having to ask me any clarifying questions about dependencies or commands. 

Here is an example of what a good Installation section looks like for a similar project:
` ` `
## Installation
1. Clone the repo: `git clone https://github.com/KrishMistry18/flyrank-ml-internship-starter`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the pipeline: `python scripts/run_all.py`
` ` `

Output the README in markdown. You must strictly use the following headers and no others: `# FlyRank ML`, `## Overview`, `## Installation`, `## Usage`, and `## Data Safe Handling`. Do not include any introductory or concluding conversational text.
```

**Actual Output**:
```markdown
# FlyRank ML

## Overview
This repository contains the core machine learning data pipeline for the FlyRank project. It is designed to process search console data and train predictive models. The setup process is standardized so interns can quickly bootstrap their environment and execute the end-to-end pipeline.

## Installation
1. Clone the repo: `git clone https://github.com/KrishMistry18/flyrank-ml-internship-starter`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the pipeline: `python scripts/run_all.py`

## Usage
To use the pipeline, ensure your virtual environment is active. The `run_all.py` script executes data preparation, baseline scoring, and model training sequentially. All final artifacts and evaluation metrics will be written automatically to the `/outputs` directory.

## Data Safe Handling
All data used in this pipeline must be anonymized. Do not commit raw CSV files containing client data to version control. Ensure that any exported datasets or model weights are kept local or stored in the approved secure data warehouse.
```

**Analysis**:
- **What changed**: Added explicit constraints limiting the output strictly to 5 specific headers and banning conversational text.
- **What actually improved in the output**: The document is now perfectly concise. It dropped the intro/outro fluff and formatted exactly to the required headers.
- **What still failed**: The `Data Safe Handling` section is slightly generic. The model generated generic data rules but didn't deeply analyze the context of what FlyRank ML's specific data risks are.
- **Why the next technique was selected**: We need the model to pause and internally evaluate the components and safety rules *before* drafting the final text to improve the depth of reasoning.

---

### Version 5: Step Decomposition
**Added Technique**: Step Decomposition

**Prompt**:
```text
Act as a Senior Developer Advocate. Write a README for my FlyRank ML project. We need this so junior interns can quickly clone the repository and run the entire data pipeline without having to ask me any clarifying questions about dependencies or commands. 

Here is an example of what a good Installation section looks like for a similar project:
` ` `
## Installation
1. Clone the repo: `git clone https://github.com/KrishMistry18/flyrank-ml-internship-starter`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the pipeline: `python scripts/run_all.py`
` ` `

Output the README in markdown. You must strictly use the following headers and no others: `# FlyRank ML`, `## Overview`, `## Installation`, `## Usage`, and `## Data Safe Handling`. Do not include any introductory or concluding conversational text.

Before drafting, identify the required components, check the provided information for missing or unsafe assumptions, then produce the final README.
```

**Actual Output**:
```markdown
# FlyRank ML

## Overview
This repository contains the FlyRank machine learning pipeline, designed to prioritize content refresh opportunities using anonymized Google Search Console data. The codebase provides an end-to-end workflow from data preparation to model evaluation. This documentation ensures that all interns can immediately clone the project, install the necessary dependencies, and successfully execute the pipeline independently.

## Installation
1. Clone the repo: `git clone https://github.com/KrishMistry18/flyrank-ml-internship-starter`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the pipeline: `python scripts/run_all.py`

## Usage
Executing the installation commands above will automatically run the full pipeline. The `run_all.py` script coordinates data loading, feature engineering, baseline evaluation, and model training. Upon successful execution, all generated reports, visualizations, and ranked queues will be saved directly to the `outputs/` directory. No manual configuration of paths or variables is required for the default run.

## Data Safe Handling
The FlyRank pipeline utilizes anonymized search data. You must strictly adhere to the following safety protocols:
- Never commit raw `.csv` or `.parquet` data files to version control.
- Ensure that features derived directly from the target label (such as future trends) are strictly dropped to prevent data leakage during training.
- Do not upload local datasets to unauthorized external platforms. 
- All results generated in the `outputs/` folder are for internal analysis and should be treated confidentially.
```

**Analysis**:
- **What changed**: Added an instruction to perform internal step-by-step reasoning (without exposing a private `<thinking>` block) prior to writing the output.
- **What actually improved in the output**: The text in `Overview` and `Data Safe Handling` became significantly more intelligent and context-aware. It specifically mentioned "leakage", "target labels", and "Google Search Console data"—topics it derived from reasoning deeply about the provided context rather than just rushing to generate generic text.
- **What still failed**: Nothing. This is a highly robust, production-ready prompt that fulfills the core task perfectly.

---

## Cross-Model Comparison

**Final Prompt for Comparison**: *(Used the exact Version 5 prompt above)*

### Claude Output
```markdown
# FlyRank ML

## Overview
FlyRank ML is a [ONE-SENTENCE DESCRIPTION OF WHAT THE MODEL/PIPELINE DOES, e.g., "a ranking model that scores flight search results by predicted booking likelihood"]. This repository contains the data pipeline, training code, and evaluation scripts used by the FlyRank ML team. It is intended to be cloned and run end-to-end with minimal setup.

## Installation
1. Clone the repo:
   `git clone <YOUR-ACTUAL-REPO-URL>`
2. Create and activate a virtual environment (recommended):
   `python -m venv venv && source venv/bin/activate` (macOS/Linux) or `venv\Scripts\activate` (Windows)
3. Install dependencies:
   `pip install -r requirements.txt`
4. Set required environment variables (see `.env.example` if present — do not commit real values):
   `cp .env.example .env`
5. Run the full pipeline:
   `python <PATH-TO-YOUR-RUN-ALL-SCRIPT>`

> Note: Confirm the exact script path and any required environment variables with your team lead before running — placeholders above must be replaced with real values.

## Usage
- Run the full pipeline: `python <PATH-TO-YOUR-RUN-ALL-SCRIPT>`
- Run an individual stage (e.g., data ingestion, feature engineering, training, evaluation): `python <STAGE-SCRIPT-PATH> --config <CONFIG-FILE>`
- Outputs (models, metrics, logs) are written to `<OUTPUT-DIRECTORY>`.
- Check `<CONFIG-DIRECTORY-OR-FILE>` for adjustable parameters before re-running.

## Data Safe Handling
- Never commit raw data files, credentials, API keys, or `.env` files to version control. Confirm `.gitignore` covers all data and secrets paths before your first commit.
- If the pipeline processes any personally identifiable information (PII) or customer data, confirm with your team lead what handling, storage, and retention rules apply *before* running it on real data.
- Use only sanctioned sample or synthetic datasets for local development unless explicitly authorized to use production data.
- Do not share datasets, model artifacts, or logs outside approved internal channels.
- Report any accidental exposure of sensitive data to your team lead immediately.
```

### ChatGPT Output
```markdown
FlyRank ML
Overview

FlyRank ML is a machine learning project for training ranking models and generating predictions.

The pipeline uses public datasets as its data source and is designed to provide a reproducible workflow for preparing data, training ranking models, and producing predictions.

Installation

Clone the repository:

git clone https://github.com/KrishMistry18/flyrank-ml-internship-starter
cd flyrank-ml-internship-starter

Install the Python dependencies:

pip install -r requirements.txt

Run the complete pipeline:

python scripts/run_all.py
Usage

Run the complete ML pipeline with:

python scripts/run_all.py

The pipeline trains the ranking models and produces model predictions.

For development, make changes to the relevant pipeline or model code and rerun the pipeline to verify the results.

Data Safe Handling
This project uses public datasets.
Do not add private, confidential, or personally identifiable information (PII) to the repository.
Do not commit API keys, passwords, access tokens, credentials, or other secrets.
Keep downloaded datasets and generated artifacts out of version control when they are not intended to be committed.
Before publishing new datasets, verify that their licensing and usage terms permit redistribution.
If sensitive data is accidentally introduced, remove it from the repository and rotate any exposed credentials immediately.
```

### Comparison

**Claude:**
- **Tone**: Highly professional, cautious, and template-driven. It reads more like an enterprise policy document than an intern quickstart guide.
- **Accuracy**: It completely ignored the few-shot examples provided in the prompt and replaced them with generic placeholders like `<YOUR-ACTUAL-REPO-URL>` and `<PATH-TO-YOUR-RUN-ALL-SCRIPT>`, explicitly failing the few-shot constraint.
- **Structure**: Adhered perfectly to the requested markdown headers (`# FlyRank ML`, `## Overview`, etc.) and used blockquotes and lists effectively to structure the content.
- **Completeness**: Extensive safety rules, but functionally incomplete because an intern cannot actually copy-paste the installation commands.
- **Failure points**: Complete failure to use the provided few-shot data. It assumed it didn't have the real data and inserted `[ONE-SENTENCE DESCRIPTION...]` placeholders instead of drafting a plausible description.
- **Unsupported assumptions/hallucinations**: Assumed the pipeline requires `.env` variables and `<CONFIG-FILE>` modifications, which were never stated in the prompt and could confuse an intern.
- **Best aspect**: The Data Safe Handling section is extremely thorough and accurate to real-world enterprise standards (PII handling, retention rules, `.gitignore` checks).

**ChatGPT:**
- **Tone**: Direct, robotic, and slightly simplistic. It reads more like a mechanical summary than a Senior Developer Advocate's guide.
- **Accuracy**: High for the specific task instructions. It correctly utilized the few-shot example for the installation commands (`git clone`, `pip install`, `python scripts/run_all.py`), making it immediately actionable.
- **Structure**: It failed the markdown constraint entirely! It did not output proper markdown headers (it output plain text `FlyRank ML` instead of `# FlyRank ML`), stripping the requested formatting.
- **Completeness**: Covered all sections, but the "Data Safe Handling" is completely hallucinated in premise.
- **Failure points**: Failed the markdown formatting negative constraint entirely.
- **Unsupported assumptions/hallucinations**: Hallucinated a massive assumption by stating "This project uses public datasets" and discussing "redistribution" terms. This is a fatal compliance hallucination for an intern data pipeline.
- **Best aspect**: It strictly followed the few-shot example, producing immediately runnable installation commands without replacing them with placeholders.

**Winner for this task:**
**Claude**

**Reason:**
While ChatGPT followed the few-shot installation commands perfectly, it completely hallucinated a highly dangerous assumption in the `Data Safe Handling` section by declaring "This project uses public datasets." This is a fatal hallucination for an intern handling private Search Console data. Claude failed the few-shot constraint by using `<YOUR-ACTUAL-REPO-URL>` placeholders, but its placeholders and safety policies (`Never commit raw data`, `PII`) are vastly safer and require only trivial find-and-replace to fix. A slightly annoying template is far better than a README that confidently tells interns their private data is "public."

---

## Final Reusable Template

This generalized prompt can be used by anyone, on any repository, without relying on your personal FlyRank context. It incorporates all techniques (Role, Context, Few-Shot, Output Structure, Step Decomposition).

```text
Act as a Senior Developer Advocate. Write a README for my [PROJECT_NAME] project. We need this so [TARGET_AUDIENCE] can quickly clone the repository and run the entire pipeline without having to ask me any clarifying questions about dependencies or commands. 

Here is an example of what a good Installation section looks like for this project:
` ` `
## Installation
[INSERT_FEW_SHOT_COMMAND_1]
[INSERT_FEW_SHOT_COMMAND_2]
` ` `

Output the README in markdown. You must strictly use the following headers and no others: `# [PROJECT_NAME]`, `## Overview`, `## Installation`, `## Usage`, and `## [CUSTOM_SECTION]`. Do not include any introductory or concluding conversational text.

Before drafting, identify the required components, check the provided information for missing or unsafe assumptions, then produce the final README.
```
