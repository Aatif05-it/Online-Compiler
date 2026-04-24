#!/bin/bash
# PyCompile Setup & Run Script

echo "🐍 PyCompile - Python Compiler Setup"
echo "===================================="
echo ""

# Check Python
echo "✓ Checking Python installation..."
python --version

# Install dependencies
echo ""
echo "✓ Installing backend dependencies..."
cd backend
pip install -r requirements.txt -q

# Start backend
echo ""
echo "✓ Starting backend server..."
echo "  Backend will run at: http://localhost:8000"
echo ""
cd ..

# Create a simple startup command
echo "📝 Commands to run:"
echo ""
echo "1. Start Backend (in one terminal):"
echo "   cd backend"
echo "   python main.py"
echo ""
echo "2. Open Frontend (in another terminal):"
echo "   cd frontend"
echo "   python -m http.server 3000"
echo ""
echo "3. Visit in browser:"
echo "   http://localhost:3000"
echo ""
echo "✅ Setup complete! Follow the commands above."
