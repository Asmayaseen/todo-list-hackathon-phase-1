# Feature Spec: Delete Task

## Overview

Users can permanently remove tasks from the list by providing the task ID.

## User Stories

- As a user, I can delete a task by its ID
- As a user, I am prevented from deleting non-existent tasks
- As a user, I receive confirmation when a task is successfully deleted

## Requirements

### Functional Requirements

#### FR-1: Delete Task by ID
- User MUST be able to delete a task using its unique ID
- Deleted task MUST be completely removed from the task list
- System MUST confirm successful deletion

#### FR-2: Error Handling
- Attempting to delete a non-existent task ID MUST raise `TaskNotFoundException`
- Error message MUST include the invalid task ID for clarity

### Non-Functional Requirements

#### NFR-1: Performance
- Task deletion MUST be instant (<10ms)

#### NFR-2: ID Reuse
- Deleted task IDs MUST NOT be reused for new tasks
- Example: If task ID 2 is deleted, the next new task gets ID 4 (not 2)

## Acceptance Criteria

### AC-1: Delete Existing Task
```python
manager = TodoManager()
task = manager.add_task(title="To delete")

manager.delete_task(task_id=task.id)

assert task.id not in [t.id for t in manager.list_tasks()]
assert len(manager.list_tasks()) == 0
```

### AC-2: Delete Non-Existent Task Raises Error
```python
manager = TodoManager()

with pytest.raises(TaskNotFoundException, match="Task with ID 999 not found"):
    manager.delete_task(task_id=999)
```

### AC-3: Delete from Multiple Tasks
```python
manager = TodoManager()
task1 = manager.add_task(title="Task 1")
task2 = manager.add_task(title="Task 2")
task3 = manager.add_task(title="Task 3")

manager.delete_task(task_id=task2.id)

remaining_ids = [t.id for t in manager.list_tasks()]
assert task1.id in remaining_ids
assert task2.id not in remaining_ids
assert task3.id in remaining_ids
assert len(manager.list_tasks()) == 2
```

## Edge Cases

### EC-1: Delete All Tasks
```python
manager = TodoManager()
task1 = manager.add_task(title="Task 1")
task2 = manager.add_task(title="Task 2")

manager.delete_task(task_id=task1.id)
manager.delete_task(task_id=task2.id)

assert len(manager.list_tasks()) == 0
```

### EC-2: Invalid Task ID Type
```python
manager = TodoManager()

with pytest.raises(TypeError):
    manager.delete_task(task_id="invalid")  # String instead of int
```

## Test Cases

### Test: test_delete_existing_task()
```python
def test_delete_existing_task():
    """Test deleting an existing task."""
    manager = TodoManager()
    task = manager.add_task(title="To be deleted")

    manager.delete_task(task_id=task.id)

    assert len(manager.list_tasks()) == 0
```

### Test: test_delete_nonexistent_task_raises_error()
```python
def test_delete_nonexistent_task_raises_error():
    """Test that deleting non-existent task raises TaskNotFoundException."""
    manager = TodoManager()

    with pytest.raises(TaskNotFoundException, match="Task with ID 42 not found"):
        manager.delete_task(task_id=42)
```

### Test: test_delete_task_from_multiple_tasks()
```python
def test_delete_task_from_multiple_tasks():
    """Test deleting one task from multiple tasks."""
    manager = TodoManager()
    task1 = manager.add_task(title="Keep 1")
    task2 = manager.add_task(title="Delete me")
    task3 = manager.add_task(title="Keep 2")

    manager.delete_task(task_id=task2.id)

    remaining = manager.list_tasks()
    assert len(remaining) == 2
    assert task2.id not in [t.id for t in remaining]
```

## UI/UX Considerations

```
=== Delete Task ===
Enter task ID to delete: 2

✓ Task deleted successfully!
  Deleted: "Buy groceries" (ID: 2)
```

## Implementation Notes

```python
def delete_task(self, task_id: int) -> None:
    """
    Delete a task by ID.

    Args:
        task_id: The ID of the task to delete

    Raises:
        TaskNotFoundException: If task_id doesn't exist
    """
    if task_id not in self.tasks:
        raise TaskNotFoundException(f"Task with ID {task_id} not found")

    del self.tasks[task_id]
```

---

**Status**: ✅ Ready for Implementation
**Version**: 1.0.0
**Created**: 2025-12-07
**Dependencies**: task-model.md
