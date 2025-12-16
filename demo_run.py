#!/usr/bin/env python3
"""
Demo script to show the Todo App working
"""

import sys
sys.path.insert(0, '/mnt/d/hackathon-robotic/todo-list/src')

from todo_app.manager import TodoManager
from todo_app.exceptions import TaskNotFoundException, InvalidTaskDataError

print("=" * 60)
print("  LifeStepsAI | Todo Application - Demo")
print("=" * 60)
print()

# Create TodoManager instance
manager = TodoManager()

print("📝 Demo 1: Adding Tasks")
print("-" * 60)
task1 = manager.add_task(title="Buy groceries", description="Milk, eggs, bread")
print(f"✅ Added: {task1}")

task2 = manager.add_task(title="Call mom", description="Check in with family")
print(f"✅ Added: {task2}")

task3 = manager.add_task(title="Finish project report")
print(f"✅ Added: {task3}")
print()

print("📋 Demo 2: Viewing All Tasks")
print("-" * 60)
all_tasks = manager.list_tasks()
for task in all_tasks:
    print(f"  {task}")
print(f"Total tasks: {len(all_tasks)}")
print()

print("✓ Demo 3: Marking Task as Complete")
print("-" * 60)
manager.mark_complete(task_id=1)
print(f"✅ Marked complete: Task #{1}")
print()

print("📋 Demo 4: Viewing Pending Tasks")
print("-" * 60)
pending = manager.list_tasks(status="pending")
for task in pending:
    print(f"  {task}")
print(f"Pending tasks: {len(pending)}")
print()

print("📋 Demo 5: Viewing Completed Tasks")
print("-" * 60)
completed = manager.list_tasks(status="completed")
for task in completed:
    print(f"  {task}")
print(f"Completed tasks: {len(completed)}")
print()

print("✏️ Demo 6: Updating a Task")
print("-" * 60)
updated = manager.update_task(task_id=2, title="Call mom tonight", description="Check in with family - evening call")
print(f"✅ Updated: {updated}")
print()

print("🔄 Demo 7: Toggling Task Status")
print("-" * 60)
manager.toggle_complete(task_id=2)
print(f"✅ Toggled: Task #{2} (now complete)")
print()

print("🗑️ Demo 8: Deleting a Task")
print("-" * 60)
manager.delete_task(task_id=3)
print(f"✅ Deleted: Task #{3}")
print()

print("📋 Final: All Remaining Tasks")
print("-" * 60)
final_tasks = manager.list_tasks()
for task in final_tasks:
    print(f"  {task}")
print(f"Total remaining: {len(final_tasks)}")
print()

print("=" * 60)
print("  ✅ Demo Complete! All features working!")
print("=" * 60)
print()

print("🚀 To use the interactive app, run:")
print("   PYTHONPATH=src python3 -m todo_app.ui")
print()
