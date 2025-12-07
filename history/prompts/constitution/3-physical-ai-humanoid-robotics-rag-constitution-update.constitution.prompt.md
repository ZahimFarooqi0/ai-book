---
id: 3
stage: constitution
title: "Physical-AI-Humanoid-Robotics-RAG-Constitution-Update"
date_iso: "2025-12-07"
surface: "agent"
model: "Qwen"
feature: "none"
branch: "main"
user: "user"
command: "/sp.constitution Project Physical AI & Humanoid Robotics – AI-Driven Book with Integrated RAG Chatbot"
labels: ["documentation", "constitution", "robotics", "ai", "rag", "chatbot"]
links: {spec: null, ticket: null, adr: null, pr: null}
outcome: "updated"
evaluation: "complete"
files_yaml:
  - ".specify/memory/constitution.md"
tests_yaml: []
---

# Prompt History Record: Physical AI & Humanoid Robotics RAG Constitution Update

## PROMPT_TEXT

---
description: Create or update the project constitution from interactive or provided principle inputs, ensuring all dependent templates stay in sync
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

You are updating the project constitution at `.specify/memory/constitution.md`. This file is a TEMPLATE containing placeholder tokens in square brackets (e.g. `[PROJECT_NAME]`, `[PRINCIPLE_1_NAME]`). Your job is to (a) collect/derive concrete values, (b) fill the template precisely, and (c) propagate any amendments across dependent artifacts.

Follow this execution flow:

1. Load the existing constitution template at `.specify/memory/constitution.md`.
   - Identify every placeholder token of the form `[ALL_CAPS_IDENTIFIER]`.
   **IMPORTANT**: The user might require less or more principles than the ones used in the template. If a number is specified, respect that - follow the general template. You will update the doc accordingly.

2. Collect/derive values for placeholders:
   - If user input (conversation) supplies a value, use it.
   - Otherwise infer from existing repo context (README, docs, prior constitution versions if embedded).
   - For governance dates: `RATIFICATION_DATE` is the original adoption date (if unknown ask or mark TODO), `LAST_AMENDED_DATE` is today if changes are made, otherwise keep previous.
   - `CONSTITUTION_VERSION` must increment according to semantic versioning rules:
     - MAJOR: Backward incompatible governance/principle removals or redefinitions.
     - MINOR: New principle/section added or materially expanded guidance.
     - PATCH: Clarifications, wording, typo fixes, non-semantic refinements.
   - If version bump type ambiguous, propose reasoning before finalizing.

3. Draft the updated constitution content:
   - Replace every placeholder with concrete text (no bracketed tokens left except intentionally retained template slots that the project has chosen not to define yet—explicitly justify any left).
   - Preserve heading hierarchy and comments can be removed once replaced unless they still add clarifying guidance.
   - Ensure each Principle section: succinct name line, paragraph (or bullet list) capturing non‑negotiable rules, explicit rationale if not obvious.
   - Ensure Governance section lists amendment procedure, versioning policy, and compliance review expectations.

4. Consistency propagation checklist (convert prior checklist into active validations):
   - Read `.specify/templates/plan-template.md` and ensure any "Constitution Check" or rules align with updated principles.
   - Read `.specify/templates/spec-template.md` for scope/requirements alignment—update if constitution adds/removes mandatory sections or constraints.
   - Read `.specify/templates/tasks-template.md` and ensure task categorization reflects new or removed principle-driven task types (e.g., observability, versioning, testing discipline).
   - Read each command file in `.specify/templates/commands/*.md` (including this one) to verify no outdated references (agent-specific names like CLAUDE only) remain when generic guidance is required.
   - Read any runtime guidance docs (e.g., `README.md`, `docs/quickstart.md`, or agent-specific guidance files if present). Update references to principles changed.

5. Produce a Sync Impact Report (prepend as an HTML comment at top of the constitution file after update):
   - Version change: old → new
   - List of modified principles (old title → new title if renamed)
   - Added sections
   - Removed sections
   - Templates requiring updates (✅ updated / ⚠ pending) with file paths
   - Follow-up TODOs if any placeholders intentionally deferred.

