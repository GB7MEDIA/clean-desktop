import os
from datetime import datetime
import pandas as pd

def get_file_info(directory):
    """Scan the given directory and return file information."""
    file_types = {}
    file_list = []
    inaccessible_files = []  # Optional: to keep track of inaccessible files

    for root, _, files in os.walk(directory):
        # Skip specific directories and their contents
        if any(skip_folder in root for skip_folder in ['/Applications', '.vscode', 'node_modules']):
            continue

        for file in files:
            file_path = os.path.join(root, file)

            try:
                if os.path.isfile(file_path):  # Check if it's a regular file
                    file_size = os.path.getsize(file_path)
                    _, file_extension = os.path.splitext(file)

                    # Update file types count
                    file_types[file_extension] = file_types.get(file_extension, 0) + 1

                    # Append file info to the list
                    file_list.append([file, file_path, file_size])
            except Exception as e:
                # Handle the exception (optional)
                inaccessible_files.append(file_path)

    # Optional: Return inaccessible_files if needed
    return file_types, file_list, inaccessible_files

def create_log_file(directory):
    """Create a log file with file information from the given directory."""
    current_date = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M")
    
    # Ensure 'logs' directory exists
    logs_dir = 'logs'
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    log_file_name = f"{logs_dir}/log-{current_date}-{current_time}.txt"  # Update file name with folder path

    file_types, file_list, inaccessible_files = get_file_info(directory)

    # Create a DataFrame for file types
    df_file_types = pd.DataFrame(list(file_types.items()), columns=['File Type', 'Number of files'])
    
    # Create a DataFrame for file list
    df_file_list = pd.DataFrame(file_list, columns=['Filename', 'Path to File', 'File Size'])

    with open(log_file_name, 'w') as file:
        file.write("Number of File Types: " + str(len(file_types)) + "\n")
        file.write("Table of File Types:\n")
        file.write(df_file_types.to_string(index=False))
        file.write("\n\nList of Files:\n")
        file.write(df_file_list.to_string(index=False))

        # Optional: Log inaccessible files
        if inaccessible_files:
            file.write("\n\nInaccessible Files:\n")
            for file_path in inaccessible_files:
                file.write(file_path + "\n")

# Replace 'your_directory_path' with the path to the directory you want to scan
create_log_file('/Users')


