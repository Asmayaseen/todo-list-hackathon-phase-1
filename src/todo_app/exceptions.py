"""
Custom exceptions for the todo application.

This module defines application-specific exceptions for clear error handling.
"""


class InvalidTaskDataError(Exception):
    """
    Raised when task data fails validation.

    Examples:
        - Empty task title
        - Title exceeds 200 characters
        - Description exceeds 1000 characters
        - Invalid task ID
    """

    pass


class TaskNotFoundException(Exception):
    """
    Raised when attempting to access a task that doesn't exist.

    Examples:
        - Deleting a non-existent task ID
        - Updating a non-existent task ID
        - Marking a non-existent task as complete
    """

    pass
