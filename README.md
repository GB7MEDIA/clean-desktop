# Clean-Desktop

## Description
The Clean-Desktop script is designed to analyze files in a specified directory and generate a detailed log report. This report includes a table of file types with their counts and a list of files with their names, paths, and sizes. The script is particularly useful for organizing and gaining insights into the contents of large directories.

## Installation

### Prerequisites
- Python 3.x
- Pandas library

### Steps
1. Ensure Python 3.x is installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

2. Install the Pandas library. This can be done via pip: pip install pandas

3. Clone the repository or download the script: git clone https://github.com/GB7MEDIA/clean-desktop.git

Alternatively, you can download the `analyse-files-on-computer.py` file directly from the repository.

## Usage

1. Navigate to the directory where the script is located: cd path/to/clean-desktop

2. Run the script by specifying the directory you want to analyze. Replace `path/to/directory` with the actual path of the directory: python analyse-files-on-computer.py path/to/directory

For example, to analyze your entire desktop, you might run: python analyse-files-on-computer.py /Users/yourusername/Desktop

3. After running the script, check the `logs` folder in the script's directory. You will find the generated log file named in the format `log-YYYY-MM-DD-HH:MM.txt`, containing the report.

## Notes
- The script creates a `logs` directory to store the log files.
- Files in `/Applications`, `.vscode`, and `node_modules` directories are skipped during the analysis.
- The script can handle large directories but may take some time to process them, depending on the number and size of the files.

## Contributing
Feel free to fork the repository and submit pull requests with enhancements or fixes.

## License
[MIT License](LICENSE.md) or specify another license if applicable.


