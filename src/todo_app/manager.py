"""
TodoManager class for managing todo tasks.

This module provides the core CRUD operations for managing tasks in-memory.
"""

from typing import Optional

from todo_app.exceptions import InvalidTaskDataError, TaskNotFoundException
from todo_app.models import Task


class TodoManager:
    """
    Manages in-memory todo tasks with CRUD operations.

    The TodoManager provides methods to create, read, update, and delete tasks.
    All tasks are stored in-memory and will be lost when the application terminates.

    Attributes:
        tasks: Dictionary mapping task IDs to Task objects
        _next_id: Counter for generating unique task IDs

    Examples:
        >>> manager = TodoManager()
        >>> task = manager.add_task(title="Buy milk")
        >>> task.id
        1
        >>> len(manager.list_tasks())
        1
    """

    def __init__(self) -> None:
        """Initialize TodoManager with empty task dictionary and ID counter."""
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

        Examples:
            >>> manager = TodoManager()
            >>> task = manager.add_task(title="Buy groceries")
            >>> task.title
            'Buy groceries'
            >>> task.id
            1
        """
        # Validation happens in Task.__post_init__()
        task = Task(
            id=self._next_id,
            title=title,  # Will be trimmed in Task.__post_init__
            description=description,
        )

        self.tasks[task.id] = task
        self._next_id += 1

        return task

    def list_tasks(self, status: str = "all") -> list[Task]:
        """
        List tasks with optional status filter.

        Args:
            status: Filter by status - "all", "pending", or "completed".
                   Default is "all"

        Returns:
            List of Task objects matching the filter, ordered by creation (ID)

        Raises:
            ValueError: If status is not one of the valid options

        Examples:
            >>> manager = TodoManager()
            >>> task1 = manager.add_task(title="Task 1")
            >>> task2 = manager.add_task(title="Task 2")
            >>> manager.mark_complete(task_id=task1.id)
            >>> len(manager.list_tasks(status="all"))
            2
            >>> len(manager.list_tasks(status="pending"))
            1
        """
        valid_statuses = ["all", "pending", "completed"]
        if status not in valid_statuses:
            raise ValueError(
                f"Invalid status '{status}'. Must be one of: {', '.join(valid_statuses)}"
            )

        if status == "all":
            return list(self.tasks.values())
        elif status == "pending":
            return [task for task in self.tasks.values() if not task.completed]
        else:  # status == "completed"
            return [task for task in self.tasks.values() if task.completed]

    def get_task(self, task_id: int) -> Task:
        """
        Get a single task by ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The Task object

        Raises:
            TaskNotFoundException: If task_id doesn't exist

        Examples:
            >>> manager = TodoManager()
            >>> task = manager.add_task(title="Test")
            >>> retrieved = manager.get_task(task_id=task.id)
            >>> retrieved.title
            'Test'
        """
        if task_id not in self.tasks:
            raise TaskNotFoundException(f"Task with ID {task_id} not found")

        return self.tasks[task_id]

    def delete_task(self, task_id: int) -> None:
        """
        Delete a task by ID.

        Args:
            task_id: The ID of the task to delete

        Raises:
            TaskNotFoundException: If task_id doesn't exist

        Examples:
            >>> manager = TodoManager()
            >>> task = manager.add_task(title="To delete")
            >>> manager.delete_task(task_id=task.id)
            >>> len(manager.list_tasks())
            0
        """
        if task_id not in self.tasks:
            raise TaskNotFoundException(f"Task with ID {task_id} not found")

        del self.tasks[task_id]

    def update_task(
        self,
        task_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None,
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

        Examples:
            >>> manager = TodoManager()
            >>> task = manager.add_task(title="Old title")
            >>> updated = manager.update_task(task_id=task.id, title="New title")
            >>> updated.title
            'New title'
        """
        if task_id not in self.tasks:
            raise TaskNotFoundException(f"Task with ID {task_id} not found")

        task = self.tasks[task_id]

        # Update title if provided
        if title is not None:
            # Create a temporary task to validate the new title
            # This leverages Task.__post_init__ validation
            temp_task = Task(
                id=task.id,
                title=title,
                description=task.description,
                completed=task.completed,
            )
            task.title = temp_task.title  # Use the validated and trimmed title

        # Update description if provided
        if description is not None:
            # Validate description length
            if len(description) > 1000:
                raise InvalidTaskDataError(
                    f"Description must be at most 1000 characters (got {len(description)})"
                )
            task.description = description

        return task

    def mark_complete(self, task_id: int) -> None:
        """
        Mark a task as complete.

        Args:
            task_id: The ID of the task to mark complete

        Raises:
            TaskNotFoundException: If task_id doesn't exist

        Examples:
            >>> manager = TodoManager()
            >>> task = manager.add_task(title="Task")
            >>> manager.mark_complete(task_id=task.id)
            >>> manager.get_task(task.id).completed
            True
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

        Examples:
            >>> manager = TodoManager()
            >>> task = manager.add_task(title="Task")
            >>> manager.mark_complete(task_id=task.id)
            >>> manager.mark_incomplete(task_id=task.id)
            >>> manager.get_task(task.id).completed
            False
        """
        if task_id not in self.tasks:
            raise TaskNotFoundException(f"Task with ID {task_id} not found")

        self.tasks[task_id].completed = False

    def toggle_complete(self, task_id: int) -> None:
        """
        Toggle task completion status.

        If task is complete, mark it incomplete. If incomplete, mark it complete.

        Args:
            task_id: The ID of the task to toggle

        Raises:
            TaskNotFoundException: If task_id doesn't exist

        Examples:
            >>> manager = TodoManager()
            >>> task = manager.add_task(title="Task")
            >>> manager.toggle_complete(task_id=task.id)  # False -> True
            >>> manager.get_task(task.id).completed
            True
            >>> manager.toggle_complete(task_id=task.id)  # True -> False
            >>> manager.get_task(task.id).completed
            False
        """
        if task_id not in self.tasks:
            raise TaskNotFoundException(f"Task with ID {task_id} not found")

        task = self.tasks[task_id]
        task.completed = not task.completed
