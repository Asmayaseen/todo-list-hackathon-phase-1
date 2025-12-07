# LifeStepsAI | Todo App - Project Overview

## Purpose

LifeStepsAI is an in-memory Python console application for managing daily tasks (todos). This Phase I implementation focuses on core task management functionality following strict Spec-Driven Development (SDD) and Test-Driven Development (TDD) principles.

## Project Vision

This todo application will evolve through 5 phases:
- **Phase I** (Current): In-Memory Python Console App - Basic task management
- **Phase II**: Full-Stack Web Application with Next.js + FastAPI + Neon DB
- **Phase III**: AI-Powered Todo Chatbot using OpenAI Agents SDK + MCP
- **Phase IV**: Local Kubernetes Deployment with Minikube + Helm
- **Phase V**: Advanced Cloud Deployment on DigitalOcean/GCP/Azure + Kafka + Dapr

## Current Phase: Phase I

### Objectives
Build a command-line todo application that stores tasks in-memory and demonstrates:
1. Spec-Driven Development methodology
2. Test-Driven Development (TDD) with 100% core coverage
3. Clean code with type hints and docstrings
4. Proper Python project structure

### Technology Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.13+ |
| Package Manager | UV |
| Testing | pytest |
| Development Process | Claude Code + Spec-Kit Plus |
| Code Quality | Type hints (PEP 484), Docstrings |

### Features (Phase I)

#### Basic Level Functionality
All 5 Basic Level features MUST be implemented:

1. **Add Task** - Create new todo items with title and description
2. **Delete Task** - Remove tasks from the list by ID
3. **Update Task** - Modify existing task details
4. **View Task List** - Display all tasks with status indicators
5. **Mark as Complete** - Toggle task completion status

### Core Principles (from Constitution)

1. **Spec-Driven Development**: Every feature has a specification before implementation
2. **Test-Driven Development**: Tests written before code (Red-Green-Refactor)
3. **Clean Code**: Type hints, docstrings, meaningful names, SRP
4. **100% Test Coverage**: All core logic fully tested
5. **In-Memory Storage**: No persistent storage in Phase I

### Success Criteria

✅ All 5 Basic Level features working
✅ 100% unit test coverage for core logic
✅ All code has type hints and docstrings
✅ Follows spec-driven development
✅ Clean, well-structured Python project
✅ Comprehensive README with setup instructions

### Project Structure

```
todo-list/
├── .claude/                    # Claude Code agents, skills, commands
│   ├── agents/                 # Reusable agents (documentation, security, qa)
│   ├── skills/                 # Reusable skills (action_sequencer, e2e_test_runner)
│   └── commands/               # Spec-Kit commands (sp.*)
├── .specify/
│   └── memory/
│       └── constitution.md     # Project principles and standards
├── specs/
│   ├── overview.md            # This file
│   └── features/              # Feature specifications
│       ├── task-model.md      # Task data model spec
│       ├── add-task.md        # Add task feature spec
│       ├── delete-task.md     # Delete task feature spec
│       ├── update-task.md     # Update task feature spec
│       ├── view-tasks.md      # View tasks feature spec
│       └── mark-complete.md   # Mark complete feature spec
├── src/
│   └── todo_app/              # Application source code
│       ├── __init__.py
│       ├── models.py          # Task model
│       ├── manager.py         # TodoManager (CRUD operations)
│       ├── ui.py              # Console UI
│       └── exceptions.py      # Custom exceptions
├── tests/                     # Unit tests (mirrors src structure)
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_manager.py
│   └── test_ui.py
├── history/
│   └── prompts/               # Prompt History Records
│       ├── constitution/      # Constitution-related prompts
│       └── general/           # General prompts
├── pyproject.toml             # UV project configuration
├── README.md                  # Setup and usage documentation
└── CLAUDE.md                  # Claude Code instructions
```

### Development Workflow

1. **Specification Phase**: Write feature spec in `/specs/features/`
2. **Planning Phase**: Review spec, identify tasks and tests
3. **Red Phase**: Write failing tests first
4. **Green Phase**: Implement minimal code to pass tests
5. **Refactor Phase**: Improve code quality
6. **Review Phase**: Verify constitution compliance

### Constraints

#### Phase I Specific Constraints
- ✅ In-memory storage ONLY (no files, no databases)
- ✅ Python 3.13+ required
- ✅ Console interface (no web UI in Phase I)
- ✅ Single-user application

#### Non-Goals for Phase I
- ❌ Persistent storage (comes in Phase II)
- ❌ Multi-user support (comes in Phase II)
- ❌ Web interface (comes in Phase II)
- ❌ AI integration (comes in Phase III)
- ❌ Cloud deployment (comes in Phase IV-V)

### Quality Standards

| Standard | Requirement |
|----------|-------------|
| Test Coverage | 100% for core logic |
| Code Quality | Type hints + Docstrings on all public functions |
| Error Handling | Explicit exceptions with clear messages |
| Performance | Instant response (in-memory operations) |
| Documentation | Comprehensive README + CLAUDE.md |

### Deliverables

1. GitHub repository with:
   - Constitution file (`.specify/memory/constitution.md`)
   - Specs folder with all specifications
   - `/src` folder with Python source code
   - `/tests` folder with comprehensive unit tests
   - `README.md` with setup instructions
   - `CLAUDE.md` with Claude Code instructions

2. Working console application demonstrating:
   - Adding tasks with title and description
   - Listing all tasks with status indicators
   - Updating task details
   - Deleting tasks by ID
   - Marking tasks as complete/incomplete

3. Test suite with 100% coverage for core logic

### Timeline (Hackathon Phase I)

- **Due Date**: December 7, 2025
- **Points**: 100 points
- **Submission**: Public GitHub repo + demo video (<90 seconds)

### Next Steps

After Phase I completion, the application will evolve:
- **Phase II**: Add web interface (Next.js + FastAPI + Neon DB)
- **Phase III**: Add AI chatbot (OpenAI Agents SDK + MCP)
- **Phase IV**: Deploy locally (Minikube + Helm + kubectl-ai)
- **Phase V**: Deploy to cloud (DOKS/GKE/AKS + Kafka + Dapr)

---

**Version**: 1.0.0 | **Created**: 2025-12-07 | **Phase**: I (In-Memory Console App)
