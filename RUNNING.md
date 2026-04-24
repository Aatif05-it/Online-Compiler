# PyCompile Complete Setup Guide

## 🎯 What You Just Built

**Advanced Python Compiler** - A modern, web-based IDE for executing Python code online with:
- ✨ Beautiful dark/light theme UI
- ⚡ Real-time code execution
- 📚 Execution history
- ⚙️ Advanced settings
- 🚀 Production-ready backend

---

## 🏃 Quick Run (Windows)

### Terminal 1: Start Backend
```bash
cd backend
python main.py
```
✅ Runs at: http://localhost:8000

### Terminal 2: Start Frontend
```bash
cd frontend
python -m http.server 3000
```
✅ Runs at: http://localhost:3000

### 3. Open in Browser
Visit: **http://localhost:3000**

---

## 📁 Project Structure

```
Compiler/
├── backend/              # FastAPI server
│   ├── main.py          # REST API endpoints
│   ├── requirements.txt  # Dependencies
│   └── .env.example     # Configuration
├── frontend/            # Web interface
│   ├── index.html       # UI
│   ├── styles.css       # Styling
│   └── app.js          # Logic
└── Documentation files
```

---

## 🌐 Deployment to Internet (FREE)

### Quick Render Deployment (2 minutes)

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "PyCompile"
   git push origin main
   ```

2. **Go to** https://render.com and sign up

3. **Deploy Backend:**
   - New Web Service
   - Build: `pip install -r backend/requirements.txt`
   - Start: `cd backend && uvicorn main:app --host 0.0.0.0`
   - Get your URL (e.g., https://pycompile-xyz.onrender.com)

4. **Update Frontend:**
   - Edit `frontend/app.js`
   - Change: `const API_URL = 'http://localhost:8000/api'`
   - To: `const API_URL = 'https://pycompile-xyz.onrender.com/api'`

5. **Deploy Frontend:**
   - New Static Site
   - Publish directory: `frontend`
   - Done! ✅

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed steps.

---

## 🎨 Features

### Frontend
✅ Syntax highlighting
✅ Line numbers
✅ Dark/Light theme
✅ Font size control
✅ Word wrap
✅ Execution history
✅ Custom timeout
✅ Beautiful UI

### Backend
✅ Code execution
✅ Syntax analysis
✅ Error handling
✅ Timeout protection
✅ REST API
✅ Auto-documentation

---

## 🔗 API Endpoints

```bash
# Execute code
curl -X POST http://localhost:8000/api/execute \
  -H "Content-Type: application/json" \
  -d '{"code":"print(1+1)","timeout":10}'

# Check syntax
curl -X POST http://localhost:8000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"code":"print(1+1)"}'

# API docs
http://localhost:8000/docs
```

---

## 🎨 Customization Ideas

1. **Change Colors**
   - Edit `frontend/styles.css` `:root` variables

2. **Change Logo**
   - Edit `frontend/index.html` - change 🐍 emoji

3. **Add Features**
   - Export code as files
   - Share code via links
   - Collaborative editing
   - Package installation

4. **Branding**
   - Update title, colors, logo
   - Add your domain
   - Custom email alerts

---

## 🚀 Next Steps

1. ✅ Test locally (you're here!)
2. 📝 Customize branding
3. 🌐 Deploy to Render (free)
4. 📢 Share with friends
5. 🎯 Add more features

---

## 📊 API Documentation

### Automatic Docs
When backend runs, visit: **http://localhost:8000/docs**

Interactive Swagger UI with all endpoints!

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Port 8000 in use | Change port in `main.py` |
| CORS Error | Update `API_URL` in `app.js` |
| Module not found | Check backend started |
| Timeout | Increase timeout in settings |

---

## 💡 Pro Tips

1. **Code Sharing**: Copy code URL and share
2. **History**: Click history items to restore code
3. **Keyboard**: Ctrl+Enter to run code
4. **Export**: Copy output to clipboard
5. **Performance**: Use execution history for repeated tasks

---

## 🎓 Learning Resources

- [Backend Docs](backend/README.md)
- [Frontend Docs](frontend/README.md)
- [Deployment Guide](DEPLOYMENT.md)
- [Quick Start](QUICKSTART.md)

---

## 📧 Questions?

Check the README files in each folder for detailed documentation.

---

**🎉 You're all set! Start coding!**

Frontend: http://localhost:3000
Backend: http://localhost:8000
API Docs: http://localhost:8000/docs
