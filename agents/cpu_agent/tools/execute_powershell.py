import subprocess
import sys
import ctypes
import os
from typing import Dict, List, Any, Optional

def is_admin() -> bool:
    """Check if the script is running with administrator privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    """Relaunch the script with administrator privileges."""
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join([f'"{arg}"' for arg in sys.argv]), None, 1
    )
    sys.exit(0)

def execute_powershell(command: str, require_admin: bool = False) -> Dict[str, Any]:
    """
    Execute a PowerShell command on the Windows system.
    
    Args:
        command: The PowerShell command to execute
        require_admin: If True, ensures the command runs with admin privileges
        
    Returns:
        dict: A dictionary containing:
            - success: bool indicating if the command executed successfully
            - output: str with the command output (stdout)
            - error: str with any error message (stderr)
            - return_code: int with the process return code
    """
    if require_admin and not is_admin():
        # If admin is required but not running as admin, restart with admin rights
        run_as_admin()
        return {
            "success": False,
            "output": "",
            "error": "Restarting with admin privileges...",
            "return_code": 0
        }
    try:
        cmd = [
            "powershell.exe",
            "-NoProfile",
            "-NoExit" if sys.stdout.isatty() else "-NonInteractive",
            "-ExecutionPolicy", "Bypass",
            "-WindowStyle", "Hidden" if not sys.stdout.isatty() else "Normal",
            "-Command", command
        ]
            
        result = subprocess.run(
            cmd,
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

def list_connected_bluetooth_devices() -> Dict[str, List[str]]:
    """
    List all currently connected Bluetooth devices by querying Windows Bluetooth device status.
    
    Returns:
        dict: A JSON object with a list of connected device names (empty list if error).
    """
    try:
        result = execute_powershell(
            "Get-PnpDevice -Class Bluetooth | "
            "Where-Object { $_.Status -eq 'OK' } | "
            "Select-Object -ExpandProperty FriendlyName"
        )
        
        if result["success"] and result["output"]:
            devices = [name.strip() for name in result["output"].split('\n') if name.strip()]
            return {"devices": devices}
        return {"devices": []}
        
    except Exception:
        return {"devices": []}
