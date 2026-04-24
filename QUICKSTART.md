# 🚀 Quick Start Guide - PyCompile

## ⚡ 30 Second Setup (Local)

### 1️⃣ Install Backend Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 2️⃣ Start Backend Server
```bash
python main.py
```
✅ Backend runs at: http://localhost:8000

### 3️⃣ Open Frontend in Browser
```bash
# Option A: Open directly
open frontend/index.html

# Option B: Serve with Python
cd frontend
python -m http.server 3000
# Visit http://localhost:3000
```

✅ **That's it! Your compiler is ready to use.**

---

## 🎯 Try These Examples

### Example 1: Hello World
```python
print("Hello, World!")
```

### Example 2: Variables & Math
```python
x = 10
y = 20
print(f"Sum: {x + y}")
print(f"Product: {x * y}")
```

### Example 3: Lists & Loops
```python
numbers = [1, 2, 3, 4, 5]
squared = [n**2 for n in numbers]
print("Squared:", squared)
```

### Example 4: Functions
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print([fibonacci(i) for i in range(10)])
```

### Example 5: String Operations
```python
text = "PyCompile"
print(f"Original: {text}")
print(f"Reversed: {text[::-1]}")
print(f"Uppercase: {text.upper()}")
```

---

## 🌐 Deploy Online (2 Minutes)

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

**TL;DR:**
1. Push code to GitHub
2. Connect to Render.com
3. Deploy (auto in 2 minutes)
4. Get free URL

---

## 📋 Features Showcase

✅ **Code Editor**
- Line numbers
- Tab support
- Copy/paste
- Font size adjustment

✅ **Execution**
- Real-time output
- Error display
- Timeout protection

✅ **History**
- Save executions
- Quick reload
- Browser storage

✅ **Settings**
- Dark/Light theme
- Font size
- Word wrap
- Timeout control

---

## 🔗 API Examples

### Execute Python Code
```bash
curl -X POST http://localhost:8000/api/execute \
  -H "Content-Type: application/json" \
  -d '{"code": "print(\"Hello\")", "timeout": 10}'
```

### Check Syntax
```bash
curl -X POST http://localhost:8000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"code": "print(\"Hello\")"}'
```

### Get Python Info
```bash
curl http://localhost:8000/api/python-version
```

---

## ⚙️ Customization

### Change API URL (for deployment)
Edit `frontend/app.js`:
```javascript
const API_URL = 'https://your-deployed-backend.com/api';
```

### Change Theme Colors
Edit `frontend/styles.css`:
```css
:root {
    --accent: #007acc;  /* Change accent color */
    --success: #6a9955; /* Change success color */
}
```

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| "Cannot connect to API" | Make sure backend is running on port 8000 |
| "Module not found" | Python standard library only - external modules not supported |
| "CORS error" | Update `ALLOWED_ORIGINS` in backend config |
| "Code times out" | Increase timeout in Settings tab (max 30s) |

---

## 📚 Learn More

- [Backend Documentation](backend/README.md)
- [Deployment Guide](DEPLOYMENT.md)
- [Full README](README.md)
- [Project Structure](PROJECT_STRUCTURE.md)

---

## 🎉 Next Steps

1. ✅ Run locally
2. 📝 Customize colors/branding
3. 🚀 Deploy to Render (free)
4. 🌐 Share with friends!

---

**Happy coding! 🐍✨**
