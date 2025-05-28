import os
import shutil

# Set your source folder
source_folder = "C:\\Users\\danny\\Downloads"

# Define file categories and extensions
file_types = {
    "Documents": [".pdf", ".docx", ".txt", ".doc", ".odt"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac"],
    "Scripts": [".py", ".js", ".html", ".css", ".ipynb"],
    "Archives": [".zip", ".rar", ".7z"],
    "Installers": [".exe", ".msi", ".pyc"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Presentations": [".ppt", ".pptx"],
    "Virtual_Machines": [".vmdk", ".vdi", ".ova", ".vbox"],
    "Miscellaneous": [".json", ".xml", ".log", ".md"],
    "Databases": [".db", ".sqlite", ".sql"],
    "Diagrams": [".drawio", ".vsdx", ".svg", ".cairis"],
    "Wireshark": [".pcap", ".pcapng"]
}

# Prevent organizing files into folders we just created
destination_folders = set(file_types.keys())

# Walk through all folders and subfolders
for root, dirs, files in os.walk(source_folder):
    # Skip the folders we just created to avoid moving files back and forth
    if any(root.endswith(cat) for cat in destination_folders):
        continue

    for filename in files:
        file_path = os.path.join(root, filename)
        ext = os.path.splitext(filename)[1].lower()

        for folder, extensions in file_types.items():
            if ext in extensions:
                # Build full destination folder: e.g. Documents\PDF
                category_folder = os.path.join(source_folder, folder)
                sub_folder = os.path.join(category_folder, ext[1:].upper())
                os.makedirs(sub_folder, exist_ok=True)

                try:
                    shutil.move(file_path, os.path.join(sub_folder, filename))
                    print(f"Moved {filename} → {sub_folder}")
                except PermissionError:
                    print(f"Skipping {filename}: file in use.")
                break  # Stop checking after matching one category