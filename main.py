import os
from datetime import datetime
import shutil


class FileManager:
    def __init__(self, directory):
        self.directory = directory
        self.extensions = {
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
            'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.ppt', '.pptx'],
            'Audio': ['.mp3', '.wav', '.flac'],
            'Video': ['.mp4', '.avi', '.mkv', '.mov'],
            'Archives': ['.zip', '.rar', '.7z']
        }

    def create_categories_folders(self):
        """
        Create folders for each category defined in self.extensions.
        If a folder already exists, it will not be recreated.
        """
        for category in self.extensions.keys():
            category_path = os.path.join(self.directory, category)
            if not os.path.exists(self.directory, category):
                os.makedirs(category_path)

    def get_category(self, file_extension):
        """
        Determine the category of a file based on its extension.

        Args:
            file_extension (str): The file extension to categorize.

        Returns:
            str: The category name, or 'Other' if no matching category is found.
        """
        for category, extensions in self.extensions.items():
            if file_extension.lower() in extensions:
                return category
        return 'Other'

    def organize_files(self):
        """
        Organize files in the specified directory into category folders.
        This method creates category folders and moves files into them based on their extensions.
        """
        # Create category folders
        self.create_categories_folders()

        # Iterate through files in the directory
        for filename in os.listdir(self.directory):
            if os.path.isfile(os.path.join(self.directory, filename)):
                # Get file extension and determine its category
                file_extension = os.path.splitext(filename)[1]
                category = self.get_category(file_extension)

                # Set up source and destination paths
                source_path = os.path.join(self.directory, filename)
                destination_path = os.path.join(
                    self.directory, category, filename)

                try:

                    # Move the file to its category folder
                    shutil.move(source_path, destination_path)
                    print(f"Moved: {filename} to {category}")

                except Exception as e:
                    print(f"Error moving {filename}: {e}")


def main():
    """
      Main function to run the file organization process.
      It prompts the user for a directory, validates it, 
      and organizes the files.
    """

    print("file manager started")
    source_directory = input("Enter the directory to organize: ")
  # Validate the provided directory
    if not os.path.exists(source_directory):
        print("The provided directory does not exist.")
        return
        # Create a FileManager instance and organize the files
    manager = FileManager(source_directory)
    manager.organize_files()
    print("File organization completed.")


if __name__ == "__main__":
    main()