6. Validation before final output:
   - No remaining unexplained bracket tokens.
   - Version line matches report.
   - Dates ISO format YYYY-MM-DD.
   - Principles are declarative, testable, and free of vague language ("should" → replace with MUST/SHOULD rationale where appropriate).

7. Write the completed constitution back to `.specify/memory/constitution.md` (overwrite).

8. Output a final summary to the user with:
   - New version and bump rationale.
   - Any files flagged for manual follow-up.
   - Suggested commit message (e.g., `docs: amend constitution to vX.Y.Z (principle additions + governance update)`).

Formatting & Style Requirements:

- Use Markdown headings exactly as in the template (do not demote/promote levels).
- Wrap long rationale lines to keep readability (<100 chars ideally) but do not hard enforce with awkward breaks.
- Keep a single blank line between sections.
- Avoid trailing whitespace.

If the user supplies partial updates (e.g., only one principle revision), still perform validation and version decision steps.

If critical info missing (e.g., ratification date truly unknown), insert `TODO(<FIELD_NAME>): explanation` and include in the Sync Impact Report under deferred items.

Do not create a new template; always operate on the existing `.specify/memory/constitution.md` file.

---

/sp.constitution

Project: Physical AI & Humanoid Robotics – AI-Driven Book with Integrated RAG Chatbot

Core principles:
- Accuracy: All AI, robotics, and simulation content must be correct and validated with credible sources.
- Practicality: Hands-on instructions for ROS 2, Gazebo, Unity, NVIDIA Isaac, and humanoid robotics must be reproducible.
- Clarity: Writing must be accessible to beginners-to-intermediate students in AI/robotics.
- Integration: RAG chatbot must reliably reference content selected by the user and provide accurate, context-aware answers.
- Embodiment: Focus on bridging digital AI with physical humanoid robots, including simulations and real-world applications.

Key standards:
- All code examples (Python, ROS 2, LLM integrations) must run correctly in simulation or real hardware.
- References to tools and libraries must link to official documentation.
- Chatbot responses must be traceable to book content only.
- Writing clarity: Flesch-Kincaid grade 10-12.
- Formatting: Docusaurus book with modular chapters; deployable on GitHub Pages.

Constraints:
- Book structure: 4 main modules + Capstone Project.
- Module content: ROS 2 (Nodes, Topics, URDF), Gazebo & Unity (simulation), NVIDIA Isaac (perception & VSLAM), Vision-Language-Action (LLM-robot interface).
- Chatbot integration: FastAPI backend, Neon Serverless Postgres, Qdrant Cloud Free Tier.
- Deployment: Docusaurus + GitHub Pages.
- File types: Markdown + embedded code snippets + illustrations.
- Word count: 15,000–25,000 words total.

Success criteria:
- All robotic and AI examples work as described.
- Chatbot correctly answers questions based on selected text only.
- Book is fully deployed and navigable on GitHub Pages.
- Zero technical errors during simulation or chatbot interaction.
- Students can follow instructions to simulate and control humanoid robots in ROS 2 + NVIDIA Isaac + Unity.
- Peer review / expert verification of robotics and AI content.

## RESPONSE_TEXT

I have successfully updated the constitution document for the "Physical AI & Humanoid Robotics – AI-Driven Book with Integrated RAG Chatbot" project. This was a major update (version 1.1.0 → 2.0.0) that incorporated all the specified requirements:

Key changes made:
1. Updated Core Principles to include Technical Accuracy and Modularity & Integration principles
2. Added requirements for AI/robotics/RAG focus with specific tech stack
3. Modified Success Criteria with specific metrics related to RAG chatbot and deployment
4. Updated Constraints with specific tech stack and module content requirements
5. Expanded Scope section to include specific tools and technologies (ROS 2, Gazebo, Unity, NVIDIA Isaac, etc.)
6. Added RAG chatbot and word count objectives to the Objectives section
7. Updated Content Structure to include integration requirements
8. Added Integration Standards to the Quality Standards section

The constitution now comprehensively covers all aspects of the project including the 4 main modules + Capstone Project structure, the RAG chatbot integration using FastAPI/Neon/Qdrant, and the deployment on GitHub Pages with Docusaurus. All code examples are required to run correctly in simulation or real hardware, and all content must maintain Flesch-Kincaid grade 10-12 readability level.