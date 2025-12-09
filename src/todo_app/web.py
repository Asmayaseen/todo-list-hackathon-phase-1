"""
Web interface for the todo application using Flask.

This module provides a web-based UI for managing tasks with a modern, responsive design.
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
import os

from todo_app.manager import TodoManager
from todo_app.exceptions import InvalidTaskDataError, TaskNotFoundException


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    
    # Enable CORS for API endpoints
    CORS(app)
    
    # Initialize the todo manager
    todo_manager = TodoManager()
    
    @app.route('/')
    def index():
        """Render the main page."""
        return render_template('index.html')
    
    @app.route('/api/tasks', methods=['GET'])
    def get_tasks():
        """Get all tasks."""
        status = request.args.get('status', 'all')
        tasks = todo_manager.list_tasks(status)
        return jsonify([
            {
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'completed': task.completed,
                'created_at': task.created_at.isoformat()
            }
            for task in tasks
        ])
    
    @app.route('/api/tasks', methods=['POST'])
    def add_task():
        """Add a new task."""
        data = request.get_json()
        title = data.get('title', '').strip()
        description = data.get('description', '').strip()
        
        try:
            task = todo_manager.add_task(title=title, description=description)
            return jsonify({
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'completed': task.completed,
                'created_at': task.created_at.isoformat()
            }), 201
        except InvalidTaskDataError as e:
            return jsonify({'error': str(e)}), 400
    
    @app.route('/api/tasks/<int:task_id>', methods=['PUT'])
    def update_task(task_id):
        """Update an existing task."""
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        
        try:
            updated_task = todo_manager.update_task(
                task_id=task_id,
                title=title,
                description=description
            )
            return jsonify({
                'id': updated_task.id,
                'title': updated_task.title,
                'description': updated_task.description,
                'completed': updated_task.completed,
                'created_at': updated_task.created_at.isoformat()
            })
        except TaskNotFoundException as e:
            return jsonify({'error': str(e)}), 404
        except InvalidTaskDataError as e:
            return jsonify({'error': str(e)}), 400
    
    @app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
    def delete_task(task_id):
        """Delete a task."""
        try:
            todo_manager.delete_task(task_id)
            return jsonify({'message': 'Task deleted successfully'}), 200
        except TaskNotFoundException as e:
            return jsonify({'error': str(e)}), 404
    
    @app.route('/api/tasks/<int:task_id>/complete', methods=['PUT'])
    def mark_complete(task_id):
        """Mark a task as complete."""
        try:
            todo_manager.mark_complete(task_id)
            task = todo_manager.get_task(task_id)
            return jsonify({
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'completed': task.completed,
                'created_at': task.created_at.isoformat()
            })
        except TaskNotFoundException as e:
            return jsonify({'error': str(e)}), 404
    
    @app.route('/api/tasks/<int:task_id>/incomplete', methods=['PUT'])
    def mark_incomplete(task_id):
        """Mark a task as incomplete."""
        try:
            todo_manager.mark_incomplete(task_id)
            task = todo_manager.get_task(task_id)
            return jsonify({
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'completed': task.completed,
                'created_at': task.created_at.isoformat()
            })
        except TaskNotFoundException as e:
            return jsonify({'error': str(e)}), 404
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)