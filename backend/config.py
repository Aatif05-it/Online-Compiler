import os
from dotenv import load_dotenv

load_dotenv()

# Server Configuration
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8000))
DEBUG = os.getenv("DEBUG", "False") == "True"

# Execution Configuration
MAX_TIMEOUT = 30
DEFAULT_TIMEOUT = 10

# CORS Configuration
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*").split(",")

# API Configuration
API_TITLE = "PyCompile - Advanced Python Executor"
API_VERSION = "1.0.0"
