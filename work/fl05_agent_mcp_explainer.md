# Agent Concepts and MCP Basics

## Workflow vs Agent
In the world of AI automation, the line between a "workflow" and an "agent" can seem blurry because both involve language models performing tasks. However, the distinction is fundamentally about **agency** and **control flow**. 

A **workflow** is a deterministic, predefined sequence of steps. The human designer maps out the exact route the data will take—first A, then B, then C. The AI acts as a processor at each node, transforming inputs into outputs based on strict prompts, but it has no power to alter the sequence or make decisions about what to do next. It blindly follows the pipeline.

An **agent**, on the other hand, is given a goal and a set of tools, and it dynamically determines its own path. Instead of following a hardcoded pipeline, an agent uses a "reasoning loop" (like ReAct—Reason, Act, Observe). It can decide which tool to call, evaluate the tool's output, and then decide if it needs to call another tool, retry, or finalize its answer. It adapts its process based on the intermediate results it encounters.

## My FL-04 Pipeline
My FL-04 pipeline (the Weekly AI + Developer Industry Brief) is strictly a **workflow**, not an agent. 

If we look at its implementation, the control flow is entirely hardcoded: `Gather → Synthesize → Draft → Review`. The model does not have the autonomy to decide, for instance, to skip the Synthesis step, or to go back and search the web for more articles if it finds the initial input lacking. The handoffs are highly predictable; the output of step 1 is rigidly passed to step 2 as input. Even if the AI realizes a source URL is broken, it cannot spontaneously decide to open a web browser tool to find a replacement—it simply outputs an error or hallucinates, forcing the human to fix it. Because the model strictly follows my designed process without autonomous routing, it is a classic workflow.

## What is MCP?
The Model Context Protocol (MCP) is an open standard that acts as a universal bridge between AI models and external data sources or tools. Historically, if you wanted an AI to read your local files, query your company's database, or trigger a Slack message, you had to write custom API integrations specifically for that AI (like ChatGPT plugins or custom LangChain tools). 

MCP solves this fragmentation. It standardizes the communication layer so that an AI application (like Claude or the Antigravity IDE) can connect to any MCP-compliant server. Think of it like USB-C for AI: instead of building a custom connector for every new data source, you just plug the AI into an MCP server, and it instantly understands how to interact with the underlying environment securely.

## The Three MCP Primitives
The protocol exposes the external world to the AI through three core primitives:

### Tools
Tools are actionable functions the AI can execute to perform operations or fetch dynamic data. Unlike passive reading, tools allow the AI to *do* things. 
*Example from my setup:* I connected to the `stitch` MCP server (a UI prototyping environment). The server exposes tools like `list_projects` and `get_project`. The AI can dynamically pass arguments (like a specific project ID) to these tools, execute them, and read the JSON response to understand what UI projects exist in my workspace.

### Resources
Resources are passive, static data that the AI can read to gain context, similar to mounting a read-only hard drive. Unlike tools, resources don't require the AI to pass complex arguments or execute functions; they are just data files, logs, or database snapshots exposed via unique URIs (like `file:///app/logs/error.log` or `postgres://schema/users`) that the AI can seamlessly ingest to understand the current state of the world.

### Prompts
MCP Prompts are reusable, pre-defined templates hosted by the server. Instead of the user having to type out a massive set of instructions every time, the MCP server can serve standardized prompts (e.g., "Code Review Prompt" or "UI Audit Prompt") that automatically inject the necessary context and rules before the AI begins its task.

## My MCP Demonstration
To prove this works, I connected my AI assistant to the local `stitch` MCP server available in my environment. This server manages UI design projects and screens. 

I executed three real tasks that ordinary chat alone could not do, because ordinary chat has no access to my local workspace's UI projects:
1. I asked the assistant to call the `list_projects` tool to discover what design systems I owned.
2. I asked it to use `list_screens` on a specific project ID ("PriceRadar") to fetch all the mobile UI screens associated with it.
3. I asked it to use `get_project` to inspect the raw design metadata (fonts, colors, and layout configurations) of that specific project.
The assistant successfully queried the local MCP server, parsed the massive JSON outputs, and summarized my private, local UI design tokens—something a disconnected LLM could never achieve.

## How I Would Upgrade FL-04 into an Agent
To turn my rigid FL-04 workflow into a true agent, I would replace the fixed pipeline with an autonomous reasoning loop equipped with MCP tools (e.g., `web_search`, `read_url`, `github_repo_reader`). 

Instead of always executing Gather → Synthesize → Draft → Review, the agent would receive a vague prompt like: *"Write this week's AI brief focusing on new models."*
The agent would then dynamically decide its actions:
1. It calls `web_search` to find news from the last 7 days.
2. It loops through `read_url` on the top 5 links. 
3. *Crucial agentic behavior:* If it reads an article and detects conflicting benchmark claims between OpenAI and Anthropic, it autonomously decides to halt drafting, calls `web_search` again specifically targeting benchmark validations, reads those, and *then* synthesizes the truth.
4. It calls a `draft_brief` tool, reviews its own output, and if it detects missing citations, loops back to its history to fix them before finally presenting the completed brief to me.

## What Still Needs Human Review
Even with a fully autonomous MCP agent, human oversight remains critical. The human must still verify the final output for **hallucinated tool data** (e.g., if the agent misread a JSON response), check the **tone** to ensure it aligns with the brand rather than sounding like generic AI copy, and confirm that the agent didn't autonomously pull data from an **unreliable or heavily biased source** during its unguided web searches.
