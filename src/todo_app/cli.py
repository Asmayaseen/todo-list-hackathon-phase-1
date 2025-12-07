"""
Command-line interface for the todo application.

This module provides a CLI for managing tasks via command-line arguments.
"""

import argparse
import sys
from typing import Optional

from todo_app.exceptions import InvalidTaskDataError, TaskNotFoundException
from todo_app.manager import TodoManager


class TodoCLI:
    """
    Command-line interface for todo application.

    Provides command-line arguments for all task management operations.
    """

    def __init__(self) -> None:
        """Initialize CLI with a TodoManager instance."""
        self.manager = TodoManager()
        self.parser = self._create_parser()

    def _create_parser(self) -> argparse.ArgumentParser:
        """
        Create argument parser with all subcommands.

        Returns:
            Configured ArgumentParser instance
        """
        parser = argparse.ArgumentParser(
            prog="todo",
            description="LifeStepsAI Todo Application - CLI Interface",
            epilog="Phase I: In-Memory Python Console App",
        )

        subparsers = parser.add_subparsers(dest="command", help="Available commands")

        # Add task command
        add_parser = subparsers.add_parser("add", help="Add a new task")
        add_parser.add_argument("title", help="Task title")
        add_parser.add_argument(
            "-d", "--description", default="", help="Task description (optional)"
        )

        # List tasks command
        list_parser = subparsers.add_parser("list", help="List tasks")
        list_parser.add_argument(
            "-s",
            "--status",
            choices=["all", "pending", "completed"],
            default="all",
            help="Filter tasks by status (default: all)",
        )

        # Get task command
        get_parser = subparsers.add_parser("get", help="Get a specific task")
        get_parser.add_argument("id", type=int, help="Task ID")

        # Update task command
        update_parser = subparsers.add_parser("update", help="Update a task")
        update_parser.add_argument("id", type=int, help="Task ID")
        update_parser.add_argument("-t", "--title", help="New task title")
        update_parser.add_argument("-d", "--description", help="New task description")

        # Complete task command
        complete_parser = subparsers.add_parser(
            "complete", help="Mark task as complete"
        )
        complete_parser.add_argument("id", type=int, help="Task ID")

        # Incomplete task command
        incomplete_parser = subparsers.add_parser(
            "incomplete", help="Mark task as incomplete"
        )
        incomplete_parser.add_argument("id", type=int, help="Task ID")

        # Toggle task command
        toggle_parser = subparsers.add_parser(
            "toggle", help="Toggle task completion status"
        )
        toggle_parser.add_argument("id", type=int, help="Task ID")

        # Delete task command
        delete_parser = subparsers.add_parser("delete", help="Delete a task")
        delete_parser.add_argument("id", type=int, help="Task ID")

        return parser

    def print_task(self, task) -> None:
        """
        Print a single task in formatted style.

        Args:
            task: Task object to display
        """
        status = "✓" if task.completed else "☐"
        print(f"[{task.id}] {status} {task.title}")
        if task.description:
            print(f"    Description: {task.description}")
        print(f"    Status: {'Completed' if task.completed else 'Pending'}")

    def cmd_add(self, args: argparse.Namespace) -> None:
        """
        Handle add command.

        Args:
            args: Parsed command-line arguments
        """
        try:
            task = self.manager.add_task(title=args.title, description=args.description)
            print("✅ Task added successfully!")
            self.print_task(task)
        except InvalidTaskDataError as e:
            print(f"❌ Error: {e}", file=sys.stderr)
            sys.exit(1)

    def cmd_list(self, args: argparse.Namespace) -> None:
        """
        Handle list command.

        Args:
            args: Parsed command-line arguments
        """
        tasks = self.manager.list_tasks(status=args.status)

        if not tasks:
            print(f"📭 No {args.status} tasks found.")
            return

        status_names = {
            "all": "All Tasks",
            "pending": "Pending Tasks",
            "completed": "Completed Tasks",
        }
        print(f"\n{status_names[args.status]}:")
        print("=" * 60)

        for task in tasks:
            status = "✓" if task.completed else "☐"
            print(f"[{task.id}] {status} {task.title}")
            if task.description:
                print(f"    {task.description}")

        # Show summary
        total = len(tasks)
        if args.status == "all":
            completed = len([t for t in tasks if t.completed])
            pending = total - completed
            print(f"\n📊 Total: {total} tasks ({completed} completed, {pending} pending)")
        else:
            print(f"\n📊 Total: {total} {args.status} tasks")

    def cmd_get(self, args: argparse.Namespace) -> None:
        """
        Handle get command.

        Args:
            args: Parsed command-line arguments
        """
        try:
            task = self.manager.get_task(task_id=args.id)
            self.print_task(task)
        except TaskNotFoundException as e:
            print(f"❌ Error: {e}", file=sys.stderr)
            sys.exit(1)

    def cmd_update(self, args: argparse.Namespace) -> None:
        """
        Handle update command.

        Args:
            args: Parsed command-line arguments
        """
        if not args.title and not args.description:
            print(
                "❌ Error: At least one of --title or --description must be provided",
                file=sys.stderr,
            )
            sys.exit(1)

        try:
            self.manager.update_task(
                task_id=args.id, title=args.title, description=args.description
            )
            print("✅ Task updated successfully!")
            task = self.manager.get_task(task_id=args.id)
            self.print_task(task)
        except (TaskNotFoundException, InvalidTaskDataError) as e:
            print(f"❌ Error: {e}", file=sys.stderr)
            sys.exit(1)

    def cmd_complete(self, args: argparse.Namespace) -> None:
        """
        Handle complete command.

        Args:
            args: Parsed command-line arguments
        """
        try:
            self.manager.mark_complete(task_id=args.id)
            print("✅ Task marked as complete!")
            task = self.manager.get_task(task_id=args.id)
            self.print_task(task)
        except TaskNotFoundException as e:
            print(f"❌ Error: {e}", file=sys.stderr)
            sys.exit(1)

    def cmd_incomplete(self, args: argparse.Namespace) -> None:
        """
        Handle incomplete command.

        Args:
            args: Parsed command-line arguments
        """
        try:
            self.manager.mark_incomplete(task_id=args.id)
            print("✅ Task marked as incomplete!")
            task = self.manager.get_task(task_id=args.id)
            self.print_task(task)
        except TaskNotFoundException as e:
            print(f"❌ Error: {e}", file=sys.stderr)
            sys.exit(1)

    def cmd_toggle(self, args: argparse.Namespace) -> None:
        """
        Handle toggle command.

        Args:
            args: Parsed command-line arguments
        """
        try:
            self.manager.toggle_complete(task_id=args.id)
            task = self.manager.get_task(task_id=args.id)
            status = "complete" if task.completed else "incomplete"
            print(f"✅ Task toggled to {status}!")
            self.print_task(task)
        except TaskNotFoundException as e:
            print(f"❌ Error: {e}", file=sys.stderr)
            sys.exit(1)

    def cmd_delete(self, args: argparse.Namespace) -> None:
        """
        Handle delete command.

        Args:
            args: Parsed command-line arguments
        """
        try:
            task = self.manager.get_task(task_id=args.id)
            self.manager.delete_task(task_id=args.id)
            print(f"✅ Task '{task.title}' (ID: {args.id}) deleted successfully!")
        except TaskNotFoundException as e:
            print(f"❌ Error: {e}", file=sys.stderr)
            sys.exit(1)

    def run(self, argv: Optional[list[str]] = None) -> None:
        """
        Run the CLI application.

        Args:
            argv: Command-line arguments (default: sys.argv[1:])
        """
        args = self.parser.parse_args(argv)

        if not args.command:
            self.parser.print_help()
            sys.exit(0)

        # Map commands to handler methods
        command_handlers = {
            "add": self.cmd_add,
            "list": self.cmd_list,
            "get": self.cmd_get,
            "update": self.cmd_update,
            "complete": self.cmd_complete,
            "incomplete": self.cmd_incomplete,
            "toggle": self.cmd_toggle,
            "delete": self.cmd_delete,
        }

        handler = command_handlers.get(args.command)
        if handler:
            handler(args)
        else:
            print(f"❌ Unknown command: {args.command}", file=sys.stderr)
            self.parser.print_help()
            sys.exit(1)


def main() -> None:
    """Main entry point for the CLI application."""
    try:
        cli = TodoCLI()
        cli.run()
    except KeyboardInterrupt:
        print("\n\n👋 Application interrupted. Goodbye! 🚀\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}", file=sys.stderr)
        print("Please report this issue if it persists.\n", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
