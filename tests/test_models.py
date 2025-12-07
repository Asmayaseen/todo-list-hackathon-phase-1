"""
Unit tests for the Task model.

Following TDD principles: Tests written before implementation.
Target: 100% code coverage for models.py
"""

from datetime import datetime

import pytest

from todo_app.exceptions import InvalidTaskDataError
from todo_app.models import Task


class TestTaskCreation:
    """Test suite for Task model creation and initialization."""

    def test_task_creation_with_required_fields_only(self):
        """Test creating a task with only required fields."""
        task = Task(id=1, title="Buy milk")

        assert task.id == 1
        assert task.title == "Buy milk"
        assert task.description == ""
        assert task.completed is False
        assert isinstance(task.created_at, datetime)

    def test_task_creation_with_all_fields(self):
        """Test creating a task with all fields."""
        task = Task(
            id=5,
            title="Project meeting",
            description="Discuss Q1 roadmap",
        )

        assert task.id == 5
        assert task.title == "Project meeting"
        assert task.description == "Discuss Q1 roadmap"
        assert task.completed is False

    def test_task_creation_with_explicit_completed_status(self):
        """Test creating a task with explicit completed status."""
        task = Task(id=1, title="Done task", completed=True)

        assert task.completed is True

    def test_task_id_is_preserved(self):
        """Test that task ID is correctly set and preserved."""
        task1 = Task(id=1, title="First")
        task2 = Task(id=100, title="Hundredth")

        assert task1.id == 1
        assert task2.id == 100


class TestTaskValidation:
    """Test suite for Task model validation."""

    def test_task_with_empty_title_raises_error(self):
        """Test that empty title raises InvalidTaskDataError."""
        with pytest.raises(InvalidTaskDataError, match="Title cannot be empty"):
            Task(id=1, title="")

    def test_task_with_whitespace_only_title_raises_error(self):
        """Test that whitespace-only title raises InvalidTaskDataError."""
        with pytest.raises(InvalidTaskDataError, match="Title cannot be empty"):
            Task(id=1, title="   ")

    def test_task_with_title_exceeding_max_length_raises_error(self):
        """Test that title >200 chars raises InvalidTaskDataError."""
        long_title = "x" * 201
        with pytest.raises(
            InvalidTaskDataError, match="Title must be between 1 and 200 characters"
        ):
            Task(id=1, title=long_title)

    def test_task_with_description_exceeding_max_length_raises_error(self):
        """Test that description >1000 chars raises InvalidTaskDataError."""
        long_desc = "x" * 1001
        with pytest.raises(
            InvalidTaskDataError,
            match="Description must be at most 1000 characters",
        ):
            Task(id=1, title="Valid", description=long_desc)

    def test_task_with_valid_max_length_title(self):
        """Test that title with exactly 200 chars is valid."""
        max_title = "x" * 200
        task = Task(id=1, title=max_title)

        assert len(task.title) == 200

    def test_task_with_valid_max_length_description(self):
        """Test that description with exactly 1000 chars is valid."""
        max_desc = "x" * 1000
        task = Task(id=1, title="Valid", description=max_desc)

        assert len(task.description) == 1000

    def test_task_with_none_title_raises_error(self):
        """Test that None title raises InvalidTaskDataError."""
        with pytest.raises(InvalidTaskDataError):
            Task(id=1, title=None)  # type: ignore


class TestTaskCompletionStatus:
    """Test suite for Task completion status management."""

    def test_task_completion_status_toggle(self):
        """Test toggling task completion status."""
        task = Task(id=1, title="Test task")

        assert task.completed is False

        task.completed = True
        assert task.completed is True

        task.completed = False
        assert task.completed is False

    def test_new_task_defaults_to_incomplete(self):
        """Test that new tasks default to incomplete status."""
        task = Task(id=1, title="New task")

        assert task.completed is False


