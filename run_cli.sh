#!/bin/bash
# CLI Demo Script

echo "============================================================"
echo "  LifeStepsAI | Todo Application - CLI Demo"
echo "============================================================"
echo ""

export PYTHONPATH=/mnt/d/hackathon-robotic/todo-list/src

echo "📝 Adding tasks..."
python3 -m todo_app.cli add "Buy groceries" -d "Milk, eggs, bread"
python3 -m todo_app.cli add "Call mom"
python3 -m todo_app.cli add "Finish project"
echo ""

echo "📋 Listing all tasks..."
python3 -m todo_app.cli list
echo ""

echo "✅ Note: Each command runs independently (in-memory storage resets)"
echo ""
echo "🚀 Try these commands yourself:"
echo "   PYTHONPATH=src python3 -m todo_app.cli add \"Your task\""
echo "   PYTHONPATH=src python3 -m todo_app.cli list"
echo "   PYTHONPATH=src python3 -m todo_app.cli --help"
echo ""
