# Feature Spec: Add Task

## Overview

Users can create new tasks by providing a title and optional description. Tasks are stored in-memory and assigned a unique ID automatically.

## User Stories

- As a user, I can add a new task with just a title
- As a user, I can add a new task with both title and description
- As a user, I am prevented from adding tasks with invalid data (empty title, too long, etc.)
- As a user, I receive immediate feedback when a task is successfully added

## Requirements

### Functional Requirements

#### FR-1: Add Task with Title Only
- User MUST be able to create a task with only a title
- System MUST auto-generate a unique task ID
- Task MUST default to incomplete status (`completed=False`)
- Task MUST record creation timestamp

#### FR-2: Add Task with Title and Description
- User MUST be able to create a task with title and description
- Description MUST be optional
- Description MAY be empty string

#### FR-3: Input Validation
- Title MUST NOT be empty
- Title MUST NOT exceed 200 characters
- Description MUST NOT exceed 1000 characters
- System MUST reject invalid inputs with clear error messages

#### FR-4: Unique ID Assignment
- Each new task MUST receive a unique integer ID
- IDs MUST be sequential (1, 2, 3, ...)
- IDs MUST NOT be reused (even after task deletion)

### Non-Functional Requirements

#### NFR-1: Performance
- Task creation MUST be instant (<10ms) for in-memory storage

#### NFR-2: Error Messages
- Error messages MUST be clear and actionable
- Example: "Title cannot be empty" instead of "Invalid input"

#### NFR-3: Return Value
- `add_task()` MUST return the created Task object
- This allows immediate access to the task ID and other properties

## Acceptance Criteria

### AC-1: Add Task with Title Only
```python
manager = TodoManager()
task = manager.add_task(title="Buy groceries")

assert task.id == 1
assert task.title == "Buy groceries"
assert task.description == ""
assert task.completed is False
assert task.id in [t.id for t in manager.list_tasks()]
```

### AC-2: Add Task with Title and Description
```python
manager = TodoManager()
task = manager.add_task(
    title="Team meeting",
    description="Discuss Q1 roadmap at 2 PM"
)

assert task.title == "Team meeting"
assert task.description == "Discuss Q1 roadmap at 2 PM"
```

### AC-3: Add Multiple Tasks with Auto-Incrementing IDs
```python
manager = TodoManager()

task1 = manager.add_task(title="First task")
task2 = manager.add_task(title="Second task")
task3 = manager.add_task(title="Third task")

assert task1.id == 1
assert task2.id == 2
assert task3.id == 3
```

### AC-4: Reject Empty Title
```python
manager = TodoManager()

with pytest.raises(InvalidTaskDataError, match="Title cannot be empty"):
    manager.add_task(title="")
```

### AC-5: Reject Title Exceeding Max Length
```python
manager = TodoManager()
long_title = "x" * 201

with pytest.raises(InvalidTaskDataError, match="Title must be"):
    manager.add_task(title=long_title)
```

### AC-6: Reject Description Exceeding Max Length
```python
manager = TodoManager()
long_desc = "x" * 1001

with pytest.raises(InvalidTaskDataError, match="Description must be"):
    manager.add_task(title="Valid", description=long_desc)
```

## Edge Cases

### EC-1: Whitespace-Only Title
```python
manager = TodoManager()

with pytest.raises(InvalidTaskDataError):
    manager.add_task(title="   ")  # Only spaces
```

### EC-2: Title with Leading/Trailing Whitespace
- System SHOULD trim leading/trailing whitespace from title
- Example: `"  Task  "` → `"Task"`

### EC-3: Unicode Support
```python
manager = TodoManager()
task = manager.add_task(title="日本語タスク", description="説明文")

assert task.title == "日本語タスク"
```

### EC-4: Special Characters
```python
manager = TodoManager()
task = manager.add_task(title="Meeting @ 2PM!", description="Review #Q1 goals")

assert "@" in task.title
assert "#" in task.description
```

### EC-5: Very Long Valid Description
```python
manager = TodoManager()
long_desc = "x" * 1000  # Exactly 1000 chars (valid)

task = manager.add_task(title="Test", description=long_desc)
assert len(task.description) == 1000
```

## Test Cases

### Test Suite: Add Task

