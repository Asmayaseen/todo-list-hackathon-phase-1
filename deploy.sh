#!/bin/bash
# Quick Deployment Script for Todo List Application

set -e  # Exit on error

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║        🚀 Todo List App - Quick Deploy Script 🚀            ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Function to print colored output
print_success() {
    echo "✅ $1"
}

print_info() {
    echo "ℹ️  $1"
}

print_error() {
    echo "❌ $1"
}

# Check if we're in the right directory
if [ ! -f "pyproject.toml" ]; then
    print_error "Please run this script from the todo-list directory!"
    exit 1
fi

print_success "Found project files"

# Menu
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Select deployment option:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "1. 🐳 Docker (Local)"
echo "2. 🌐 Render (Cloud - Free)"
echo "3. 🟣 Heroku (Cloud)"
echo "4. 💻 Local Python (Development)"
echo "5. 📋 Show all deployment options"
echo ""
read -p "Enter choice (1-5): " choice

case $choice in
    1)
        echo ""
        print_info "Building Docker image..."
        docker build -t todo-list-app .

        print_success "Docker image built!"
        print_info "Starting container..."

        docker run -d -p 5000:5000 --name todo-list todo-list-app

        print_success "Container started!"
        echo ""
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo "🎉 App is running!"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo ""
        echo "🌐 Web UI: http://localhost:5000"
        echo ""
        echo "To stop: docker stop todo-list"
        echo "To remove: docker rm todo-list"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        ;;

    2)
        echo ""
        print_info "Render Deployment Instructions:"
        echo ""
        echo "1. Go to: https://dashboard.render.com"
        echo "2. Click 'New +' → 'Web Service'"
        echo "3. Connect repository: Asmayaseen/todo-list-hackathon-phase-1"
        echo "4. Branch: main"
        echo "5. Render will auto-detect render.yaml"
        echo "6. Click 'Create Web Service'"
        echo ""
        print_success "Render will build and deploy automatically!"
        echo ""
        echo "Your app will be live at:"
        echo "https://todo-list-hackathon-phase-1.onrender.com"
        echo ""
        read -p "Press Enter to open Render dashboard..."

        # Try to open browser
        if command -v xdg-open &> /dev/null; then
            xdg-open "https://dashboard.render.com" 2>/dev/null || true
        elif command -v open &> /dev/null; then
            open "https://dashboard.render.com" 2>/dev/null || true
        fi
        ;;

    3)
        echo ""
        print_info "Deploying to Heroku..."

        # Check if Heroku CLI is installed
        if ! command -v heroku &> /dev/null; then
            print_error "Heroku CLI not found!"
            echo ""
            echo "Install Heroku CLI:"
            echo "curl https://cli-assets.heroku.com/install.sh | sh"
            exit 1
        fi

        print_info "Creating Heroku app..."
        heroku create todo-list-cli-$(date +%s) || true

        print_info "Pushing to Heroku..."
        git push heroku main

        print_success "Deployed to Heroku!"
        heroku open
        ;;

    4)
        echo ""
        print_info "Setting up local development environment..."

        # Check if virtual environment exists
        if [ ! -d ".venv" ]; then
            print_info "Creating virtual environment..."
            python3 -m venv .venv
        fi

        print_info "Activating virtual environment..."
        source .venv/bin/activate

        print_info "Installing dependencies..."
        pip install -e ".[dev]" --quiet

        print_success "Installation complete!"
        echo ""
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo "🎉 Development environment ready!"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo ""
        echo "Available commands:"
        echo "  todo add 'Task'        - Add task via CLI"
        echo "  todo list              - List tasks"
        echo "  todo-interactive       - Interactive menu UI"
        echo "  todo-web               - Start web server"
        echo ""
        echo "To start web server:"
        echo "  python -m todo_app.web"
        echo ""
        echo "Then visit: http://localhost:5000"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

        # Ask if they want to start web server
        read -p "Start web server now? (y/n): " start_web
        if [ "$start_web" = "y" ]; then
            print_info "Starting web server..."
            python -m todo_app.web
        fi
        ;;

    5)
        echo ""
        cat DEPLOYMENT_INSTRUCTIONS.md
        ;;

    *)
        print_error "Invalid choice!"
        exit 1
        ;;
esac

echo ""
print_success "Done!"
