from fastapi import FastAPI
from pydantic import BaseModel
from executor import run_compiler
import tempfile

app = FastAPI()

class CodeInput(BaseModel):
    code: str = ""

@app.post("/execute")
async def execute_code(file: CodeInput) -> dict:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".ffo") as temporary:
        temporary.write(file.code.encode("utf-8"))
        temporary_path = temporary.name

    result = run_compiler(temporary_path)
    return result
