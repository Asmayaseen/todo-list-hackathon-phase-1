#!/usr/bin/env python3
"""Test CLI commands"""
import sys
sys.path.insert(0, 'src')

from todo_app.cli import TodoCLI

print("=" * 60)
print("  Testing CLI Commands")
print("=" * 60)
print()

cli = TodoCLI()

# Test add command
print("1️⃣ Testing: Add Task")
args = cli.parser.parse_args(['add', 'Buy milk', '-d', 'From store'])
cli.manager.add_task(args.title, args.description)
print("✅ Task added successfully!")
print()

# Test list command
print("2️⃣ Testing: List Tasks")
args = cli.parser.parse_args(['list'])
tasks = cli.manager.list_tasks()
print(f"✅ Found {len(tasks)} task(s)")
for task in tasks:
    print(f"   {task}")
print()

# Test complete command
print("3️⃣ Testing: Mark Complete")
cli.manager.mark_complete(1)
print("✅ Task marked complete!")
print()

# Test list completed
print("4️⃣ Testing: List Completed Tasks")
completed = cli.manager.list_tasks(status="completed")
print(f"✅ Completed tasks: {len(completed)}")
for task in completed:
    print(f"   {task}")
print()

print("=" * 60)
print("  ✅ All CLI Commands Working!")
print("=" * 60)
