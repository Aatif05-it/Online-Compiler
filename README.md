# Online Compiler - Advanced Python Compiler

🐍 **Online Compiler** is a modern, web-based Python code executor with a beautiful UI and powerful backend.

## 🌟 Features

- **Modern Code Editor**: Syntax highlighting, line numbers, code formatting
- **Real-time Execution**: Run Python code instantly with output display
- **Execution History**: Keep track of all your executed code
- **Dark/Light Theme**: Toggle between themes based on preference
- **Customizable Settings**: Adjust font size, word wrap, and execution timeout
- **Code Analysis**: Syntax checking before execution
- **Python Version Info**: Check Python interpreter details
- **Production Ready**: Deployable to free platforms

## 🚀 Quick Start

### Local Development

#### Backend Setup
```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt
python main.py
```

Backend runs at: `http://localhost:8000`
API Docs: `http://localhost:8000/docs`

#### Frontend Setup
```bash
cd frontend
# Serve with Python
python -m http.server 3000

# Or use Node.js http-server
npx http-server -p 3000
```

Frontend runs at: `http://localhost:3000`

## 📦 Deployment Options

### Option 1: Deploy to Render (Recommended - Free)

1. **Fork or push this project to your own GitHub repository**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Create Render Account** at https://render.com

3. **Deploy Backend:**
   - Click "New +" → "Web Service"
   - Connect your GitHub repo
   - Build Command: `pip install -r backend/requirements.txt`
   - Start Command: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Environment: Set `DEBUG=False`
   - Environment: Set `ALLOWED_ORIGINS=https://your-frontend-name.onrender.com`

4. **Deploy Frontend:**
   - Click "New +" → "Static Site"
   - Connect your GitHub repo
   - Publish directory: `frontend`
   - Update `frontend/config.js` and set `API_URL` to your backend URL, for example: `https://your-backend-name.onrender.com/api`

### Option 2: Deploy to Railway (Free Tier Available)

1. Go to https://railway.app
2. Create new project
3. Select "Deploy from GitHub"
4. Choose backend folder
5. Railway auto-detects Python and deploys

### Option 3: Deploy to PythonAnywhere

1. Go to https://www.pythonanywhere.com
2. Upload your backend folder
3. Configure web app with FastAPI
4. Create SSL certificate

### Option 4: Docker Deployment

```dockerfile
# backend/Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 🔧 API Endpoints

### Health Check
```
GET /health
```

### Execute Code
```
POST /api/execute
{
  "code": "print('Hello, World!')",
  "timeout": 10
}
```

### Analyze Code
```
POST /api/analyze
{
  "code": "print('Hello, World!')"
}
```

### Python Version
```
GET /api/python-version
```

## 🎨 Customization

### Change API URL
In `frontend/config.js`, update:
```javascript
window.RUNTIME_CONFIG = {
   API_URL: 'https://your-backend-url.com/api'
};
```

### Change Theme Colors
In `frontend/styles.css`, modify CSS variables:
```css
:root {
    --primary-bg: #1e1e1e;
    --accent: #007acc;
    /* ... more variables ... */
}
```

## 🔒 Security Features

- Input validation
- Execution timeout protection
- CORS configuration
- Error handling
- No file system access during execution

## 📊 Project Structure

```
Compiler/
├── backend/
│   ├── main.py           # FastAPI app
│   ├── config.py         # Configuration
│   ├── requirements.txt   # Dependencies
│   └── .env.example      # Environment example
├── frontend/
│   ├── index.html        # Main UI
│   ├── styles.css        # Styling
│   ├── app.js            # JavaScript logic
│   └── README.md         # Frontend docs
└── README.md             # This file
```

## 🐛 Troubleshooting

### CORS Error
- Update `ALLOWED_ORIGINS` in backend configuration
- Ensure backend and frontend are on the same domain

### Code Won't Execute
- Check execution timeout isn't exceeded
- Verify Python syntax is correct
- Check backend logs for errors

### Performance Issues
- Reduce timeout value
- Optimize code execution
- Consider caching for frequently used code

## 🤝 Contributing

Feel free to fork, modify, and improve this project!

## 📝 License

MIT License - Use freely for personal and commercial projects

## 🎯 Future Enhancements

- [ ] Multiple file support
- [ ] Code sharing with unique URLs
- [ ] Collaboration features
- [ ] Custom Python packages installation
- [ ] Output formatting and visualization
- [ ] Code snippets library
- [ ] Performance profiling

## 📧 Support

For issues or questions, create an issue in the repository.

---

**Made with ❤️ by Your Khan Aatif** | PyCompile v1.0.0
