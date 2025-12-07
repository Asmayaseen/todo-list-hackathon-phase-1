# Claude Code Instructions - LifeStepsAI Todo App

## Project Overview

This is the **LifeStepsAI Todo Application** - an in-memory Python console application for Phase I of the Hackathon II. The project demonstrates Spec-Driven Development (SDD) and Test-Driven Development (TDD) principles.

## Core Development Principles

### 1. Constitution is Law
All development **MUST** comply with `.specify/memory/constitution.md`. The constitution defines:
- Spec-Driven Development (SDD) - Required
- Test-Driven Development (TDD) - Required
- Clean Code with Type Hints & Docstrings - Required
- 100% Test Coverage for Core Logic - Required
- In-Memory Storage Only (Phase I) - Required

### 2. Spec-Driven Development Workflow

**Every feature MUST have a spec before implementation:**

1. **Read the Spec**: Always read the relevant spec from `/specs/features/` before coding
2. **Understand Requirements**: Review user stories, acceptance criteria, and edge cases
3. **Plan Tests**: Identify all test cases from the spec
4. **Implement with TDD**: Write tests first, then implementation

**Spec Files Available:**
- `/specs/overview.md` - Project overview and structure
- `/specs/features/task-model.md` - Task data model specification
- `/specs/features/add-task.md` - Add task feature specification
- `/specs/features/delete-task.md` - Delete task feature specification
- `/specs/features/update-task.md` - Update task feature specification
- `/specs/features/view-tasks.md` - View tasks feature specification
- `/specs/features/mark-complete.md` - Mark complete feature specification

### 3. Test-Driven Development (TDD) Process

**MANDATORY Red-Green-Refactor Cycle:**

#### RED Phase: Write Failing Test First
```python
# Example: tests/test_models.py
def test_task_creation_with_required_fields_only():
    """Test creating a task with only required fields."""
    task = Task(id=1, title="Buy milk")

    assert task.id == 1
    assert task.title == "Buy milk"
    assert task.description == ""
    assert task.completed is False
```

