# Deployment Guide - LifeStepsAI Todo App (Phase I)

## Overview

This guide explains how to deploy and run the LifeStepsAI Todo Application Phase I (In-Memory Python Console App).

## Prerequisites

- **Python 3.12+** (Python 3.13+ recommended)
- **pip** or **UV** package manager
- **WSL 2** (for Windows users)

## Quick Start (5 Minutes)

### 1. Clone/Navigate to Project

```bash
cd /mnt/d/hackathon-robotic/todo-list
```

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python3 -m venv .venv

# Activate (Linux/macOS/WSL)
source .venv/bin/activate

# Activate (Windows PowerShell)
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
# Install pytest and dependencies
pip install pytest pytest-cov

# Set PYTHONPATH
export PYTHONPATH=$(pwd)/src
```

### 4. Run Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=src/todo_app --cov-report=term-missing
```

### 5. Run the Application

**Option A: Interactive Console UI**
```bash
python3 -m todo_app.ui
```

**Option B: Demo Script**
```bash
python3 demo.py
```

## Running Tests

### Basic Test Run

```bash
# Activate venv
source .venv/bin/activate

# Set PYTHONPATH
export PYTHONPATH=$(pwd)/src

# Run tests
pytest tests/ -v
```

### Test Coverage

```bash
# Run with coverage report
pytest tests/ --cov=src/todo_app --cov-report=term-missing --cov-report=html

# View HTML coverage report
# Linux/macOS:
open htmlcov/index.html

# Windows:
start htmlcov/index.html
```

### Expected Test Results

- **Total Tests**: 69
- **Status**: All passing ✅
- **Coverage**:
  - `models.py`: 88% (core logic)
  - `manager.py`: 98% (CRUD operations)
  - `ui.py`: 0% (optional, per constitution)

## Running the Application

### Method 1: Interactive Console UI

```bash
source .venv/bin/activate
export PYTHONPATH=$(pwd)/src
python3 -m todo_app.ui
```

**Features**:
- Add new tasks
- View all/pending/completed tasks
- Update task details
- Mark tasks complete/incomplete
- Delete tasks
- Interactive menu navigation

### Method 2: Demo Script

```bash
source .venv/bin/activate
python3 demo.py
```

**Shows**:
- Adding tasks
- Viewing tasks
- Marking complete
- Filtering by status
- Updating tasks
- Deleting tasks
- Toggling completion

### Method 3: Python Import

```python
# In Python REPL or script
import sys
sys.path.insert(0, '/mnt/d/hackathon-robotic/todo-list/src')

from todo_app import TodoManager

manager = TodoManager()
task = manager.add_task(title="Buy milk")
print(manager.list_tasks())
```

## Project Structure

```
todo-list/
├── src/todo_app/          # Application code
│   ├── models.py          # Task model
│   ├── manager.py         # TodoManager (CRUD)
│   ├── ui.py              # Console UI
│   └── exceptions.py      # Custom exceptions
├── tests/                 # Unit tests
│   ├── test_models.py
│   └── test_manager.py
├── specs/                 # Specifications
├── .venv/                 # Virtual environment
├── demo.py                # Demo script
├── README.md              # Documentation
├── CLAUDE.md              # Development guide
├── DEPLOYMENT.md          # This file
└── pyproject.toml         # Project configuration
```

## Troubleshooting

### Issue: Module not found

**Solution**: Set PYTHONPATH
```bash
export PYTHONPATH=$(pwd)/src
```

### Issue: Python version mismatch

**Solution**: Check Python version
```bash
python3 --version  # Should be 3.12+
```

### Issue: Tests failing

**Solution**: Ensure venv is activated and PYTHONPATH is set
```bash
source .venv/bin/activate
export PYTHONPATH=$(pwd)/src
pytest tests/ -v
```

### Issue: pip install fails

**Solution**: Upgrade pip
```bash
pip install --upgrade pip
pip install pytest pytest-cov
```

## Development Workflow

### 1. Make Changes

Edit code in `src/todo_app/`

### 2. Write Tests (TDD)

Add tests in `tests/`

### 3. Run Tests

```bash
pytest tests/ -v
```

### 4. Check Coverage

```bash
pytest tests/ --cov=src/todo_app --cov-report=term-missing
```

### 5. Run Application

```bash
python3 demo.py  # Quick demo
# OR
python3 -m todo_app.ui  # Full interactive UI
```

## Phase II Preparation

Phase II will add:
- Persistent storage (Neon PostgreSQL)
- Web interface (Next.js frontend)
- REST API (FastAPI backend)
- Multi-user support (Better Auth)

Current in-memory implementation will be replaced with database-backed storage.

## Important Notes

### Data Persistence
- **Phase I uses in-memory storage**
- All data is lost when application exits
- This is by design (see Constitution)
- Persistent storage comes in Phase II

### Testing
- Core logic (models, manager) has ~90%+ coverage
- UI tests are optional per project constitution
- Focus is on business logic testing

### Code Quality
- All code has type hints (PEP 484)
- All public functions have docstrings
- Follows clean code principles
- Passes all validation tests

## Support

For issues:
1. Check [README.md](README.md) for setup
2. Review [CLAUDE.md](CLAUDE.md) for development
3. See [Constitution](.specify/memory/constitution.md) for principles
4. Run demo script to verify installation

## Hackathon Submission

### Required for Submission:
- ✅ Public GitHub repository
- ✅ All source code (src/, tests/, specs/)
- ✅ README.md with setup instructions
- ✅ CLAUDE.md with development guide
- ✅ Constitution file
- ✅ Demo video (<90 seconds)
- ✅ Working application

### Demo Video Requirements:
- Maximum 90 seconds
- Show all 5 basic features:
  1. Add task
  2. View tasks
  3. Update task
  4. Mark complete
  5. Delete task
- Can use `demo.py` script for recording

### Verification Checklist:
- [ ] All 69 tests pass
- [ ] Coverage ≥90% for core logic
- [ ] Application runs without errors
- [ ] Interactive UI works
- [ ] Demo script shows all features
- [ ] README has complete setup instructions

---

**Version**: 1.0.0 | **Phase**: I | **Date**: December 7, 2025
