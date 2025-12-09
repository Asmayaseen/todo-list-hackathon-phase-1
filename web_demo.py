"""
Demo script for the LifeStepsAI Todo Web Application.

This script demonstrates how to use the web interface programmatically.
"""

from todo_app.web import create_app

def run_web_demo():
    """Run the web application demo."""
    print("🚀 LifeStepsAI Todo Application - Web Interface Demo")
    print("   Starting web server...")
    print("\n💡 Open your browser and navigate to http://localhost:5000")
    print("   to access the beautiful web UI!")
    print("\n🔧 The web interface includes:")
    print("   - Modern, responsive design")
    print("   - Real-time task management")
    print("   - Task statistics and filtering")
    print("   - Smooth animations and visual feedback")
    print("   - Intuitive controls for all task operations")
    print("\n✨ Try these features:")
    print("   1. Add new tasks with titles and descriptions")
    print("   2. Mark tasks as complete/incomplete")
    print("   3. Edit existing tasks")
    print("   4. Delete tasks you no longer need")
    print("   5. Filter tasks by status (all, pending, completed)")
    print("   6. View task statistics")
    
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == "__main__":
    run_web_demo()