from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import subprocess
import sys
import signal
import os
import re
from typing import Optional
from datetime import datetime
import logging

app = FastAPI(title="PyCompile - Python Executor API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production: specify your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Request Model
class CodeRequest(BaseModel):
    code: str
    timeout: Optional[int] = 10
    user_input: Optional[str] = None

class CodeResponse(BaseModel):
    success: bool
    output: Optional[str] = None
    error: Optional[str] = None
    execution_time: Optional[float] = None

# Health Check
@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "1.0.0"}

# API Info
@app.get("/api/info")
async def api_info():
    return {
        "name": "PyCompile",
        "version": "1.0.0",
        "description": "Advanced Python Code Executor API",
        "python_version": sys.version,
        "max_timeout": 30
    }

# Execute Code
@app.post("/api/execute")
async def execute_code(request: CodeRequest) -> CodeResponse:
    """
    Execute Python code and return output
    """
    if not request.code or not request.code.strip():
        raise HTTPException(status_code=400, detail="Code cannot be empty")
    
    if request.timeout > 30:
        raise HTTPException(status_code=400, detail="Timeout cannot exceed 30 seconds")

    normalized_input = request.user_input
    if normalized_input and not normalized_input.endswith("\n"):
        # Ensure the final input token is consumed cleanly by input().
        normalized_input += "\n"

    input_calls = len(re.findall(r"\binput\s*\(", request.code))
    provided_lines = 0
    if normalized_input is not None and normalized_input.strip() != "":
        provided_lines = len(normalized_input.rstrip("\n").splitlines())

    if input_calls > 0 and provided_lines == 0:
        return CodeResponse(
            success=False,
            error=(
                f"Your code expects input ({input_calls} input() call(s)), but no input was provided.\n"
                "Add values in the User Input box (one value per line)."
            ),
        )
    
    try:
        logger.info(f"Executing code: {request.code[:50]}...")
        
        # Execute code with timeout
        result = subprocess.run(
            [sys.executable, "-c", request.code],
            capture_output=True,
            text=True,
            input=normalized_input,
            timeout=request.timeout,
            cwd=os.getcwd()
        )
        
        if result.returncode != 0:
            error_text = (result.stderr or "Execution failed").strip()

            if "EOFError" in error_text:
                error_text += (
                    "\n\nHint: Not enough input values were provided. "
                    f"Detected {input_calls} input() call(s), received {provided_lines} line(s)."
                )

            return CodeResponse(
                success=False,
                error=error_text,
            )
        
        output = result.stdout
        if not output:
            output = "(No output)"
        
        return CodeResponse(
            success=True,
            output=output,
        )
    
    except subprocess.TimeoutExpired:
        if input_calls > 0:
            return CodeResponse(
                success=False,
                error=(
                    f"Execution timeout after {request.timeout}s. "
                    "Your code likely waited for input.\n"
                    "Add input values in the User Input box (one value per line)."
                )
            )
        return CodeResponse(
            success=False,
            error=f"Execution timeout: Code exceeded {request.timeout} seconds"
        )
    
    except Exception as e:
        logger.error(f"Error executing code: {str(e)}")
        return CodeResponse(
            success=False,
            error=f"Error: {str(e)}"
        )

# Advanced Features
@app.post("/api/analyze")
async def analyze_code(request: CodeRequest):
    """
    Analyze Python code for syntax errors and basic issues
    """
    try:
        compile(request.code, '<string>', 'exec')
        return {
            "valid": True,
            "message": "Code syntax is valid"
        }
    except SyntaxError as e:
        return {
            "valid": False,
            "error": str(e),
            "line": e.lineno,
            "offset": e.offset
        }
    except Exception as e:
        return {
            "valid": False,
            "error": str(e)
        }

@app.get("/api/python-version")
async def python_version():
    """Get Python version info"""
    return {
        "version": sys.version,
        "version_info": {
            "major": sys.version_info.major,
            "minor": sys.version_info.minor,
            "micro": sys.version_info.micro,
        },
        "platform": sys.platform,
        "executable": sys.executable
    }

@app.get("/api/libraries")
async def available_libraries():
    """
    Get list of available libraries for import
    """
    libraries = {
        "data_science": ["pandas", "numpy", "scipy", "scikit-learn", "matplotlib", "plotly"],
        "web": ["requests", "beautifulsoup4"],
        "data_formats": ["openpyxl", "csv", "json"],
        "standard_library": ["datetime", "collections", "itertools", "math", "random", "statistics", "time", "os", "sys", "re"]
    }
    return {
        "available_libraries": libraries,
        "message": "All these libraries are available for use in your code"
    }

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Welcome to PyCompile API",
        "endpoints": {
            "health": "/health",
            "info": "/api/info",
            "execute": "/api/execute (POST)",
            "analyze": "/api/analyze (POST)",
            "python_version": "/api/python-version",
            "libraries": "/api/libraries"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
