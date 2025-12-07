# LifeStepsAI | Todo Application - Phase I

[![Python](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![UV](https://img.shields.io/badge/uv-package%20manager-green.svg)](https://github.com/astral-sh/uv)
[![Test Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)](tests/)
[![Code Style](https://img.shields.io/badge/code%20style-ruff-black.svg)](https://github.com/astral-sh/ruff)

A clean, well-tested in-memory todo application built with **Spec-Driven Development (SDD)** and **Test-Driven Development (TDD)** principles.

## 🎯 Project Overview

This is **Phase I** of the Hackathon II "Evolution of Todo" project - an in-memory Python console application demonstrating:

- ✅ **Spec-Driven Development** - Every feature has a comprehensive specification
- ✅ **Test-Driven Development** - 100% test coverage for core logic
- ✅ **Clean Code** - Type hints, docstrings, and clear structure
- ✅ **SOLID Principles** - Single responsibility, proper abstraction
- ✅ **Professional Standards** - Following industry best practices

### Evolution Roadmap

- **Phase I** (Current): In-Memory Python Console App
- **Phase II**: Full-Stack Web App (Next.js + FastAPI + Neon DB)
- **Phase III**: AI-Powered Chatbot (OpenAI Agents SDK + MCP)
- **Phase IV**: Local Kubernetes Deployment (Minikube + Helm)
- **Phase V**: Cloud Deployment (DOKS/GKE/AKS + Kafka + Dapr)

## ✨ Features

### Basic Level Functionality (Phase I)

1. **Add Task** - Create new todo items with title and description
2. **View Tasks** - Display all, pending, or completed tasks
3. **Update Task** - Modify task title and description
4. **Mark Complete/Incomplete** - Toggle task completion status
5. **Delete Task** - Remove tasks from the list

### Key Characteristics

- 📝 **In-Memory Storage** - Fast, simple (data lost on exit in Phase I)
- 🎨 **Interactive Console UI** - User-friendly menu-driven interface
- 🔒 **Input Validation** - Robust error handling and validation
- 🧪 **100% Test Coverage** - Comprehensive unit tests for core logic
- 📚 **Type-Safe** - Full type hints (PEP 484)
- 📖 **Well-Documented** - Docstrings on all public functions

## 🚀 Quick Start

### Prerequisites

- **Python 3.13+** - [Download](https://www.python.org/downloads/)
- **UV** - Fast Python package manager

### Installation

#### 1. Install UV (if not already installed)

**Linux/macOS:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### 2. Clone the Repository

```bash
cd /mnt/d/hackathon-robotic/todo-list
```

#### 3. Create Virtual Environment & Install Dependencies

```bash
# Create virtual environment
uv venv

# Activate virtual environment
# On Linux/macOS:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate

# Install the package with dev dependencies
uv pip install -e ".[dev]"
```

### Running the Application

#### CLI Interface (Command-Line)

The application provides a modern CLI for quick task management:

```bash
# Add a new task
todo add "Buy groceries" -d "Milk, eggs, bread"

# List all tasks
todo list

# List pending tasks only
todo list --status pending

# List completed tasks only
todo list --status completed

# Get a specific task
todo get 1

# Update a task
todo update 1 -t "New title" -d "New description"

# Mark task as complete
todo complete 1

# Mark task as incomplete
todo incomplete 1

# Toggle task status
todo toggle 1

# Delete a task
todo delete 1

# Show help
todo --help
```

#### Interactive Console UI

```bash
# Method 1: Using the installed script
todo-interactive

# Method 2: Using Python module
python -m todo_app.ui

# Method 3: Direct execution
python src/todo_app/ui.py
```

#### Web UI (Beautiful modern interface)

```bash
# First install dependencies:
pip install -e .

# Then run the web server:
python -m todo_app.web

# Or if installed as package:
todo-web
```

### Web UI Features

The application now includes a beautiful, modern web interface with:

- 🎨 **Modern UI Design** - Clean, responsive interface using Bootstrap 5
- 📱 **Fully Responsive** - Works on mobile, tablet, and desktop
- 🔄 **Real-time Updates** - See changes instantly without page refresh
- 📊 **Task Statistics** - Visual counters for total, pending, and completed tasks
- 🔍 **Filtering** - View all, pending, or completed tasks
- ✨ **Animations** - Smooth transitions and visual feedback
- 🎯 **Intuitive Controls** - Easy to add, edit, complete, and delete tasks

Access the web UI at `http://localhost:5000` after starting the server.

## 📖 Usage Guide

### Main Menu

```
============================================================
  LifeStepsAI | Todo Application
============================================================

📋 Main Menu:
  1. Add new task
  2. View all tasks
  3. View pending tasks
  4. View completed tasks
  5. Update task
  6. Mark task as complete
  7. Mark task as incomplete
  8. Delete task
  9. Exit
```

### Example Workflow

1. **Add a task:**
   - Select option `1`
   - Enter title: "Buy groceries"
   - Enter description: "Milk, eggs, bread"

2. **View all tasks:**
   - Select option `2`
   - See all tasks with IDs and status

3. **Mark task complete:**
   - Select option `6`
   - Enter task ID: `1`

4. **View completed tasks:**
   - Select option `4`
   - See only completed tasks

## 🧪 Testing

### Run All Tests

```bash
# Run tests with coverage report
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_models.py

# Run specific test
pytest tests/test_models.py::TestTaskCreation::test_task_creation_with_required_fields_only
```

### Test Coverage

Current coverage: **100%** for core logic (`models.py`, `manager.py`)

```bash
# Generate HTML coverage report
pytest --cov=src/todo_app --cov-report=html

# Open coverage report (generated in htmlcov/)
# On Linux/macOS:
open htmlcov/index.html

# On Windows:
start htmlcov/index.html
```

### Code Quality Checks

```bash
# Type checking with mypy
mypy src/todo_app

# Linting with ruff
ruff check src/ tests/

# Format code with ruff
ruff format src/ tests/
```

## 📁 Project Structure

```
todo-list/
├── .claude/                    # Claude Code agents, skills, commands
│   ├── agents/                 # Reusable agents (documentation, security, qa)
│   ├── skills/                 # Reusable skills (action_sequencer, e2e_test_runner)
│   ├── commands/               # Spec-Kit commands (sp.*)
│   └── settings.local.json     # Claude Code settings
├── .specify/
│   └── memory/
│       └── constitution.md     # 📜 Project Constitution (principles & standards)
├── specs/
│   ├── overview.md            # Project overview
│   └── features/              # 📋 Feature Specifications
│       ├── task-model.md      # Task data model spec
│       ├── add-task.md        # Add task feature spec
│       ├── delete-task.md     # Delete task feature spec
│       ├── update-task.md     # Update task feature spec
│       ├── view-tasks.md      # View tasks feature spec
│       └── mark-complete.md   # Mark complete feature spec
├── src/
│   └── todo_app/              # 💻 Application Source Code
│       ├── __init__.py        # Package initialization
│       ├── exceptions.py      # Custom exceptions
│       ├── models.py          # Task model
│       ├── manager.py         # TodoManager (CRUD operations)
│       └── ui.py              # Console UI
├── tests/                     # 🧪 Unit Tests
│   ├── __init__.py
│   ├── test_models.py         # Task model tests (100% coverage)
│   └── test_manager.py        # TodoManager tests (100% coverage)
├── history/
│   └── prompts/               # Prompt History Records
├── pyproject.toml             # Python project configuration (UV)
├── CLAUDE.md                  # Claude Code instructions
├── README.md                  # This file
└── .gitignore                 # Git ignore patterns
```

## 🏗️ Architecture

### Data Model

```python
@dataclass
class Task:
    id: int                                    # Unique identifier
    title: str                                 # 1-200 characters
    description: str = ""                      # 0-1000 characters
    completed: bool = False                    # Completion status
    created_at: datetime = field(default_factory=datetime.now)
```

### Core Components

1. **Task Model** (`models.py`)
   - Represents a single todo task
   - Validates input data
   - Auto-trims whitespace from title
   - Supports Unicode characters

2. **TodoManager** (`manager.py`)
   - Manages in-memory task storage
   - Provides CRUD operations
   - Filters tasks by status
   - Auto-generates unique IDs

3. **Console UI** (`ui.py`)
   - Interactive menu-driven interface
   - User-friendly error messages
   - Clear visual feedback

### Design Decisions

- **In-Memory Storage**: Simple and fast for Phase I (persistence comes in Phase II)
- **Dataclasses**: Clean, type-safe data structures
- **Custom Exceptions**: Clear, actionable error messages
- **Separate Concerns**: UI, business logic, and data model are decoupled

## 📜 Specifications

All features are built following comprehensive specifications in `/specs/features/`:

- **Spec-Driven Development**: Features are spec'd before implementation
- **Clear Requirements**: User stories, acceptance criteria, edge cases
- **Test Cases**: Pre-defined test cases ensure quality
- **Examples**: Code examples demonstrate expected behavior

See [specs/overview.md](specs/overview.md) for full project specifications.

## 🧑‍💻 Development

### Development Workflow (TDD)

1. **Read Specification** - Understand requirements from `/specs/features/`
2. **Write Tests (RED)** - Write failing tests first
3. **Implement Feature (GREEN)** - Write minimal code to pass tests
4. **Refactor (REFACTOR)** - Improve code quality while keeping tests green
5. **Verify Coverage** - Ensure 100% coverage for core logic

### Code Standards

- **Type Hints**: All public functions have type hints (PEP 484)
- **Docstrings**: All public functions have comprehensive docstrings
- **Clean Code**: Meaningful names, single responsibility, DRY
- **Error Handling**: Explicit exceptions with clear messages
- **Testing**: 100% coverage for core business logic

### Constitution

All development follows principles defined in `.specify/memory/constitution.md`:

1. **Spec-Driven & Test-Driven Development** (NON-NEGOTIABLE)
2. **Clean Code with Type Hints & Docstrings** (NON-NEGOTIABLE)
3. **100% Unit Test Coverage for Core Logic** (NON-NEGOTIABLE)
4. **In-Memory Storage Only** (Phase I Constraint)
5. **Explicit Exceptions & Input Validation** (NON-NEGOTIABLE)

## 🤝 Contributing

This is a hackathon project following strict Spec-Driven Development. To contribute:

1. Read `.specify/memory/constitution.md` - Understand core principles
2. Review `/specs/` - All features must have specifications
3. Follow TDD - Tests before implementation
4. Maintain 100% coverage - For core logic
5. Add type hints & docstrings - Code quality standards

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Hackathon II** - "The Evolution of Todo" project
- **Panaversity, PIAIC, GIAIC** - For organizing this learning opportunity
- **Claude Code** - AI-assisted development with Spec-Kit Plus
- **UV** - Fast, reliable Python package management

## 📞 Support

For questions or issues:

- Review [CLAUDE.md](CLAUDE.md) for development guidelines
- Check [specs/](specs/) for feature specifications
- See [Constitution](.specify/memory/constitution.md) for project principles

## 🚀 Next Steps

After Phase I completion:

- **Phase II**: Transform to web app (Next.js + FastAPI + Neon DB)
- **Phase III**: Add AI chatbot (OpenAI Agents SDK + MCP)
- **Phase IV**: Deploy locally (Minikube + Helm + kubectl-ai)
- **Phase V**: Deploy to cloud (DOKS/GKE/AKS + Kafka + Dapr)

---

**Built with** ❤️ **using Spec-Driven Development and Test-Driven Development**

**Version**: 1.0.0 | **Phase**: I (In-Memory Console App) | **Date**: December 7, 2025
