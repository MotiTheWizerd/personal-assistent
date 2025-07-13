import subprocess
from typing import Dict, Any

def execute_command(command: str) -> Dict[str, Any]:
    """
    Execute a CMD command on the Windows system.
    
    Args:
        command: The CMD command to execute
        
    Returns:
        dict: A dictionary containing:
            - success: bool indicating if the command executed successfully
            - output: str with the command output (stdout)
            - error: str with any error message (stderr)
            - return_code: int with the process return code
    """
    try:            
        result = subprocess.run(
            ["cmd.exe", "/c", command],
            text=True,
            capture_output=True,
            shell=False,
            timeout=30  # 30 second timeout
        )
        
        return {
            "success": result.returncode == 0,
            "output": result.stdout.strip(),
            "error": result.stderr.strip(),
            "return_code": result.returncode
        }
        
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "output": "",
            "error": "Command timed out after 30 seconds",
            "return_code": -1
        }
    except Exception as e:
        return {
            "success": False,
            "output": "",
            "error": str(e),
            "return_code": -1
        }
