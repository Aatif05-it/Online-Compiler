from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import subprocess
import sys
import os
import re
from typing import Optional
import logging
import time

app = FastAPI(title="PyCompile - Python Executor API")


PORT = int(os.environ.get("PORT", 8000))
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*").split(",")


app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CodeRequest(BaseModel):
    code: str
    timeout: Optional[int] = 10
    user_input: Optional[str] = None

class CodeResponse(BaseModel):
    success: bool
    output: Optional[str] = None
    error: Optional[str] = None
    execution_time: Optional[float] = None

@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "1.0.0"}


@app.get("/api/info")
async def api_info():
    return {
        "name": "PyCompile",
        "version": "1.0.0",
        "python_version": sys.version,
        "max_timeout": 30
    }


@app.post("/api/execute")
async def execute_code(request: CodeRequest) -> CodeResponse:

    if not request.code.strip():
        raise HTTPException(status_code=400, detail="Code cannot be empty")

    if request.timeout > 30:
        raise HTTPException(status_code=400, detail="Max timeout = 30s")

    start_time = time.time()

    # Normalize input
    user_input = request.user_input or ""
    if user_input and not user_input.endswith("\n"):
        user_input += "\n"

    input_calls = len(re.findall(r"\binput\s*\(", request.code))
    provided_lines = len(user_input.strip().splitlines()) if user_input else 0

    if input_calls > 0 and provided_lines == 0:
        return CodeResponse(
            success=False,
            error="Input required but not provided"
        )

    try:
        result = subprocess.run(
            [sys.executable, "-c", request.code],
            input=user_input,
            capture_output=True,
            text=True,
            timeout=request.timeout,
        )

        execution_time = round(time.time() - start_time, 3)

        if result.returncode != 0:
            return CodeResponse(
                success=False,
                error=result.stderr.strip()
            )

        output = result.stdout.strip() or "(No output)"

        return CodeResponse(
            success=True,
            output=output,
            execution_time=execution_time
        )

    except subprocess.TimeoutExpired:
        return CodeResponse(
            success=False,
            error=f"Timeout after {request.timeout}s"
        )

    except Exception as e:
        logger.error(str(e))
        return CodeResponse(
            success=False,
            error=str(e)
        )


@app.post("/api/analyze")
async def analyze_code(request: CodeRequest):
    try:
        compile(request.code, "<string>", "exec")
        return {"valid": True}
    except SyntaxError as e:
        return {
            "valid": False,
            "error": str(e),
            "line": e.lineno
        }


@app.get("/")
async def root():
    return {"message": "PyCompile API running 🚀"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=PORT)