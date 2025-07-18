from fastapi import APIRouter
from pydantic import BaseModel
import subprocess, tempfile, os

router = APIRouter(tags=["code-runner"])

class CodeRequest(BaseModel):
	source_code: str = ""

@router.post("/run")
async def execute_code(request: CodeRequest) -> dict:
	code = request.source_code

	try:
		with tempfile.NamedTemporaryFile(suffix=".ffo", mode="w+", delete=False) as temporary_file:
			temporary_file.write(code)
			temporary_file_path = temporary_file.name

		compile_result = subprocess.run(["./sacompiler", temporary_file_path], capture_output=True, text=True, timeout=5)

		if compile_result.returncode != 0:
			os.unlink(temporary_file_path)
			return {
				"stage": "compilation",
				"exit_code": compile_result.returncode,
				"stdout": compile_result.stdout,
				"stderr": compile_result.stderr
			}

		exec_result = subprocess.run(["./out"], capture_output=True, text=True, timeout=5)

		# Cleanup
		os.unlink(temporary_file_path)
		os.remove("out.o")
		os.remove("out.asm")
		os.remove("out")

		return {
			"stage": "execution",
			"exit_code": exec_result.returncode,
			"stdout": exec_result.stdout,
			"stderr": exec_result.stderr
		}

	except Exception as err:
		return {"error": err}