#### Test: test_add_task_with_title_only()
```python
def test_add_task_with_title_only():
    """Test adding a task with only a title."""
    manager = TodoManager()

    task = manager.add_task(title="Buy milk")

    assert task.id == 1
    assert task.title == "Buy milk"
    assert task.description == ""
    assert task.completed is False
    assert len(manager.list_tasks()) == 1
```

#### Test: test_add_task_with_title_and_description()
```python
def test_add_task_with_title_and_description():
    """Test adding a task with title and description."""
    manager = TodoManager()

    task = manager.add_task(
        title="Doctor appointment",
        description="Annual checkup at 10 AM"
    )

    assert task.title == "Doctor appointment"
    assert task.description == "Annual checkup at 10 AM"
```

#### Test: test_add_multiple_tasks_auto_increment_ids()
```python
def test_add_multiple_tasks_auto_increment_ids():
    """Test that multiple tasks get sequential IDs."""
    manager = TodoManager()

    task1 = manager.add_task(title="Task 1")
    task2 = manager.add_task(title="Task 2")
    task3 = manager.add_task(title="Task 3")

    assert task1.id == 1
    assert task2.id == 2
    assert task3.id == 3
```

#### Test: test_add_task_with_empty_title_raises_error()
```python
def test_add_task_with_empty_title_raises_error():
    """Test that empty title raises InvalidTaskDataError."""
    manager = TodoManager()

    with pytest.raises(InvalidTaskDataError, match="Title cannot be empty"):
        manager.add_task(title="")
```

#### Test: test_add_task_with_title_too_long_raises_error()
```python
def test_add_task_with_title_too_long_raises_error():
    """Test that title >200 chars raises InvalidTaskDataError."""
    manager = TodoManager()
    long_title = "x" * 201

    with pytest.raises(InvalidTaskDataError, match="Title must be"):
        manager.add_task(title=long_title)
```

#### Test: test_add_task_with_description_too_long_raises_error()
```python
def test_add_task_with_description_too_long_raises_error():
    """Test that description >1000 chars raises InvalidTaskDataError."""
    manager = TodoManager()
    long_desc = "x" * 1001

    with pytest.raises(InvalidTaskDataError):
        manager.add_task(title="Valid", description=long_desc)
```

#### Test: test_add_task_with_unicode_characters()
```python
def test_add_task_with_unicode_characters():
    """Test adding task with Unicode characters."""
    manager = TodoManager()

    task = manager.add_task(
        title="日本語タスク",
        description="説明: العربية - ελληνικά"
    )

    assert "日本語" in task.title
    assert "العربية" in task.description
```

#### Test: test_add_task_returns_task_object()
```python
def test_add_task_returns_task_object():
    """Test that add_task returns the created Task object."""
    manager = TodoManager()

    result = manager.add_task(title="Test")

    assert isinstance(result, Task)
    assert result.title == "Test"
```

## UI/UX Considerations

### Console Interface
When implementing the console UI, the add task flow should be:

```
=== Add New Task ===
Enter task title: Buy groceries
Enter description (optional, press Enter to skip): Milk, eggs, bread

✓ Task added successfully!
  ID: 1
  Title: Buy groceries
  Description: Milk, eggs, bread
  Status: Incomplete
```

### Error Handling in Console
```
=== Add New Task ===
Enter task title: [user presses Enter without typing]

✗ Error: Title cannot be empty. Please try again.
Enter task title:
```

## Implementation Notes

### TodoManager.add_task() Method

```python
class TodoManager:
    """Manages in-memory todo tasks."""

    def __init__(self):
        self.tasks: dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Add a new task to the list.

        Args:
            title: Task title (1-200 characters, required)
            description: Task description (0-1000 characters, optional)

        Returns:
            The newly created Task object

        Raises:
            InvalidTaskDataError: If title/description violate constraints
        """
        # Validation happens in Task.__post_init__()
        task = Task(
            id=self._next_id,
            title=title.strip(),  # Trim whitespace
            description=description
        )

        self.tasks[task.id] = task
        self._next_id += 1

        return task
```

## Dependencies

- Task model (see `task-model.md`)
- InvalidTaskDataError exception
- TodoManager class
- pytest for testing

## Out of Scope

- Bulk task import (not in Phase I)
- Task templates (not in Phase I)
- Task priorities (Phase V)
- Task categories/tags (Phase V)
- Task due dates (Phase V)

---

**Status**: ✅ Ready for Implementation
**Version**: 1.0.0
**Created**: 2025-12-07
**Dependencies**: task-model.md
