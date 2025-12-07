"""
Unit tests for the TodoManager class.

Following TDD principles: Tests written before implementation.
Target: 100% code coverage for manager.py
"""

import pytest

from todo_app.exceptions import InvalidTaskDataError, TaskNotFoundException
from todo_app.manager import TodoManager
from todo_app.models import Task


class TestTodoManagerInit:
    """Test suite for TodoManager initialization."""

    def test_manager_initializes_with_empty_task_list(self):
        """Test that new manager has empty task list."""
        manager = TodoManager()

        assert len(manager.list_tasks()) == 0

    def test_manager_initializes_with_id_counter_at_one(self):
        """Test that new manager starts ID counter at 1."""
        manager = TodoManager()
        task = manager.add_task(title="First task")

        assert task.id == 1


class TestAddTask:
    """Test suite for add_task functionality."""

    def test_add_task_with_title_only(self):
        """Test adding a task with only a title."""
        manager = TodoManager()

        task = manager.add_task(title="Buy milk")

        assert task.id == 1
        assert task.title == "Buy milk"
        assert task.description == ""
        assert task.completed is False
        assert len(manager.list_tasks()) == 1

    def test_add_task_with_title_and_description(self):
        """Test adding a task with title and description."""
        manager = TodoManager()

        task = manager.add_task(
            title="Doctor appointment", description="Annual checkup at 10 AM"
        )

        assert task.title == "Doctor appointment"
        assert task.description == "Annual checkup at 10 AM"

    def test_add_multiple_tasks_auto_increment_ids(self):
        """Test that multiple tasks get sequential IDs."""
        manager = TodoManager()

        task1 = manager.add_task(title="Task 1")
        task2 = manager.add_task(title="Task 2")
        task3 = manager.add_task(title="Task 3")

        assert task1.id == 1
        assert task2.id == 2
        assert task3.id == 3

    def test_add_task_with_empty_title_raises_error(self):
        """Test that empty title raises InvalidTaskDataError."""
        manager = TodoManager()

        with pytest.raises(InvalidTaskDataError, match="Title cannot be empty"):
            manager.add_task(title="")

    def test_add_task_with_title_too_long_raises_error(self):
        """Test that title >200 chars raises InvalidTaskDataError."""
        manager = TodoManager()
        long_title = "x" * 201

        with pytest.raises(
            InvalidTaskDataError, match="Title must be between 1 and 200 characters"
        ):
            manager.add_task(title=long_title)

    def test_add_task_with_description_too_long_raises_error(self):
        """Test that description >1000 chars raises InvalidTaskDataError."""
        manager = TodoManager()
        long_desc = "x" * 1001

        with pytest.raises(InvalidTaskDataError):
            manager.add_task(title="Valid", description=long_desc)

    def test_add_task_with_unicode_characters(self):
        """Test adding task with Unicode characters."""
        manager = TodoManager()

        task = manager.add_task(title="日本語タスク", description="説明: العربية")

        assert "日本語" in task.title
        assert "العربية" in task.description

    def test_add_task_returns_task_object(self):
        """Test that add_task returns the created Task object."""
        manager = TodoManager()

        result = manager.add_task(title="Test")

        assert isinstance(result, Task)
        assert result.title == "Test"

    def test_add_task_trims_whitespace_from_title(self):
        """Test that add_task trims leading/trailing whitespace."""
        manager = TodoManager()

        task = manager.add_task(title="  Task with spaces  ")

        assert task.title == "Task with spaces"


