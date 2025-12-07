# Feature Spec: Task Model

## Overview

The Task model is the core data structure representing a single todo item in the application. It encapsulates all task-related data and provides validation and state management.

## User Stories

- As a developer, I need a Task model to represent todo items with title, description, and completion status
- As a developer, I need the Task model to validate input data and enforce constraints
- As a developer, I need the Task model to provide a unique identifier for each task

## Requirements

### Functional Requirements

#### FR-1: Task Properties
The Task model MUST have the following properties:

| Property | Type | Required | Constraints | Description |
|----------|------|----------|-------------|-------------|
| `id` | `int` | Yes | Unique, positive integer | Unique identifier for the task |
| `title` | `str` | Yes | 1-200 characters, non-empty | Short task title |
| `description` | `str` | No | 0-1000 characters | Detailed task description |
| `completed` | `bool` | Yes | Default: `False` | Task completion status |
| `created_at` | `datetime` | Yes | Auto-set on creation | When task was created |

#### FR-2: Task Initialization
- Tasks MUST be created with a title (required)
- Tasks MAY be created with a description (optional, defaults to empty string)
- Tasks MUST default to `completed=False` on creation
- Tasks MUST auto-generate creation timestamp
- Task IDs MUST be provided during initialization

#### FR-3: Task Validation
- Empty titles MUST raise `InvalidTaskDataError`
- Titles longer than 200 characters MUST raise `InvalidTaskDataError`
- Descriptions longer than 1000 characters MUST raise `InvalidTaskDataError`
- Invalid IDs (non-positive integers) MUST raise `ValueError`

### Non-Functional Requirements

#### NFR-1: Type Safety
- All properties MUST have type hints (PEP 484)
- Type hints MUST be accurate and complete

#### NFR-2: Documentation
- The Task class MUST have a comprehensive docstring
- All methods MUST have docstrings explaining purpose, parameters, and return values

#### NFR-3: Testability
- The Task model MUST be easily testable with pytest
- All validation logic MUST be unit-tested

## Acceptance Criteria

### AC-1: Task Creation (Happy Path)
```python
task = Task(id=1, title="Buy groceries")
assert task.id == 1
assert task.title == "Buy groceries"
assert task.description == ""
assert task.completed == False
assert isinstance(task.created_at, datetime)
```

### AC-2: Task Creation with Description
```python
task = Task(id=2, title="Meeting", description="Team standup at 10 AM")
assert task.title == "Meeting"
assert task.description == "Team standup at 10 AM"
```

### AC-3: Task Validation - Empty Title
```python
with pytest.raises(InvalidTaskDataError):
    task = Task(id=1, title="")
```

### AC-4: Task Validation - Title Too Long
```python
long_title = "x" * 201
with pytest.raises(InvalidTaskDataError):
    task = Task(id=1, title=long_title)
```

### AC-5: Task Validation - Description Too Long
```python
long_desc = "x" * 1001
with pytest.raises(InvalidTaskDataError):
    task = Task(id=1, title="Valid", description=long_desc)
```

### AC-6: Task Completion Toggle
```python
task = Task(id=1, title="Test")
assert task.completed == False

task.completed = True
assert task.completed == True
```

## Edge Cases

### EC-1: Whitespace-Only Title
- Title with only whitespace characters (spaces, tabs, newlines) SHOULD be rejected
- Example: `title="   "` SHOULD raise `InvalidTaskDataError`

### EC-2: None Values
- `title=None` MUST raise `InvalidTaskDataError`
- `description=None` SHOULD be converted to empty string ""

### EC-3: Unicode Characters
- Task title and description MUST support Unicode characters (e.g., "कार्य", "任務", "tâche")
- Validation MUST work correctly with Unicode

### EC-4: Special Characters
- Task title and description MUST support special characters: `@#$%^&*()[]{}!?`
- Newlines in description SHOULD be preserved

## Test Cases

