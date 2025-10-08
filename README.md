# 📘 Seam AI Prep

![Python](https://img.shields.io/badge/python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-lightgrey?logo=fastapi)
![Pydantic](https://img.shields.io/badge/Pydantic-2.3-blue?logo=pydantic)
![License](https://img.shields.io/badge/license-MIT-green)

A focused **13-day study plan** to strengthen modern AI engineering skills — from solid Python foundations to async FastAPI, LangGraph, and LLM integration.

---

## 🧭 Overview

**Goal:** Build end-to-end fluency as an AI Engineer — from typing and repo structure to async orchestration, Pydantic, FastAPI, and LangGraph agents.  
**Format:**  
⏱ **Core (3 hrs)** = must-do tasks  
➕ **Stretch (+1 hr)** = optional if energy allows  

---

## ⚙️ Recommended Setup (PowerShell)

Run your setup script to create the virtual environment and install dependencies:

```powershell
# Run the setup script
.\setup.ps1
```

---

## 📅 13-Day Seam AI Prep Plan

### **Week 1 → Developer Foundations + Async / FastAPI**

| **Day** | **Focus** | **Core (3 hrs)** | **Stretch (+1 hr)** |
|----------|------------|------------------|---------------------|
| **Day 1** | Python Typing & Codebase Reading | • Write small scripts w/ typing, run `mypy` (1h)<br>• Build class-based app w/ type hints (1h)<br>• Explore Typer repo → trace CLI entrypoint (1h) | Refactor to stricter typing |
| **Day 2** | Shell, venv, Codebase Structure | • Automate setup script (`venv`, deps, tests) (1h)<br>• Add `requirements.txt` + `pyproject.toml` (1h)<br>• Explore cookiecutter templates (1h) | Add a `Makefile` |
| **Day 3** | Git Workflows | • Branch → PR → merge workflow (1h)<br>• Practice rebasing & resolving conflicts (1h)<br>• Explore GitPython (1h) | Use `git bisect` on a bug |
| **Day 4** | VSCode & Debugging | • Set up `black`, `ruff`, `flake8`, `mypy` (1h)<br>• Debug project w/ breakpoints (1h)<br>• Explore black repo (1h) | Generate docs w/ `pdoc` |
| **Day 5** | Pydantic Models | • Define models (`User`, `Job`, `Resume`) (1h)<br>• Validate & test invalid data (1h)<br>• Explore Pydantic tests (1h) | Nested models + export schema |
| **Day 6** | FastAPI Basics | • Build `/hello` + `/predict` endpoints (1h)<br>• Add Pydantic models + tests (1h)<br>• Explore `fastapi-realworld-example-app` (1h) | Add logging middleware |
| **Day 7** | Async FastAPI | • Convert endpoints to async (1h)<br>• Simulate async DB/API calls (1h)<br>• Explore `httpx` async requests (1h) | Integration tests for concurrency |

---

### **Week 2 → LangGraph, LLM Handling, Ontologies**

| **Day** | **Focus** | **Core (3 hrs)** | **Stretch (+1 hr)** |
|----------|------------|------------------|---------------------|
| **Day 8** | LangGraph Basics | • Build simple agent (calculator + reformatter) (1h)<br>• Add branching logic w/ state (1h)<br>• Explore LangGraph examples (1h) | Error-handling node |
| **Day 9** | Async LangGraph + FastAPI | • Add async tool calls in LangGraph (1h)<br>• Wrap in FastAPI `/chat` (1h)<br>• Explore Starlette (1h) | Streaming response w/ async `yield` |
| **Day 10** | LLM Usage Mindset | • Experiment w/ OpenAI API: temp, few-shot vs zero-shot (1h)<br>• Build a prompt evaluator script (1h)<br>• Explore OpenAI Cookbook (1h) | Compare GPT outputs vs sentence-transformers similarity |
| **Day 11** | Feedback Loops | • Log model outputs as JSON (1h)<br>• Build CLI upvote/downvote (1h)<br>• Explore spaCy Streamlit (1h) | Store feedback in SQLite & query it |
| **Day 12** | Fine-tuning Encoders | • Fine-tune Sentence-Transformer on toy dataset (1h)<br>• Write typed training loop (1h)<br>• Explore Sentence-Transformers examples (1h) | Try LoRA on a small model |
| **Day 13** | Ontology & Embeddings | • Load ESCO / O*NET sample into SQLite (1h)<br>• Embed jobs & run similarity search (1h)<br>• Explore Haystack (1h) | Add FastAPI `/job-match` endpoint |

---

### Additional Study Tools

**Git Branching:** https://learngitbranching.js.org

**Security + Linux Commands:** https://overthewire.org/wargames/

**LangGraph:** https://academy.langchain.com/

---

## 🧩 Folder Structure (Tentative - Currently on Day 2)

```powershell
seam-ai-prep/
│
├── week1_foundations/
│   ├── day1_typing/
│   ├── day2_shell_venv_codebase/
│   ├── day3_gitworkflows/
│   └── ...
│
├── week2_langgraph_llm/
│   ├── day8_langgraph_basics/
│   ├── day9_async_integration/
│   └── ...
│
├── requirements.txt
├── pyproject.toml
├── setup.ps1
└── README.md
