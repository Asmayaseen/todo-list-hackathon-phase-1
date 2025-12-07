# Feature Spec: Mark Task as Complete/Incomplete

## Overview

Users can toggle the completion status of tasks. Tasks can be marked as complete (done) or marked back to incomplete (pending).

## User Stories

- As a user, I can mark a pending task as complete
- As a user, I can mark a completed task back to incomplete (if I made a mistake)
- As a user, I am prevented from marking non-existent tasks
- As a user, I receive confirmation when task status is changed

## Requirements

### Functional Requirements

#### FR-1: Mark Task as Complete
- User MUST be able to mark a pending task as complete
- Task's `completed` property MUST be set to `True`
- Other task properties (title, description, ID) MUST remain unchanged

#### FR-2: Mark Task as Incomplete
- User MUST be able to mark a completed task back to incomplete
- Task's `completed` property MUST be set to `False`
- This allows users to correct mistakes

#### FR-3: Toggle Behavior
- The method SHOULD support toggling between complete/incomplete
- Calling mark_complete on a completed task SHOULD toggle it to incomplete
- OR provide separate methods: `mark_complete()` and `mark_incomplete()`

#### FR-4: Error Handling
- Attempting to mark a non-existent task MUST raise `TaskNotFoundException`

### Non-Functional Requirements

#### NFR-1: Idempotence
- Marking an already-complete task as complete again SHOULD succeed without error
- Final state: task is complete (no change)

#### NFR-2: Performance
- Status toggle MUST be instant (<10ms)

## Acceptance Criteria

### AC-1: Mark Pending Task as Complete
```python
manager = TodoManager()
task = manager.add_task(title="Buy milk")

assert task.completed is False

manager.mark_complete(task_id=task.id)

updated = manager.get_task(task.id)
assert updated.completed is True
```

### AC-2: Mark Completed Task as Incomplete
```python
manager = TodoManager()
task = manager.add_task(title="Task")
manager.mark_complete(task_id=task.id)

assert task.completed is True

manager.mark_incomplete(task_id=task.id)

updated = manager.get_task(task.id)
assert updated.completed is False
```

### AC-3: Toggle Task Status
```python
manager = TodoManager()
task = manager.add_task(title="Task")

# First toggle: pending -> complete
manager.toggle_complete(task_id=task.id)
assert manager.get_task(task.id).completed is True

# Second toggle: complete -> pending
manager.toggle_complete(task_id=task.id)
assert manager.get_task(task.id).completed is False
```

### AC-4: Mark Non-Existent Task Raises Error
```python
manager = TodoManager()

with pytest.raises(TaskNotFoundException):
    manager.mark_complete(task_id=999)
```

### AC-5: Title and Description Unchanged
```python
manager = TodoManager()
task = manager.add_task(title="Original Title", description="Original Description")

original_title = task.title
original_desc = task.description

manager.mark_complete(task_id=task.id)

updated = manager.get_task(task.id)
assert updated.title == original_title
assert updated.description == original_desc
assert updated.completed is True
```

## Edge Cases

### EC-1: Mark Already-Complete Task as Complete
```python
manager = TodoManager()
task = manager.add_task(title="Task")
manager.mark_complete(task_id=task.id)

# Mark complete again (idempotent)
manager.mark_complete(task_id=task.id)

assert manager.get_task(task.id).completed is True
```

### EC-2: Mark Already-Incomplete Task as Incomplete
```python
manager = TodoManager()
task = manager.add_task(title="Task")

# Already incomplete, mark incomplete again
manager.mark_incomplete(task_id=task.id)

assert manager.get_task(task.id).completed is False
```

### EC-3: Complete All Tasks
```python
manager = TodoManager()
task1 = manager.add_task(title="Task 1")
task2 = manager.add_task(title="Task 2")
task3 = manager.add_task(title="Task 3")

manager.mark_complete(task_id=task1.id)
manager.mark_complete(task_id=task2.id)
manager.mark_complete(task_id=task3.id)

completed = manager.list_tasks(status="completed")
assert len(completed) == 3
```

## Test Cases

### Test: test_mark_task_as_complete()
```python
def test_mark_task_as_complete():
    """Test marking a pending task as complete."""
    manager = TodoManager()
    task = manager.add_task(title="Buy groceries")

    assert task.completed is False

    manager.mark_complete(task_id=task.id)

    updated = manager.get_task(task.id)
    assert updated.completed is True
```

