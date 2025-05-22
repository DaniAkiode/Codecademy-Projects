
import os  # OS is used to interact with the file system
import shutil  # shutil is used to move files

# Organizes files in a specified folder based on their file types
source_folder = "C:\\Users\\danny\\Downloads"  # Update this to your actual path

# Define file types and their associated extensions
file_types = {
    "Documents": [".pdf", ".docx", ".txt"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac"],
    "Scripts": [".py", ".js", ".html", ".css"],
    "Archives": [".zip", ".rar", ".7z"]
}

# Loop through all files in the source folder
for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

    # Skip if it is not a file
    if os.path.isfile(file_path):
        # Get the file extension and convert to lowercase
        ext = os.path.splitext(filename)[1].lower()

        # Match file extension to a category
        for folder, extensions in file_types.items():
            if ext in extensions:
                # Create destination folder
                dest_folder = os.path.join(source_folder, folder)
                # Create the folder if it doesn't exist
                os.makedirs(dest_folder, exist_ok=True)
                # Move the file
                shutil.move(file_path, os.path.join(dest_folder, filename))
                print(f"Moved {filename} to {dest_folder}")
                break  # Stop after finding the right category