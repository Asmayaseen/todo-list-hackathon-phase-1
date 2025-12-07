# Feature Spec: View Tasks

## Overview

Users can view all tasks in the list with filtering options to show all tasks, only pending tasks, or only completed tasks.

## User Stories

- As a user, I can view all my tasks at once
- As a user, I can filter tasks by completion status (all, pending, completed)
- As a user, I can see task details including ID, title, description, and status
- As a user, I receive a clear message when the task list is empty

## Requirements

### Functional Requirements

#### FR-1: List All Tasks
- User MUST be able to view all tasks regardless of status
- Tasks SHOULD be displayed in order of creation (oldest first)
- Each task display MUST include: ID, title, description, completion status

#### FR-2: Filter by Status
- User MUST be able to filter tasks by status:
  - `status="all"` - Show all tasks (default)
  - `status="pending"` - Show only incomplete tasks
  - `status="completed"` - Show only completed tasks

#### FR-3: Empty List Handling
- When no tasks exist, MUST return empty list (not None)
- UI SHOULD display friendly message like "No tasks found"

### Non-Functional Requirements

#### NFR-1: Return Type
- `list_tasks()` MUST return `list[Task]`
- List MUST contain Task objects, not dictionaries or tuples

#### NFR-2: Performance
- Listing tasks MUST be instant even with 100+ tasks

## Acceptance Criteria

### AC-1: List All Tasks
```python
manager = TodoManager()
task1 = manager.add_task(title="Task 1")
task2 = manager.add_task(title="Task 2")
manager.mark_complete(task_id=task1.id)

all_tasks = manager.list_tasks(status="all")

assert len(all_tasks) == 2
assert task1 in all_tasks
assert task2 in all_tasks
```

### AC-2: List Pending Tasks Only
```python
manager = TodoManager()
task1 = manager.add_task(title="Pending task")
task2 = manager.add_task(title="Completed task")
manager.mark_complete(task_id=task2.id)

pending = manager.list_tasks(status="pending")

assert len(pending) == 1
assert task1 in pending
assert task2 not in pending
```

### AC-3: List Completed Tasks Only
```python
manager = TodoManager()
task1 = manager.add_task(title="Pending task")
task2 = manager.add_task(title="Completed task")
manager.mark_complete(task_id=task2.id)

completed = manager.list_tasks(status="completed")

assert len(completed) == 1
assert task2 in completed
assert task1 not in completed
```

### AC-4: Empty Task List
```python
manager = TodoManager()

tasks = manager.list_tasks()

assert tasks == []
assert isinstance(tasks, list)
```

### AC-5: Default Status is "all"
```python
manager = TodoManager()
task1 = manager.add_task(title="Task 1")
task2 = manager.add_task(title="Task 2")
manager.mark_complete(task_id=task1.id)

# No status parameter = show all
default_tasks = manager.list_tasks()
explicit_all = manager.list_tasks(status="all")

assert len(default_tasks) == 2
assert default_tasks == explicit_all
```

## Edge Cases

### EC-1: All Tasks Completed
```python
manager = TodoManager()
task1 = manager.add_task(title="Task 1")
task2 = manager.add_task(title="Task 2")
manager.mark_complete(task_id=task1.id)
manager.mark_complete(task_id=task2.id)

pending = manager.list_tasks(status="pending")
completed = manager.list_tasks(status="completed")

assert len(pending) == 0
assert len(completed) == 2
```

### EC-2: Invalid Status Parameter
```python
manager = TodoManager()

with pytest.raises(ValueError, match="Invalid status"):
    manager.list_tasks(status="invalid")
```

### EC-3: Task Order Preservation
```python
manager = TodoManager()
task1 = manager.add_task(title="First")
task2 = manager.add_task(title="Second")
task3 = manager.add_task(title="Third")

tasks = manager.list_tasks()

assert tasks[0].title == "First"
assert tasks[1].title == "Second"
assert tasks[2].title == "Third"
```

## Test Cases

