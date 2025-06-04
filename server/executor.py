import docker
import os

import docker.errors

def run_compiler(source_path: str) -> dict:
    client = docker.from_env()
    container = None

    try:
        container = client.containers.run(
            image="sha256:e3a76d577bef280fc3e4891b905d3b5e89b209e652ebb9b420a7bf33f537a218",
            command=None,
            volumes={
                os.path.abspath(source_path): {
                    "bind": "/home/runner/source_code.ffo",
                    "mode": "ro"
                }
            },
            remove=True,
            stdout=True,
            stderr=True,
            mem_limit="256m",
            pids_limit=64
        )

        return {
            "success": True,
            "output": container.decode("utf-8")
        }

    except docker.errors.ContainerError as e:
        return {
            "success": False,
            "error": e.stderr if e.stderr else str(e)
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
