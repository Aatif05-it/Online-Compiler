# Backend Documentation

## 🔧 FastAPI Application

### Setup & Installation

```bash
# Create virtual environment
python -m venv venv

# Activate
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run server
python main.py
# Or with uvicorn directly:
uvicorn main:app --reload
```

### API Endpoints

#### 1. Health Check
```
GET /health
```
**Response:**
```json
{
  "status": "healthy",
  "version": "1.0.0"
}
```

#### 2. Execute Python Code
```
POST /api/execute
Content-Type: application/json

{
  "code": "print('Hello, World!')",
  "timeout": 10
}
```

**Response (Success):**
```json
{
  "success": true,
  "output": "Hello, World!\n",
  "error": null,
  "execution_time": 0.05
}
```

**Response (Error):**
```json
{
  "success": false,
  "output": null,
  "error": "ZeroDivisionError: division by zero",
  "execution_time": null
}
```

#### 3. Analyze Code Syntax
```
POST /api/analyze
Content-Type: application/json

{
  "code": "print('Hello')"
}
```

**Response (Valid):**
```json
{
  "valid": true,
  "message": "Code syntax is valid"
}
```

**Response (Invalid):**
```json
{
  "valid": false,
  "error": "SyntaxError: invalid syntax",
  "line": 1,
  "offset": 5
}
```

#### 4. Get Python Version
```
GET /api/python-version
```

**Response:**
```json
{
  "version": "3.11.0 (main, Oct 24 2022, ...)",
  "version_info": {
    "major": 3,
    "minor": 11,
    "micro": 0
  },
  "platform": "win32",
  "executable": "C:\\Python\\python.exe"
}
```

#### 5. API Info
```
GET /api/info
```

**Response:**
```json
{
  "name": "PyCompile",
  "version": "1.0.0",
  "description": "Advanced Python Code Executor API",
  "python_version": "3.11.0",
  "max_timeout": 30
}
```

---

## 🔐 Security Features

1. **Execution Timeout**: Max 30 seconds per execution
2. **Input Validation**: All inputs validated
3. **Error Handling**: Safe error messages
4. **CORS Protection**: Configurable origins
5. **Resource Limits**: CPU and memory protected

---

## ⚙️ Configuration

Edit `.env` file:
```env
HOST=0.0.0.0
PORT=8000
DEBUG=False
ALLOWED_ORIGINS=*,yourdomain.com
MAX_TIMEOUT=30
```

---

## 🚀 Deployment

### Docker
```bash
docker build -f Dockerfile -t pycompile .
docker run -p 8000:8000 pycompile
```

### Production Settings
```env
DEBUG=False
ALLOWED_ORIGINS=yourdomain.com
```

---

## 📊 Performance

- Average execution time: 50-100ms
- Max concurrent requests: Limited by server
- Code size limit: Unlimited (use timeout)

---

## 🐛 Error Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 400 | Bad request (invalid input) |
| 408 | Timeout exceeded |
| 500 | Server error |

---

## 📝 Logging

Logs appear in console during execution:
```
INFO:uvicorn.access: GET /health HTTP/1.1" 200
INFO:__main__: Executing code: print('Hello')...
```

---

## 🔄 CORS Configuration

For production, update `ALLOWED_ORIGINS`:
```python
# In main.py or .env
ALLOWED_ORIGINS=https://yourdomain.com,https://app.yourdomain.com
```

---

## 🚨 Limitations

- No external module imports
- No file system access
- Max 30 second timeout
- Python standard library only

---

## 📞 Support

Check logs for debugging:
```bash
# Run with verbose logging
python main.py --log-level debug
```