class TestListTasks:
    """Test suite for list_tasks functionality."""

    def test_list_all_tasks(self):
        """Test listing all tasks regardless of status."""
        manager = TodoManager()
        task1 = manager.add_task(title="Task 1")
        task2 = manager.add_task(title="Task 2")
        manager.mark_complete(task_id=task1.id)

        all_tasks = manager.list_tasks(status="all")

        assert len(all_tasks) == 2
        assert task1 in all_tasks
        assert task2 in all_tasks

    def test_list_pending_tasks_only(self):
        """Test listing only pending (incomplete) tasks."""
        manager = TodoManager()
        task1 = manager.add_task(title="Pending")
        task2 = manager.add_task(title="Completed")
        manager.mark_complete(task_id=task2.id)

        pending = manager.list_tasks(status="pending")

        assert len(pending) == 1
        assert pending[0].title == "Pending"
        assert task2 not in pending

    def test_list_completed_tasks_only(self):
        """Test listing only completed tasks."""
        manager = TodoManager()
        task1 = manager.add_task(title="Pending")
        task2 = manager.add_task(title="Completed")
        manager.mark_complete(task_id=task2.id)

        completed = manager.list_tasks(status="completed")

        assert len(completed) == 1
        assert completed[0].title == "Completed"
        assert task1 not in completed

    def test_list_tasks_empty_list(self):
        """Test listing tasks when no tasks exist."""
        manager = TodoManager()

        tasks = manager.list_tasks()

        assert tasks == []
        assert isinstance(tasks, list)

    def test_list_tasks_default_shows_all(self):
        """Test that default (no status parameter) shows all tasks."""
        manager = TodoManager()
        task1 = manager.add_task(title="Task 1")
        task2 = manager.add_task(title="Task 2")
        manager.mark_complete(task_id=task1.id)

        default = manager.list_tasks()
        explicit = manager.list_tasks(status="all")

        assert len(default) == 2
        assert default == explicit

    def test_list_tasks_with_invalid_status_raises_error(self):
        """Test that invalid status parameter raises ValueError."""
        manager = TodoManager()

        with pytest.raises(ValueError, match="Invalid status"):
            manager.list_tasks(status="invalid")

    def test_list_tasks_preserves_order(self):
        """Test that tasks are returned in creation order."""
        manager = TodoManager()
        task1 = manager.add_task(title="First")
        task2 = manager.add_task(title="Second")
        task3 = manager.add_task(title="Third")

        tasks = manager.list_tasks()

        assert tasks[0].title == "First"
        assert tasks[1].title == "Second"
        assert tasks[2].title == "Third"


class TestGetTask:
    """Test suite for get_task functionality."""

    def test_get_existing_task(self):
        """Test getting an existing task by ID."""
        manager = TodoManager()
        task = manager.add_task(title="Test task")

        retrieved = manager.get_task(task_id=task.id)

        assert retrieved == task
        assert retrieved.title == "Test task"

    def test_get_nonexistent_task_raises_error(self):
        """Test that getting non-existent task raises TaskNotFoundException."""
        manager = TodoManager()

        with pytest.raises(TaskNotFoundException, match="Task with ID 999 not found"):
            manager.get_task(task_id=999)

    def test_get_task_returns_correct_task(self):
        """Test that get_task returns the correct task among multiple."""
        manager = TodoManager()
        task1 = manager.add_task(title="Task 1")
        task2 = manager.add_task(title="Task 2")
        task3 = manager.add_task(title="Task 3")

        retrieved = manager.get_task(task_id=task2.id)

        assert retrieved == task2
        assert retrieved.title == "Task 2"


class TestDeleteTask:
    """Test suite for delete_task functionality."""

    def test_delete_existing_task(self):
        """Test deleting an existing task."""
        manager = TodoManager()
        task = manager.add_task(title="To be deleted")

        manager.delete_task(task_id=task.id)

        assert len(manager.list_tasks()) == 0

    def test_delete_nonexistent_task_raises_error(self):
        """Test that deleting non-existent task raises TaskNotFoundException."""
        manager = TodoManager()

        with pytest.raises(TaskNotFoundException, match="Task with ID 42 not found"):
            manager.delete_task(task_id=42)

    def test_delete_task_from_multiple_tasks(self):
        """Test deleting one task from multiple tasks."""
        manager = TodoManager()
        task1 = manager.add_task(title="Keep 1")
        task2 = manager.add_task(title="Delete me")
        task3 = manager.add_task(title="Keep 2")

        manager.delete_task(task_id=task2.id)

        remaining = manager.list_tasks()
        assert len(remaining) == 2
        assert task2 not in remaining
        assert task1 in remaining
        assert task3 in remaining

    def test_delete_all_tasks(self):
        """Test deleting all tasks one by one."""
        manager = TodoManager()
        task1 = manager.add_task(title="Task 1")
        task2 = manager.add_task(title="Task 2")

        manager.delete_task(task_id=task1.id)
        manager.delete_task(task_id=task2.id)

        assert len(manager.list_tasks()) == 0

    def test_delete_task_id_not_reused(self):
        """Test that deleted task IDs are not reused."""
        manager = TodoManager()
        task1 = manager.add_task(title="Task 1")
        task2 = manager.add_task(title="Task 2")

        manager.delete_task(task_id=task1.id)

        task3 = manager.add_task(title="Task 3")

        # New task should get ID 3, not reuse ID 1
        assert task3.id == 3
        assert task3.id != task1.id


