import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_directory_abs, file_path))
        valid_target = os.path.commonpath([working_directory_abs, target_file_path]) == working_directory_abs
        is_file =  os.path.isfile(target_file_path)

        if valid_target == False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if is_file == False:
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if file_path.endswith(".py") is False:
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_file_path]

        if args:
            command.extend(args)

        result = subprocess.run( command, cwd=working_directory, capture_output=True, text=True, timeout=30)


        output = ""
        if result.returncode != 0:
            output += f'Process exited with code {result.returncode}\n'
        if result.stdout == "" and result.stderr == "":
            output += f'No output produced\n'
        else:
            if result.stdout:
                output += f'STDOUT:\n{result.stdout}'
            if result.stderr:
                output += f'STDERR:\n{result.stderr}'
        
        return output
    except Exception as e:
        return f'Error: executing Python file: {e}'    

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute Python files with optional arguments",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to a python file to execute"
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="List of optional keyword commands",
                items=types.Schema(type=types.Type.STRING)
            )
            
        }
    )
)