### Test: test_mark_task_as_incomplete()
```python
def test_mark_task_as_incomplete():
    """Test marking a completed task as incomplete."""
    manager = TodoManager()
    task = manager.add_task(title="Task")
    manager.mark_complete(task_id=task.id)

    manager.mark_incomplete(task_id=task.id)

    updated = manager.get_task(task.id)
    assert updated.completed is False
```

### Test: test_toggle_task_completion_status()
```python
def test_toggle_task_completion_status():
    """Test toggling task between complete and incomplete."""
    manager = TodoManager()
    task = manager.add_task(title="Task")

    # Toggle to complete
    manager.toggle_complete(task_id=task.id)
    assert manager.get_task(task.id).completed is True

    # Toggle back to incomplete
    manager.toggle_complete(task_id=task.id)
    assert manager.get_task(task.id).completed is False
```

### Test: test_mark_complete_preserves_other_fields()
```python
def test_mark_complete_preserves_other_fields():
    """Test that marking complete doesn't change other fields."""
    manager = TodoManager()
    task = manager.add_task(title="Title", description="Description")

    original_id = task.id
    original_title = task.title
    original_desc = task.description

    manager.mark_complete(task_id=task.id)

    updated = manager.get_task(task.id)
    assert updated.id == original_id
    assert updated.title == original_title
    assert updated.description == original_desc
```

### Test: test_mark_complete_nonexistent_task_raises_error()
```python
def test_mark_complete_nonexistent_task_raises_error():
    """Test that marking non-existent task raises error."""
    manager = TodoManager()

    with pytest.raises(TaskNotFoundException):
        manager.mark_complete(task_id=999)
```

### Test: test_mark_complete_idempotent()
```python
def test_mark_complete_idempotent():
    """Test that marking already-complete task is idempotent."""
    manager = TodoManager()
    task = manager.add_task(title="Task")

    manager.mark_complete(task_id=task.id)
    manager.mark_complete(task_id=task.id)  # Mark again

    assert manager.get_task(task.id).completed is True
```

## UI/UX Considerations

### Mark Complete
```
=== Mark Task as Complete ===
Enter task ID: 2

✓ Task marked as complete!
  [2] ✓ Buy groceries
```

### Mark Incomplete
```
=== Mark Task as Incomplete ===
Enter task ID: 2

✓ Task marked as incomplete!
  [2] ☐ Buy groceries
```

### Toggle
```
=== Toggle Task Status ===
Enter task ID: 2
Current status: Incomplete

✓ Status toggled!
  [2] ✓ Buy groceries (now complete)
```

## Implementation Notes

### Recommended Approach: Separate Methods

```python
def mark_complete(self, task_id: int) -> None:
    """
    Mark a task as complete.

    Args:
        task_id: The ID of the task to mark complete

    Raises:
        TaskNotFoundException: If task_id doesn't exist
    """
    if task_id not in self.tasks:
        raise TaskNotFoundException(f"Task with ID {task_id} not found")

    self.tasks[task_id].completed = True


def mark_incomplete(self, task_id: int) -> None:
    """
    Mark a task as incomplete.

    Args:
        task_id: The ID of the task to mark incomplete

    Raises:
        TaskNotFoundException: If task_id doesn't exist
    """
    if task_id not in self.tasks:
        raise TaskNotFoundException(f"Task with ID {task_id} not found")

    self.tasks[task_id].completed = False


def toggle_complete(self, task_id: int) -> None:
    """
    Toggle task completion status.

    Args:
        task_id: The ID of the task to toggle

    Raises:
        TaskNotFoundException: If task_id doesn't exist
    """
    if task_id not in self.tasks:
        raise TaskNotFoundException(f"Task with ID {task_id} not found")

    task = self.tasks[task_id]
    task.completed = not task.completed
```

### Alternative: Single Method with Parameter

```python
def set_complete(self, task_id: int, completed: bool) -> None:
    """
    Set task completion status.

    Args:
        task_id: The ID of the task
        completed: True to mark complete, False for incomplete

    Raises:
        TaskNotFoundException: If task_id doesn't exist
    """
    if task_id not in self.tasks:
        raise TaskNotFoundException(f"Task with ID {task_id} not found")

    self.tasks[task_id].completed = completed
```

## Design Decision: Which Approach?

**Recommendation**: Use separate methods (`mark_complete`, `mark_incomplete`, `toggle_complete`)

**Rationale**:
- More explicit and readable: `mark_complete(2)` vs `set_complete(2, True)`
- Follows command pattern (clear intent)
- `toggle_complete` is convenient for UI interactions
- Easier to test each behavior separately

---

**Status**: ✅ Ready for Implementation
**Version**: 1.0.0
**Created**: 2025-12-07
**Dependencies**: task-model.md
