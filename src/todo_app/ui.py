"""
Console user interface for the todo application.

This module provides an interactive command-line interface for managing tasks.
"""

import sys
from typing import Optional

from todo_app.exceptions import InvalidTaskDataError, TaskNotFoundException
from todo_app.manager import TodoManager


class TodoUI:
    """
    Interactive console interface for todo application.

    Provides a menu-driven interface for all task management operations.
    """

    def __init__(self) -> None:
        """Initialize UI with a TodoManager instance."""
        self.manager = TodoManager()
        self.running = True

    def clear_screen(self) -> None:
        """Clear the console screen (works on both Windows and Unix)."""
        import os

        os.system("cls" if os.name == "nt" else "clear")

    def print_header(self, title: str) -> None:
        """
        Print a formatted header.

        Args:
            title: Header title to display
        """
        print("\n" + "=" * 60)
        print(f"  {title}")
        print("=" * 60)

    def print_task(self, task) -> None:
        """
        Print a single task in formatted style.

        Args:
            task: Task object to display
        """
        status = "✓" if task.completed else "☐"
        print(f"\n[{task.id}] {status} {task.title}")
        if task.description:
            print(f"    Description: {task.description}")
        print(f"    Status: {'Completed' if task.completed else 'Pending'}")

    def show_menu(self) -> None:
        """Display the main menu options."""
        self.print_header("LifeStepsAI | Todo Application")
        print("\n📋 Main Menu:")
        print("  1. Add new task")
        print("  2. View all tasks")
        print("  3. View pending tasks")
        print("  4. View completed tasks")
        print("  5. Update task")
        print("  6. Mark task as complete")
        print("  7. Mark task as incomplete")
        print("  8. Delete task")
        print("  9. Exit")
        print("\n" + "-" * 60)

    def get_input(self, prompt: str, required: bool = True) -> Optional[str]:
        """
        Get user input with optional validation.

        Args:
            prompt: Prompt to display to user
            required: Whether input is required (default: True)

        Returns:
            User input string or None if not required and empty
        """
        while True:
            value = input(prompt).strip()
            if not value and required:
                print("❌ This field is required. Please try again.")
                continue
            return value if value else None

    def add_task_menu(self) -> None:
        """Handle adding a new task."""
        self.print_header("Add New Task")

        title = self.get_input("Enter task title: ", required=True)
        assert title is not None  # For type checker

        description = self.get_input(
            "Enter description (optional, press Enter to skip): ", required=False
        )

        try:
            task = self.manager.add_task(
                title=title, description=description or ""
            )
            print("\n✅ Task added successfully!")
            self.print_task(task)
        except InvalidTaskDataError as e:
            print(f"\n❌ Error: {e}")

        input("\nPress Enter to continue...")

    def view_tasks_menu(self, status: str = "all") -> None:
        """
        Handle viewing tasks with optional status filter.

        Args:
            status: Filter status ("all", "pending", or "completed")
        """
        status_names = {
            "all": "All Tasks",
            "pending": "Pending Tasks",
            "completed": "Completed Tasks",
        }
        self.print_header(status_names.get(status, "All Tasks"))

        tasks = self.manager.list_tasks(status=status)

        if not tasks:
            print("\n📭 No tasks found.")
        else:
            for task in tasks:
                self.print_task(task)

            # Show summary
            total = len(tasks)
            if status == "all":
                completed = len([t for t in tasks if t.completed])
                pending = total - completed
                print(f"\n📊 Total: {total} tasks ({completed} completed, {pending} pending)")
            else:
                print(f"\n📊 Total: {total} {status} tasks")

        input("\nPress Enter to continue...")

    def update_task_menu(self) -> None:
        """Handle updating an existing task."""
        self.print_header("Update Task")

        # Show current tasks
        tasks = self.manager.list_tasks()
        if not tasks:
            print("\n📭 No tasks to update.")
            input("\nPress Enter to continue...")
            return

        print("\nCurrent tasks:")
        for task in tasks:
            print(f"  [{task.id}] {task.title}")

        try:
            task_id_str = self.get_input("\nEnter task ID to update: ", required=True)
            assert task_id_str is not None
            task_id = int(task_id_str)

            # Get current task
            task = self.manager.get_task(task_id)

            print(f"\nCurrent title: {task.title}")
            new_title = self.get_input(
                "Enter new title (or press Enter to keep current): ", required=False
            )

            print(f"Current description: {task.description or '(empty)'}")
            new_description = self.get_input(
                "Enter new description (or press Enter to keep current): ",
                required=False,
            )

            # Update task
            self.manager.update_task(
                task_id=task_id, title=new_title, description=new_description
            )

            print("\n✅ Task updated successfully!")
            updated_task = self.manager.get_task(task_id)
            self.print_task(updated_task)

        except ValueError:
            print("\n❌ Error: Invalid task ID. Please enter a number.")
        except TaskNotFoundException as e:
            print(f"\n❌ Error: {e}")
        except InvalidTaskDataError as e:
            print(f"\n❌ Error: {e}")

        input("\nPress Enter to continue...")

    def mark_complete_menu(self) -> None:
        """Handle marking a task as complete."""
        self.print_header("Mark Task as Complete")

        # Show pending tasks
        tasks = self.manager.list_tasks(status="pending")
        if not tasks:
            print("\n✅ No pending tasks! All done!")
            input("\nPress Enter to continue...")
            return

        print("\nPending tasks:")
        for task in tasks:
            print(f"  [{task.id}] {task.title}")

        try:
            task_id_str = self.get_input("\nEnter task ID to mark complete: ", required=True)
            assert task_id_str is not None
            task_id = int(task_id_str)

            self.manager.mark_complete(task_id=task_id)
            task = self.manager.get_task(task_id)

            print("\n✅ Task marked as complete!")
            self.print_task(task)

        except ValueError:
            print("\n❌ Error: Invalid task ID. Please enter a number.")
        except TaskNotFoundException as e:
            print(f"\n❌ Error: {e}")

        input("\nPress Enter to continue...")

    def mark_incomplete_menu(self) -> None:
        """Handle marking a task as incomplete."""
        self.print_header("Mark Task as Incomplete")

        # Show completed tasks
        tasks = self.manager.list_tasks(status="completed")
        if not tasks:
            print("\n📋 No completed tasks to mark as incomplete.")
            input("\nPress Enter to continue...")
            return

        print("\nCompleted tasks:")
        for task in tasks:
            print(f"  [{task.id}] {task.title}")

        try:
            task_id_str = self.get_input(
                "\nEnter task ID to mark incomplete: ", required=True
            )
            assert task_id_str is not None
            task_id = int(task_id_str)

            self.manager.mark_incomplete(task_id=task_id)
            task = self.manager.get_task(task_id)

            print("\n✅ Task marked as incomplete!")
            self.print_task(task)

        except ValueError:
            print("\n❌ Error: Invalid task ID. Please enter a number.")
        except TaskNotFoundException as e:
            print(f"\n❌ Error: {e}")

        input("\nPress Enter to continue...")

    def delete_task_menu(self) -> None:
        """Handle deleting a task."""
        self.print_header("Delete Task")

        # Show current tasks
        tasks = self.manager.list_tasks()
        if not tasks:
            print("\n📭 No tasks to delete.")
            input("\nPress Enter to continue...")
            return

        print("\nCurrent tasks:")
        for task in tasks:
            status = "✓" if task.completed else "☐"
            print(f"  [{task.id}] {status} {task.title}")

        try:
            task_id_str = self.get_input("\nEnter task ID to delete: ", required=True)
            assert task_id_str is not None
            task_id = int(task_id_str)

            # Get task before deleting (for confirmation)
            task = self.manager.get_task(task_id)

            # Confirm deletion
            confirm = self.get_input(
                f"\n⚠️  Delete '{task.title}'? (y/n): ", required=True
            )

            if confirm and confirm.lower() == "y":
                self.manager.delete_task(task_id=task_id)
                print(f"\n✅ Task '{task.title}' (ID: {task_id}) deleted successfully!")
            else:
                print("\n❌ Deletion cancelled.")

        except ValueError:
            print("\n❌ Error: Invalid task ID. Please enter a number.")
        except TaskNotFoundException as e:
            print(f"\n❌ Error: {e}")

        input("\nPress Enter to continue...")

    def run(self) -> None:
        """Run the main application loop."""
        print("\n🚀 Welcome to LifeStepsAI Todo Application!")
        print("   Phase I: In-Memory Python Console App")
        input("\nPress Enter to start...")

        while self.running:
            self.clear_screen()
            self.show_menu()

            choice = input("Enter your choice (1-9): ").strip()

            if choice == "1":
                self.add_task_menu()
            elif choice == "2":
                self.view_tasks_menu(status="all")
            elif choice == "3":
                self.view_tasks_menu(status="pending")
            elif choice == "4":
                self.view_tasks_menu(status="completed")
            elif choice == "5":
                self.update_task_menu()
            elif choice == "6":
                self.mark_complete_menu()
            elif choice == "7":
                self.mark_incomplete_menu()
            elif choice == "8":
                self.delete_task_menu()
            elif choice == "9":
                self.running = False
                print("\n👋 Thank you for using LifeStepsAI Todo App!")
                print("   All tasks are stored in-memory and will be lost on exit.")
                print("   Good bye! 🚀\n")
            else:
                print("\n❌ Invalid choice. Please enter a number between 1-9.")
                input("Press Enter to continue...")


def main() -> None:
    """Main entry point for the application."""
    try:
        ui = TodoUI()
        ui.run()
    except KeyboardInterrupt:
        print("\n\n👋 Application interrupted. Goodbye! 🚀\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
        print("Please report this issue if it persists.\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