Run the test - **it MUST fail** (code doesn't exist yet):
```bash
pytest tests/test_models.py::test_task_creation_with_required_fields_only
```

#### GREEN Phase: Write Minimal Code to Pass
```python
# Example: src/todo_app/models.py
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Task:
    id: int
    title: str
    description: str = ""
    completed: bool = False
    created_at: datetime = field(default_factory=datetime.now)
```

Run the test - **it MUST pass**:
```bash
pytest tests/test_models.py::test_task_creation_with_required_fields_only
```

#### REFACTOR Phase: Improve Code Quality
- Add type hints
- Add docstrings
- Improve naming
- Extract duplicated code
- **Tests MUST still pass after refactoring**

### 4. Code Quality Standards

#### Type Hints (REQUIRED)
```python
# ✅ GOOD - All types explicitly declared
def add_task(self, title: str, description: str = "") -> Task:
    """Add a new task to the list."""
    pass

# ❌ BAD - No type hints
def add_task(self, title, description=""):
    pass
```

#### Docstrings (REQUIRED for public functions)
```python
# ✅ GOOD - Comprehensive docstring
def delete_task(self, task_id: int) -> None:
    """
    Delete a task by ID.

    Args:
        task_id: The ID of the task to delete

    Raises:
        TaskNotFoundException: If task_id doesn't exist
    """
    pass

# ❌ BAD - No docstring
def delete_task(self, task_id: int) -> None:
    pass
```

#### Clean Code Principles
- **Meaningful names**: `add_task()` not `add()`
- **Single Responsibility**: One function = one purpose
- **DRY**: Don't Repeat Yourself
- **Small functions**: Ideally < 20 lines
- **No magic numbers**: Use named constants

## Project Structure

```
todo-list/
├── .claude/                    # Reusable agents, skills, commands
│   ├── agents/                 # documentation_agent, security_enforcer, qa_script_generator
│   ├── skills/                 # action_sequencer, e2e_test_runner
│   └── commands/               # sp.* commands for spec-kit
├── .specify/
│   └── memory/
│       └── constitution.md     # ⭐ PROJECT CONSTITUTION (READ THIS FIRST)
├── specs/
│   ├── overview.md            # Project overview
│   └── features/              # ⭐ FEATURE SPECIFICATIONS (READ BEFORE IMPLEMENTING)
│       ├── task-model.md
│       ├── add-task.md
│       ├── delete-task.md
│       ├── update-task.md
│       ├── view-tasks.md
│       └── mark-complete.md
├── src/
│   └── todo_app/              # Application source code
│       ├── __init__.py
│       ├── exceptions.py      # Custom exceptions (InvalidTaskDataError, TaskNotFoundException)
│       ├── models.py          # Task model (TO IMPLEMENT)
│       ├── manager.py         # TodoManager - CRUD operations (TO IMPLEMENT)
│       └── ui.py              # Console UI (TO IMPLEMENT)
├── tests/                     # ⭐ WRITE TESTS FIRST (TDD)
│   ├── __init__.py
│   ├── test_models.py         # Task model tests
│   ├── test_manager.py        # TodoManager tests
│   └── test_ui.py             # UI tests (optional, focus on core logic)
├── history/
│   └── prompts/               # Prompt History Records
├── pyproject.toml             # Python project configuration (UV)
├── README.md                  # Setup and usage documentation
├── CLAUDE.md                  # ⭐ THIS FILE
└── .gitignore                 # Git ignore patterns
```

## Implementation Order (Following TDD)

### Phase 1: Task Model
1. Read `specs/features/task-model.md`
2. Write tests in `tests/test_models.py` (RED)
3. Implement `src/todo_app/models.py` (GREEN)
4. Refactor for quality (REFACTOR)

### Phase 2: TodoManager - Add Task
1. Read `specs/features/add-task.md`
2. Write tests in `tests/test_manager.py` (RED)
3. Implement `add_task()` in `src/todo_app/manager.py` (GREEN)
4. Refactor (REFACTOR)

### Phase 3: TodoManager - View Tasks
1. Read `specs/features/view-tasks.md`
2. Write tests (RED)
3. Implement `list_tasks()`, `get_task()` (GREEN)
4. Refactor (REFACTOR)

### Phase 4: TodoManager - Delete Task
1. Read `specs/features/delete-task.md`
2. Write tests (RED)
3. Implement `delete_task()` (GREEN)
4. Refactor (REFACTOR)

### Phase 5: TodoManager - Update Task
1. Read `specs/features/update-task.md`
2. Write tests (RED)
3. Implement `update_task()` (GREEN)
4. Refactor (REFACTOR)

### Phase 6: TodoManager - Mark Complete
1. Read `specs/features/mark-complete.md`
2. Write tests (RED)
3. Implement `mark_complete()`, `mark_incomplete()`, `toggle_complete()` (GREEN)
4. Refactor (REFACTOR)

### Phase 7: Console UI
1. Implement console interface in `src/todo_app/ui.py`
2. Interactive menu with all operations
3. User-friendly error messages

## Commands & Workflows

### Setup Development Environment
```bash
# Install UV (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment and install dependencies
cd /mnt/d/hackathon-robotic/todo-list
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dev dependencies
uv pip install -e ".[dev]"
```

### Running Tests
```bash
# Run all tests with coverage
pytest

# Run specific test file
pytest tests/test_models.py

# Run specific test
pytest tests/test_models.py::test_task_creation_with_required_fields_only

# Run tests with verbose output
pytest -v

# Run tests and stop at first failure
pytest -x

# Run tests and show print statements
pytest -s
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

### Running the Application
```bash
# Run the console app
python -m todo_app.ui

# Or using the installed script
todo
```

## Testing Standards

### Test Coverage Requirements
- **100% coverage for core logic** (models.py, manager.py)
- UI tests optional (focus on core business logic)

### Test Structure
```python
def test_descriptive_name_of_what_is_tested():
    """
    Clear docstring explaining the test purpose.

    This test verifies that [specific behavior] works correctly
    when [specific conditions].
    """
    # Arrange - Set up test data
    manager = TodoManager()
    task = manager.add_task(title="Test")

    # Act - Perform the operation
    manager.delete_task(task_id=task.id)

    # Assert - Verify the result
    assert len(manager.list_tasks()) == 0
```

### Test Naming Convention
- `test_<action>_<condition>_<expected_result>()`
- Examples:
  - `test_add_task_with_valid_title_succeeds()`
  - `test_delete_nonexistent_task_raises_error()`
  - `test_task_with_empty_title_raises_error()`

## Error Handling Standards

### Custom Exceptions (Already Defined)
```python
from todo_app.exceptions import InvalidTaskDataError, TaskNotFoundException

# Use InvalidTaskDataError for validation errors
if not title.strip():
    raise InvalidTaskDataError("Title cannot be empty")

# Use TaskNotFoundException for missing tasks
if task_id not in self.tasks:
    raise TaskNotFoundException(f"Task with ID {task_id} not found")
```

### User-Facing Error Messages
- ✅ GOOD: "Title cannot be empty"
- ❌ BAD: "Error"

## Important Constraints

### Phase I Constraints (MUST FOLLOW)
- ✅ **In-memory storage ONLY** - No files, no databases
- ✅ **Python 3.13+** - Use modern Python features
- ✅ **Console interface** - No web UI in Phase I
- ✅ **Single-user** - No multi-user support in Phase I

### What NOT to Implement (Phase I)
- ❌ Persistent storage (comes in Phase II)
- ❌ Web interface (comes in Phase II)
- ❌ Multi-user support (comes in Phase II)
- ❌ AI integration (comes in Phase III)
- ❌ Priorities, tags, due dates (comes in Phase V)
- ❌ Recurring tasks, reminders (comes in Phase V)

## Reusable Components

### Available Agents (in .claude/agents/)
- `documentation_agent.md` - Generate comprehensive documentation
- `security_enforcer.md` - Security validation and best practices
- `qa_script_generator.md` - Generate test scripts

### Available Skills (in .claude/skills/)
- `action_sequencer.md` - Coordinate multi-step actions
- `e2e_test_runner.md` - End-to-end testing workflows

### Available Commands (in .claude/commands/)
- `/sp.constitution` - View/update constitution
- `/sp.checklist` - Generate implementation checklists
- `/sp.clarify` - Clarify requirements
- `/sp.adr` - Create Architecture Decision Records

## When Implementing Features

### Step-by-Step Process
1. **Read Constitution**: `.specify/memory/constitution.md`
2. **Read Feature Spec**: `/specs/features/<feature-name>.md`
3. **Understand Requirements**: User stories, acceptance criteria, edge cases
4. **Write Tests First** (TDD RED):
   - Copy test cases from spec
   - Implement in `tests/test_*.py`
   - Run tests - they MUST fail
5. **Implement Feature** (TDD GREEN):
   - Write minimal code to pass tests
   - Add type hints
   - Add docstrings
6. **Refactor** (TDD REFACTOR):
   - Improve code quality
   - Keep tests passing
7. **Verify Coverage**: Run `pytest` - must be 100% for core logic

### Common Pitfalls to Avoid
- ❌ Writing code before tests (violates TDD)
- ❌ Skipping type hints or docstrings (violates constitution)
- ❌ Using file I/O or databases (violates Phase I constraint)
- ❌ Ignoring edge cases from specs
- ❌ Not running tests frequently
- ❌ Accepting < 100% coverage for core logic

## Quick Reference

### File Locations
| Need | Location |
|------|----------|
| Constitution | `.specify/memory/constitution.md` |
| Feature Specs | `specs/features/*.md` |
| Task Model | `src/todo_app/models.py` |
| TodoManager | `src/todo_app/manager.py` |
| Console UI | `src/todo_app/ui.py` |
| Exceptions | `src/todo_app/exceptions.py` |
| Tests | `tests/test_*.py` |

### Essential Commands
| Command | Purpose |
|---------|---------|
| `pytest` | Run all tests with coverage |
| `pytest -v` | Verbose test output |
| `pytest -x` | Stop at first failure |
| `mypy src/` | Type checking |
| `ruff check src/` | Linting |
| `python -m todo_app.ui` | Run the app |

## Next Steps

After reading this file:
1. Read `.specify/memory/constitution.md` thoroughly
2. Read `specs/overview.md` for project context
3. Start with `specs/features/task-model.md`
4. Follow TDD: Tests → Implementation → Refactor
5. Repeat for each feature in order

## Getting Help

- Check specs for feature requirements
- Check constitution for coding standards
- Use available agents/skills for complex tasks
- Run tests frequently to catch issues early

---

**Remember**: Spec-Driven Development + Test-Driven Development = High-Quality, Maintainable Code

**Golden Rule**: If it's not in the spec, don't build it. If there's no test, it doesn't work.

Good luck! 🚀
