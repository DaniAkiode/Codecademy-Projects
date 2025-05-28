import os
import shutil

# ✅ Set the folder to organize
source_folder = "C:\\Users\\danny\\Downloads"

# ✅ Define file types and associated extensions
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

# ✅ Go through each file in the source folder
for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

    # ✅ Skip folders
    if not os.path.isfile(file_path):
        continue

    # ✅ Get extension and lower case it
    ext = os.path.splitext(filename)[1].lower()

    moved = False  # Track whether file was moved

    for folder, extensions in file_types.items():
        if ext in extensions:
            # ✅ Create main and subfolders
            category_folder = os.path.join(source_folder, folder)
            os.makedirs(category_folder, exist_ok=True)

            sub_folder = ext[1:].upper()
            final_folder = os.path.join(category_folder, sub_folder)
            os.makedirs(final_folder, exist_ok=True)

            try:
                shutil.move(file_path, os.path.join(final_folder, filename))
                print(f"✅ Moved {filename} to {final_folder}")
                moved = True
            except PermissionError:
                print(f"❌ Skipped (in use): {filename}")
            break  # No need to check other categories

    # ✅ If file didn't match any category
    if not moved:
        unsorted_folder = os.path.join(source_folder, "Unsorted")
        os.makedirs(unsorted_folder, exist_ok=True)
        try:
            shutil.move(file_path, os.path.join(unsorted_folder, filename))
            print(f"📁 Moved {filename} to Unsorted")
        except PermissionError:
            print(f"❌ Skipped (in use): {filename}")