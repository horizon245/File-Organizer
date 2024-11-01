import os
import shutil

def main():
    root_directory = "/home/horizon/Downloads"
    files = retrieve_files(root_directory)
    categorized_files = categorize_files(files)
    move_files(categorized_files, root_directory)

def retrieve_files(directory):
    list_of_files = []

    for root, _, files in os.walk(directory):
        for file in files:
            path_of_file = os.path.join(root, file)
            list_of_files.append(path_of_file)

    return list_of_files

def categorize_files(files):
    categories = {
        "Videos": [".mp4", ".avi", ".mkv"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
        "Music": [".mp3", ".wav", ".aac"],
        "Pictures": [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
    }

    categorized_files = {category: [] for category in categories}
    for file in files:
        file_extension = os.path.splitext(file)[1].lower()
        categorized = False

        for category, extensions in categories.items():
            if file_extension in extensions:
                categorized_files[category].append(file)
                categorized = True
                break

        if not categorized:
            if "Others" not in categorized_files:
                categorized_files["Others"] = []
            categorized_files["Others"].append(file)

    return categorized_files

def move_files(categorized_files, root_directory):
    for category, files in categorized_files.items():
        category_folder = os.path.join(root_directory, category)
        os.makedirs(category_folder, exist_ok=True)

        for file in files:
            try:
                target_path = os.path.join(category_folder, os.path.basename(file))
                shutil.move(file, target_path)
                print(f"Moved: {file} --> {target_path}")

            except Exception as e:
                print(f"Error moving {file}: {e}")

if __name__ == "__main__":
    main()