### Test Suite: Task Model

#### Test: test_task_creation_with_required_fields_only()
```python
def test_task_creation_with_required_fields_only():
    """Test creating a task with only required fields."""
    task = Task(id=1, title="Buy milk")

    assert task.id == 1
    assert task.title == "Buy milk"
    assert task.description == ""
    assert task.completed is False
    assert isinstance(task.created_at, datetime)
```

#### Test: test_task_creation_with_all_fields()
```python
def test_task_creation_with_all_fields():
    """Test creating a task with all fields."""
    task = Task(
        id=5,
        title="Project meeting",
        description="Discuss Q1 roadmap"
    )

    assert task.id == 5
    assert task.title == "Project meeting"
    assert task.description == "Discuss Q1 roadmap"
```

#### Test: test_task_with_empty_title_raises_error()
```python
def test_task_with_empty_title_raises_error():
    """Test that empty title raises InvalidTaskDataError."""
    with pytest.raises(InvalidTaskDataError, match="Title cannot be empty"):
        Task(id=1, title="")
```

#### Test: test_task_with_title_exceeding_max_length_raises_error()
```python
def test_task_with_title_exceeding_max_length_raises_error():
    """Test that title >200 chars raises InvalidTaskDataError."""
    long_title = "x" * 201
    with pytest.raises(InvalidTaskDataError, match="Title must be"):
        Task(id=1, title=long_title)
```

#### Test: test_task_with_description_exceeding_max_length_raises_error()
```python
def test_task_with_description_exceeding_max_length_raises_error():
    """Test that description >1000 chars raises InvalidTaskDataError."""
    long_desc = "x" * 1001
    with pytest.raises(InvalidTaskDataError, match="Description must be"):
        Task(id=1, title="Valid", description=long_desc)
```

#### Test: test_task_completion_status_toggle()
```python
def test_task_completion_status_toggle():
    """Test toggling task completion status."""
    task = Task(id=1, title="Test task")

    assert task.completed is False

    task.completed = True
    assert task.completed is True

    task.completed = False
    assert task.completed is False
```

#### Test: test_task_with_unicode_characters()
```python
def test_task_with_unicode_characters():
    """Test task with Unicode characters in title and description."""
    task = Task(
        id=1,
        title="कार्य - 任務 - tâche",
        description="Supports 日本語 and العربية"
    )

    assert "कार्य" in task.title
    assert "日本語" in task.description
```

#### Test: test_task_string_representation()
```python
def test_task_string_representation():
    """Test task __repr__ and __str__ methods."""
    task = Task(id=3, title="Review code")

    repr_str = repr(task)
    assert "Task" in repr_str
    assert "id=3" in repr_str
    assert "Review code" in repr_str
```

## Implementation Notes

### Data Structure
```python
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Task:
    """
    Represents a single todo task.

    Attributes:
        id (int): Unique task identifier
        title (str): Task title (1-200 characters)
        description (str): Task description (0-1000 characters)
        completed (bool): Completion status
        created_at (datetime): Creation timestamp
    """
    id: int
    title: str
    description: str = ""
    completed: bool = False
    created_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        """Validate task data after initialization."""
        # Validation logic here
```

### Custom Exceptions
```python
class InvalidTaskDataError(Exception):
    """Raised when task data fails validation."""
    pass
```

## Dependencies

- Python 3.13+
- `dataclasses` (built-in)
- `datetime` (built-in)
- `typing` (built-in)
- `pytest` (for testing)

## Out of Scope

- Task persistence (Phase II)
- Task priorities (Phase V - Advanced features)
- Task tags/categories (Phase V - Intermediate features)
- Due dates (Phase V - Advanced features)
- Recurring tasks (Phase V - Advanced features)

---

**Status**: ✅ Ready for Implementation
**Version**: 1.0.0
**Created**: 2025-12-07
**Related Specs**: All CRUD operation specs depend on this model