### Test: test_list_all_tasks()
```python
def test_list_all_tasks():
    """Test listing all tasks regardless of status."""
    manager = TodoManager()
    task1 = manager.add_task(title="Task 1")
    task2 = manager.add_task(title="Task 2")
    manager.mark_complete(task_id=task1.id)

    all_tasks = manager.list_tasks(status="all")

    assert len(all_tasks) == 2
```

### Test: test_list_pending_tasks_only()
```python
def test_list_pending_tasks_only():
    """Test listing only pending (incomplete) tasks."""
    manager = TodoManager()
    task1 = manager.add_task(title="Pending")
    task2 = manager.add_task(title="Completed")
    manager.mark_complete(task_id=task2.id)

    pending = manager.list_tasks(status="pending")

    assert len(pending) == 1
    assert pending[0].title == "Pending"
```

### Test: test_list_completed_tasks_only()
```python
def test_list_completed_tasks_only():
    """Test listing only completed tasks."""
    manager = TodoManager()
    task1 = manager.add_task(title="Pending")
    task2 = manager.add_task(title="Completed")
    manager.mark_complete(task_id=task2.id)

    completed = manager.list_tasks(status="completed")

    assert len(completed) == 1
    assert completed[0].title == "Completed"
```

### Test: test_list_tasks_empty_list()
```python
def test_list_tasks_empty_list():
    """Test listing tasks when no tasks exist."""
    manager = TodoManager()

    tasks = manager.list_tasks()

    assert tasks == []
    assert isinstance(tasks, list)
```

### Test: test_list_tasks_default_shows_all()
```python
def test_list_tasks_default_shows_all():
    """Test that default (no status parameter) shows all tasks."""
    manager = TodoManager()
    task1 = manager.add_task(title="Task 1")
    task2 = manager.add_task(title="Task 2")
    manager.mark_complete(task_id=task1.id)

    default = manager.list_tasks()
    explicit = manager.list_tasks(status="all")

    assert len(default) == 2
    assert default == explicit
```

## UI/UX Considerations

### Display Format
```
=== Task List (All) ===

[1] ✓ Buy groceries
    Description: Milk, eggs, bread
    Status: Completed

[2] ☐ Team meeting
    Description: Discuss Q1 roadmap
    Status: Pending

Total: 2 tasks (1 completed, 1 pending)
```

### Empty List
```
=== Task List (All) ===

No tasks found. Add a new task to get started!
```

### Filter View
```
=== Task List (Pending Only) ===

[2] ☐ Team meeting
    Description: Discuss Q1 roadmap
    Status: Pending

[4] ☐ Call dentist
    Description: Schedule appointment
    Status: Pending

Total: 2 pending tasks
```

## Implementation Notes

```python
def list_tasks(self, status: str = "all") -> list[Task]:
    """
    List tasks with optional status filter.

    Args:
        status: Filter by status - "all", "pending", or "completed"
                Default is "all"

    Returns:
        List of Task objects matching the filter

    Raises:
        ValueError: If status is not one of the valid options
    """
    valid_statuses = ["all", "pending", "completed"]
    if status not in valid_statuses:
        raise ValueError(
            f"Invalid status '{status}'. Must be one of: {valid_statuses}"
        )

    if status == "all":
        return list(self.tasks.values())
    elif status == "pending":
        return [task for task in self.tasks.values() if not task.completed]
    else:  # status == "completed"
        return [task for task in self.tasks.values() if task.completed]
```

### Helper Method: get_task()
```python
def get_task(self, task_id: int) -> Task:
    """
    Get a single task by ID.

    Args:
        task_id: The ID of the task to retrieve

    Returns:
        The Task object

    Raises:
        TaskNotFoundException: If task_id doesn't exist
    """
    if task_id not in self.tasks:
        raise TaskNotFoundException(f"Task with ID {task_id} not found")

    return self.tasks[task_id]
```

---

**Status**: ✅ Ready for Implementation
**Version**: 1.0.0
**Created**: 2025-12-07
**Dependencies**: task-model.md
