# Python File Organizer

A simple  Python script to automatically organize files in a directory based on their file types. 
This tool helps you maintain a clean and structured file system by categorizing files into appropriate folders.

## Features

- Automatically categorizes files based on their extensions
- Creates category folders as needed
- Supports multiple file types including:
  - Images (.jpg, .jpeg, .png, .gif, .bmp)
  - Documents (.pdf, .doc, .docx, .txt, .xlsx, .ppt, .pptx)
  - Audio (.mp3, .wav, .flac)
  - Video (.mp4, .avi, .mkv, .mov)
  - Archives (.zip, .rar, .7z)
- Moves files to their respective category folders
- Provides feedback on the organization process

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses standard library modules)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/ahhmadas213/file-manager.git
```

2. Navigate to the project directory:
```bash
cd file-organizer
```

## Usage

1. Run the script:
```bash
python file_organizer.py
```

2. When prompted, enter the path to the directory you want to organize:
```
File Organizer
Enter the directory path to organize: /path/to/your/directory
```

3. The script will automatically:
   - Create category folders if they don't exist
   - Move files to their respective category folders
   - Print progress as files are moved

## Code Structure

- `FileOrganizer` class:
  - `__init__(source_dir)`: Initializes the organizer with source directory and categories
  - `create_category_folders()`: Creates necessary category folders
  - `get_category(file_extension)`: Determines the category for a given file extension
  - `organize_files()`: Moves files to their respective category folders

## Example

```python
organizer = FileOrganizer("/path/to/messy/directory")
organizer.organize_files()
```





## Acknowledgments

- Inspired by the need for automated file organization
- Thanks to the Python community for the robust standard library

## Support

If you encounter any problems or have any questions, please open an issue on GitHub.