class TestUpdateTask:
    """Test suite for update_task functionality."""

    def test_update_task_title_only(self):
        """Test updating only the task title."""
        manager = TodoManager()
        task = manager.add_task(title="Original", description="Desc")

        manager.update_task(task_id=task.id, title="Updated Title")

        updated = manager.get_task(task.id)
        assert updated.title == "Updated Title"
        assert updated.description == "Desc"

    def test_update_task_description_only(self):
        """Test updating only the task description."""
        manager = TodoManager()
        task = manager.add_task(title="Title", description="Original")

        manager.update_task(task_id=task.id, description="New desc")

        updated = manager.get_task(task.id)
        assert updated.title == "Title"
        assert updated.description == "New desc"

    def test_update_both_title_and_description(self):
        """Test updating both title and description."""
        manager = TodoManager()
        task = manager.add_task(title="Old", description="Old desc")

        manager.update_task(
            task_id=task.id, title="New", description="New desc"
        )

        updated = manager.get_task(task.id)
        assert updated.title == "New"
        assert updated.description == "New desc"

    def test_update_nonexistent_task_raises_error(self):
        """Test that updating non-existent task raises error."""
        manager = TodoManager()

        with pytest.raises(TaskNotFoundException):
            manager.update_task(task_id=42, title="New")

    def test_update_task_with_invalid_title_raises_error(self):
        """Test that updating with invalid title raises error."""
        manager = TodoManager()
        task = manager.add_task(title="Original")

        with pytest.raises(InvalidTaskDataError):
            manager.update_task(task_id=task.id, title="")

    def test_update_task_with_same_values(self):
        """Test updating with same values succeeds."""
        manager = TodoManager()
        task = manager.add_task(title="Title", description="Desc")

        manager.update_task(task_id=task.id, title="Title", description="Desc")

        updated = manager.get_task(task.id)
        assert updated.title == "Title"

    def test_update_preserves_completion_status(self):
        """Test that update preserves completion status."""
        manager = TodoManager()
        task = manager.add_task(title="Task")
        manager.mark_complete(task_id=task.id)

        manager.update_task(task_id=task.id, title="Updated Task")

        updated = manager.get_task(task.id)
        assert updated.title == "Updated Task"
        assert updated.completed is True


class TestMarkComplete:
    """Test suite for mark_complete functionality."""

    def test_mark_task_as_complete(self):
        """Test marking a pending task as complete."""
        manager = TodoManager()
        task = manager.add_task(title="Buy groceries")

        assert task.completed is False

        manager.mark_complete(task_id=task.id)

        updated = manager.get_task(task.id)
        assert updated.completed is True

    def test_mark_complete_nonexistent_task_raises_error(self):
        """Test that marking non-existent task raises error."""
        manager = TodoManager()

        with pytest.raises(TaskNotFoundException):
            manager.mark_complete(task_id=999)

    def test_mark_complete_idempotent(self):
        """Test that marking already-complete task is idempotent."""
        manager = TodoManager()
        task = manager.add_task(title="Task")

        manager.mark_complete(task_id=task.id)
        manager.mark_complete(task_id=task.id)  # Mark again

        assert manager.get_task(task.id).completed is True

    def test_mark_complete_preserves_other_fields(self):
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


class TestMarkIncomplete:
    """Test suite for mark_incomplete functionality."""

    def test_mark_task_as_incomplete(self):
        """Test marking a completed task as incomplete."""
        manager = TodoManager()
        task = manager.add_task(title="Task")
        manager.mark_complete(task_id=task.id)

        manager.mark_incomplete(task_id=task.id)

        updated = manager.get_task(task.id)
        assert updated.completed is False

    def test_mark_incomplete_nonexistent_task_raises_error(self):
        """Test that marking non-existent task raises error."""
        manager = TodoManager()

        with pytest.raises(TaskNotFoundException):
            manager.mark_incomplete(task_id=999)


class TestToggleComplete:
    """Test suite for toggle_complete functionality."""

    def test_toggle_task_completion_status(self):
        """Test toggling task between complete and incomplete."""
        manager = TodoManager()
        task = manager.add_task(title="Task")

        # Toggle to complete
        manager.toggle_complete(task_id=task.id)
        assert manager.get_task(task.id).completed is True

        # Toggle back to incomplete
        manager.toggle_complete(task_id=task.id)
        assert manager.get_task(task.id).completed is False

    def test_toggle_complete_nonexistent_task_raises_error(self):
        """Test that toggling non-existent task raises error."""
        manager = TodoManager()

        with pytest.raises(TaskNotFoundException):
            manager.toggle_complete(task_id=999)
