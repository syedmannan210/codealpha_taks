import os
import shutil
import sys
import time

def custom_loader(sec:float):
    chars = ["-", "\\", "|", "/"]
    for _ in range(20):
        for char in chars:
            sys.stdout.write(f"\rFile Organization in Progress {char} ")
            sys.stdout.flush()
            time.sleep(sec)
    print("\nDone!")

print("Welcome to Python Automation Script for File Handling".center(150))
path = input("Please enter the directory path for File Organization (or type 'exit' to quit):\n")
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"New directory '{directory}' has been created")
def custom_filetype():
    while True:
        filetype = input('''Enter the file type (e.g., "docx", "pdf", etc.) that you want to organize (or type 'exit' to go back):\n''')
        if filetype.lower() == 'exit':
            exit()

        subdirectory = os.path.join(path, filetype)
        custom_loader(0.05)
        if not os.path.exists(subdirectory):
            create_directory(subdirectory)  # Create the subdirectory if it doesn't exist
            print(f"Created directory: {subdirectory}")

        files = os.listdir(path)
        found_file = False  # Flag to track if a matching file was found

        for file in files:
            root, extension = os.path.splitext(file)
            extension = extension[1:]  # Remove the leading dot from extension

            if extension == filetype:
                oldpath = os.path.join(path, file)
                newpath = os.path.join(subdirectory, file)  # Use the subdirectory path
                shutil.move(oldpath, newpath)
                print(f"Moved '{file}' to '{newpath}'")
                found_file = True

        if not found_file:
            print(f"No '{filetype}' files found in the current directory.")


def all_filetypes():
    custom_loader(0.05)
    files = os.listdir(path)
    while True:
        for file in files:
            root, extension = os.path.splitext(file)
            extension = extension[1:]  # Remove the leading dot from extension
            subdirectory = os.path.join(path, extension)
            if not os.path.exists(subdirectory):
                create_directory(subdirectory)
            try:
                oldpath = os.path.join(path, file)
                newpath = os.path.join(path, extension, file)
                shutil.move(oldpath, newpath)
                print(f"Moved '{file}' to '{newpath}'")
                print("Operation Successful!")
            except FileNotFoundError:
                print(f"Error: File '{file}' not found or destination directory missing.")
            except Exception as e:
                print(f"Error: {e}")
        break


def main():
    while True:
        if path.lower() == 'exit':
            break
        choice=input("Which type of files you want to manage:\n1- Custom Type\n2- All files in folder:\n3- Press 3 to exit:\n")
        if choice=="1":
            custom_filetype()
            custom_loader(0.05)
        if choice=="2":
            all_filetypes()
            custom_loader(0.05)
        if choice=="3":
            exit()


if __name__ == "__main__":
    main()
