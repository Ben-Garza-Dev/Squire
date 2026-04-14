import os

def get_files_info(working_directory, directory= "."):
    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_directory_abs, directory))
        valid_target_dir = os.path.commonpath([working_directory_abs, target_dir]) == working_directory_abs
        if valid_target_dir is False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        valid_dir = os.path.isdir(target_dir)
        if valid_dir is False:

            return f'Error: "{directory}" is not a directory'
        
        dir_files_list = [ f'- {dir}: file_size={os.path.getsize(os.path.join(target_dir, dir))} bytes, is_dir={os.path.isdir(os.path.join(target_dir, dir))}' for dir in os.listdir(target_dir)]
        print(f"Results for {directory} directory:")
        return "\n".join(dir_files_list)
    except Exception as e:
        return f"Error {e}"
        