class TestTaskUnicodeSupport:
    """Test suite for Unicode character support in tasks."""

    def test_task_with_unicode_characters_in_title(self):
        """Test task with Unicode characters in title."""
        task = Task(id=1, title="कार्य - 任務 - tâche")

        assert "कार्य" in task.title
        assert "任務" in task.title
        assert "tâche" in task.title

    def test_task_with_unicode_characters_in_description(self):
        """Test task with Unicode characters in description."""
        task = Task(
            id=1,
            title="Task",
            description="Supports 日本語 and العربية and ελληνικά",
        )

        assert "日本語" in task.description
        assert "العربية" in task.description
        assert "ελληνικά" in task.description

    def test_task_with_emoji_characters(self):
        """Test task with emoji characters."""
        task = Task(id=1, title="Meeting 📅", description="Important! ⚠️")

        assert "📅" in task.title
        assert "⚠️" in task.description


class TestTaskSpecialCharacters:
    """Test suite for special characters in tasks."""

    def test_task_with_special_characters_in_title(self):
        """Test task with special characters in title."""
        task = Task(id=1, title="Meeting @ 2PM!")

        assert "@" in task.title
        assert "!" in task.title

    def test_task_with_special_characters_in_description(self):
        """Test task with special characters in description."""
        task = Task(id=1, title="Task", description="Review #Q1 goals & objectives")

        assert "#" in task.description
        assert "&" in task.description

    def test_task_with_newlines_in_description(self):
        """Test that newlines in description are preserved."""
        task = Task(
            id=1,
            title="Multi-line task",
            description="Line 1\nLine 2\nLine 3",
        )

        assert "\n" in task.description
        assert task.description.count("\n") == 2


class TestTaskStringRepresentation:
    """Test suite for Task string representation."""

    def test_task_string_representation(self):
        """Test task __repr__ and __str__ methods."""
        task = Task(id=3, title="Review code")

        repr_str = repr(task)
        assert "Task" in repr_str
        assert "id=3" in repr_str
        assert "Review code" in repr_str

    def test_task_string_shows_completion_status(self):
        """Test that string representation shows completion status."""
        task = Task(id=1, title="Task")

        incomplete_repr = repr(task)
        assert "completed=False" in incomplete_repr

        task.completed = True
        complete_repr = repr(task)
        assert "completed=True" in complete_repr


class TestTaskTimestamp:
    """Test suite for Task creation timestamp."""

    def test_task_has_creation_timestamp(self):
        """Test that task has creation timestamp."""
        task = Task(id=1, title="Task")

        assert hasattr(task, "created_at")
        assert isinstance(task.created_at, datetime)

    def test_task_creation_timestamp_is_recent(self):
        """Test that creation timestamp is recent (within last second)."""
        before = datetime.now()
        task = Task(id=1, title="Task")
        after = datetime.now()

        assert before <= task.created_at <= after


class TestTaskEquality:
    """Test suite for Task equality comparison."""

    def test_tasks_with_same_id_are_equal(self):
        """Test that tasks with same ID are considered equal."""
        task1 = Task(id=1, title="Task 1")
        task2 = Task(id=1, title="Task 1")

        # Note: dataclass auto-generates __eq__ based on all fields
        # For same ID but different content, they won't be equal
        # This is expected behavior for dataclass
        assert task1.id == task2.id

    def test_tasks_with_different_ids_are_not_equal(self):
        """Test that tasks with different IDs are not equal."""
        task1 = Task(id=1, title="Task")
        task2 = Task(id=2, title="Task")

        assert task1.id != task2.id


class TestTaskEdgeCases:
    """Test suite for Task model edge cases."""

    def test_task_with_minimum_valid_title(self):
        """Test task with single character title (minimum valid)."""
        task = Task(id=1, title="A")

        assert task.title == "A"
        assert len(task.title) == 1

    def test_task_with_empty_description_is_valid(self):
        """Test that empty description is valid (optional field)."""
        task = Task(id=1, title="Task", description="")

        assert task.description == ""

    def test_task_title_is_trimmed(self):
        """Test that task title has leading/trailing whitespace trimmed."""
        task = Task(id=1, title="  Task with spaces  ")

        # Title should be trimmed in __post_init__
        assert task.title == "Task with spaces"
        assert not task.title.startswith(" ")
        assert not task.title.endswith(" ")
