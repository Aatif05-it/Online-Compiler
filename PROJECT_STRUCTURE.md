# PyCompile Project Structure

```
Compiler/
│
├── 📁 backend/
│   ├── main.py                 # FastAPI application (core)
│   ├── config.py               # Configuration settings
│   ├── requirements.txt         # Python dependencies
│   ├── .env.example            # Environment template
│   └── README.md               # Backend documentation
│
├── 📁 frontend/
│   ├── index.html              # Main HTML page
│   ├── styles.css              # CSS styling (dark/light theme)
│   ├── app.js                  # JavaScript logic
│   └── README.md               # Frontend documentation
│
├── 📁 .github/workflows/
│   └── deploy.yml              # GitHub Actions deployment
│
├── 📄 docker-compose.yml       # Docker multi-container setup
├── 📄 Dockerfile               # Docker image for backend
├── 📄 nginx.conf               # Nginx proxy configuration
├── 📄 render.yaml              # Render deployment config
├── 📄 README.md                # Project documentation
└── 📄 DEPLOYMENT.md            # Deployment guide

```

## 🔧 Key Files Explanation

### Backend
- **main.py**: FastAPI application with endpoints for code execution
- **config.py**: Centralized configuration management
- **requirements.txt**: All Python packages needed

### Frontend
- **index.html**: Beautiful, modern UI with dark/light theme
- **styles.css**: Comprehensive styling with VS Code-like design
- **app.js**: Client-side logic, API communication, local storage

### Deployment
- **docker-compose.yml**: Run both backend and frontend in Docker
- **Dockerfile**: Container setup for production
- **render.yaml**: One-click deployment to Render
