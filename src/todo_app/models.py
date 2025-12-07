"""
Task model for the todo application.

This module defines the Task data structure representing a single todo item.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from todo_app.exceptions import InvalidTaskDataError


@dataclass
class Task:
    """
    Represents a single todo task.

    Attributes:
        id: Unique task identifier (positive integer)
        title: Task title (1-200 characters, required)
        description: Task description (0-1000 characters, optional)
        completed: Task completion status (default: False)
        created_at: Creation timestamp (auto-generated)

    Raises:
        InvalidTaskDataError: If task data fails validation

    Examples:
        >>> task = Task(id=1, title="Buy groceries")
        >>> task.title
        'Buy groceries'
        >>> task.completed
        False

        >>> task = Task(id=2, title="Meeting", description="Team standup")
        >>> task.description
        'Team standup'
    """

    id: int
    title: str
    description: str = ""
    completed: bool = False
    created_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self) -> None:
        """
        Validate task data after initialization.

        This method is automatically called by dataclass after __init__.
        It performs validation on title and description.

        Raises:
            InvalidTaskDataError: If validation fails
        """
        # Validate and trim title
        if self.title is None:
            raise InvalidTaskDataError("Title cannot be None")

        # Trim leading/trailing whitespace
        self.title = self.title.strip()

        # Validate title is not empty after trimming
        if not self.title:
            raise InvalidTaskDataError("Title cannot be empty")

        # Validate title length
        if len(self.title) > 200:
            raise InvalidTaskDataError(
                f"Title must be between 1 and 200 characters (got {len(self.title)})"
            )

        # Validate description length (if provided)
        if self.description and len(self.description) > 1000:
            raise InvalidTaskDataError(
                f"Description must be at most 1000 characters (got {len(self.description)})"
            )

        # Convert None description to empty string
        if self.description is None:
            self.description = ""

    def __repr__(self) -> str:
        """
        Return detailed string representation of the task.

        Returns:
            String representation including all task fields

        Examples:
            >>> task = Task(id=1, title="Test")
            >>> repr(task)
            "Task(id=1, title='Test', completed=False)"
        """
        status = "✓" if self.completed else "☐"
        return (
            f"Task(id={self.id}, title='{self.title}', "
            f"completed={self.completed}, status='{status}')"
        )

    def __str__(self) -> str:
        """
        Return user-friendly string representation of the task.

        Returns:
            Formatted string for display

        Examples:
            >>> task = Task(id=1, title="Buy milk")
            >>> str(task)
            '[1] ☐ Buy milk'
        """
        status = "✓" if self.completed else "☐"
        return f"[{self.id}] {status} {self.title}"
