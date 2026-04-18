import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_directory_abs, file_path))
        valid_target = os.path.commonpath([working_directory_abs, target_file_path]) == working_directory_abs
        existing_directory = os.path.isdir(target_file_path)
        

        if valid_target == False:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if existing_directory == True:
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        os.makedirs(os.path.dirname(target_file_path), exist_ok=True)
        
        with open(target_file_path, 'w') as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: {e}'
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write or overwrite a specific file, in directory relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path", "content"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path of file to write to"
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="This is the content that will will be written in"
            )
        }
    )
)