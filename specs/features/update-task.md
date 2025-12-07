# Feature Spec: Update Task

## Overview

Users can modify the title and/or description of existing tasks.

## User Stories

- As a user, I can update a task's title
- As a user, I can update a task's description
- As a user, I can update both title and description simultaneously
- As a user, I am prevented from updating tasks with invalid data

## Requirements

### Functional Requirements

#### FR-1: Update Task Title
- User MUST be able to update an existing task's title
- New title MUST follow same validation as task creation (1-200 chars, non-empty)

#### FR-2: Update Task Description
- User MUST be able to update an existing task's description
- New description MUST follow same validation (0-1000 chars)

#### FR-3: Partial Updates
- User MAY update only title (description unchanged)
- User MAY update only description (title unchanged)
- User MAY update both title and description

#### FR-4: Error Handling
- Updating non-existent task MUST raise `TaskNotFoundException`
- Invalid new data MUST raise `InvalidTaskDataError`

### Non-Functional Requirements

#### NFR-1: Immutability of Other Fields
- Task ID MUST remain unchanged
- Task completion status MUST remain unchanged (updated separately via mark_complete)
- Task created_at timestamp MUST remain unchanged

## Acceptance Criteria

### AC-1: Update Task Title Only
```python
manager = TodoManager()
task = manager.add_task(title="Old title", description="Original desc")

manager.update_task(task_id=task.id, title="New title")

updated = manager.get_task(task.id)
assert updated.title == "New title"
assert updated.description == "Original desc"
```

### AC-2: Update Task Description Only
```python
manager = TodoManager()
task = manager.add_task(title="Title", description="Old desc")

manager.update_task(task_id=task.id, description="New description")

updated = manager.get_task(task.id)
assert updated.title == "Title"
assert updated.description == "New description"
```

### AC-3: Update Both Title and Description
```python
manager = TodoManager()
task = manager.add_task(title="Old", description="Old desc")

manager.update_task(
    task_id=task.id,
    title="New Title",
    description="New Description"
)

updated = manager.get_task(task.id)
assert updated.title == "New Title"
assert updated.description == "New Description"
```

### AC-4: Update Non-Existent Task Raises Error
```python
manager = TodoManager()

with pytest.raises(TaskNotFoundException):
    manager.update_task(task_id=999, title="New")
```

### AC-5: Update with Invalid Title Raises Error
```python
manager = TodoManager()
task = manager.add_task(title="Original")

with pytest.raises(InvalidTaskDataError):
    manager.update_task(task_id=task.id, title="")  # Empty title
```

## Edge Cases

### EC-1: Update with Same Values
```python
manager = TodoManager()
task = manager.add_task(title="Title", description="Desc")

manager.update_task(task_id=task.id, title="Title", description="Desc")

# Should succeed without error
updated = manager.get_task(task.id)
assert updated.title == "Title"
```

### EC-2: Update Completed Task
```python
manager = TodoManager()
task = manager.add_task(title="Task")
manager.mark_complete(task_id=task.id)

manager.update_task(task_id=task.id, title="Updated Task")

updated = manager.get_task(task.id)
assert updated.title == "Updated Task"
assert updated.completed is True  # Status preserved
```

## Test Cases

### Test: test_update_task_title_only()
```python
def test_update_task_title_only():
    """Test updating only the task title."""
    manager = TodoManager()
    task = manager.add_task(title="Original", description="Desc")

    manager.update_task(task_id=task.id, title="Updated Title")

    updated = manager.get_task(task.id)
    assert updated.title == "Updated Title"
    assert updated.description == "Desc"
```

### Test: test_update_task_description_only()
```python
def test_update_task_description_only():
    """Test updating only the task description."""
    manager = TodoManager()
    task = manager.add_task(title="Title", description="Original")

    manager.update_task(task_id=task.id, description="New desc")

    updated = manager.get_task(task.id)
    assert updated.title == "Title"
    assert updated.description == "New desc"
```

### Test: test_update_both_title_and_description()
```python
def test_update_both_title_and_description():
    """Test updating both title and description."""
    manager = TodoManager()
    task = manager.add_task(title="Old", description="Old desc")

    manager.update_task(
        task_id=task.id,
        title="New",
        description="New desc"
    )

    updated = manager.get_task(task.id)
    assert updated.title == "New"
    assert updated.description == "New desc"
```

### Test: test_update_nonexistent_task_raises_error()
```python
def test_update_nonexistent_task_raises_error():
    """Test that updating non-existent task raises error."""
    manager = TodoManager()

    with pytest.raises(TaskNotFoundException):
        manager.update_task(task_id=42, title="New")
```

## UI/UX Considerations

```
=== Update Task ===
Enter task ID: 2
Current title: Buy groceries
Enter new title (or press Enter to keep current): Buy groceries and fruits
Current description: Milk, eggs
Enter new description (or press Enter to keep current): Milk, eggs, bread, fruits

✓ Task updated successfully!
  ID: 2
  Title: Buy groceries and fruits
  Description: Milk, eggs, bread, fruits
```

## Implementation Notes

```python
def update_task(
    self,
    task_id: int,
    title: Optional[str] = None,
    description: Optional[str] = None
) -> Task:
    """
    Update an existing task's title and/or description.

    Args:
        task_id: The ID of the task to update
        title: New title (if provided)
        description: New description (if provided)

    Returns:
        The updated Task object

    Raises:
        TaskNotFoundException: If task_id doesn't exist
        InvalidTaskDataError: If new data violates constraints
    """
    if task_id not in self.tasks:
        raise TaskNotFoundException(f"Task with ID {task_id} not found")

    task = self.tasks[task_id]

    if title is not None:
        # Validate title
        task.title = title.strip()

    if description is not None:
        # Validate description
        task.description = description

    return task
```

---

**Status**: ✅ Ready for Implementation
**Version**: 1.0.0
**Created**: 2025-12-07
**Dependencies**: task-model.md, add-task.md
