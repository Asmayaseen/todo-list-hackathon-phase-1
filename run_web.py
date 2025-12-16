#!/usr/bin/env python3
"""
Script to run the LifeStepsAI Todo Web Application.

This script starts the Flask web server for the beautiful UI.
"""

import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from todo_app.web import create_app

def main():
    """Main entry point to run the web application."""
    print("\n🚀 Starting LifeStepsAI Todo Web Application...")
    print("   Access the beautiful UI at http://localhost:5000")
    print("   Press Ctrl+C to stop the server\n")
    
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == "__main__":
    main()