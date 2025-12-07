"""
LifeStepsAI Todo Application - In-Memory Python Console App

A simple, clean todo list application built with Spec-Driven Development (SDD)
and Test-Driven Development (TDD) principles.

Phase I: In-memory storage with console interface
"""

__version__ = "1.0.0"
__author__ = "Your Name"

from todo_app.exceptions import InvalidTaskDataError, TaskNotFoundException
from todo_app.models import Task
from todo_app.manager import TodoManager

__all__ = [
    "Task",
    "TodoManager",
    "InvalidTaskDataError",
    "TaskNotFoundException",
]
