"""
Homework 6 Exercise 2
Name: Alejandro Diaz
Due Date: 11/26/23

Exercise 2:
Write a program that
    1. Walks through a directory tree (os.walk()) and searches for files with a .pdf extension.
       You can create a directory (and optionally some subdirectories) with a few pdf files for testing.

    2. Print these files with their absolute path and file size to the screen.

    3. Copy these files from whatever location they are into a new folder in your current working
       directory called allPdfs.

"""

import os
import shutil
destination = os.path.abspath('allPdfs')


def clear_destination():
    # Iterate through all files in the target directory:
    for file in os.listdir(destination):
        path = os.path.join(destination, file)

        try:
            # Check if the path is a file (not sure what islink does):
            if os.path.isfile(path) or os.path.islink(path):
                os.unlink(path)

            # If a directory is found inside of target, remove it and all its contents:
            elif os.path.isdir(path):
                shutil.rmtree(path)

        except Exception as e:
            print('Failed to delete %s. \nReason: %s' % (path, e))


def list_copy_pdf_files():
    for folderName, sub_folders, filenames in os.walk('.'):
        for filename in filenames:

            # Only checking files with a .pdf extension:
            if filename.endswith('.pdf') or filename.endswith('.PDF'):
                pdf = os.path.abspath(folderName) + '/' + filename
                size = os.path.getsize(pdf)

                # Print absolute path + file size:
                print('PDF FILE FOUND: ' + pdf)
                print('SIZE: ' + str(size))

                # Copy file from last location to target destination:
                shutil.copy(pdf, destination)
                print('COPIED TO: ' + destination + '\n')


if __name__ == "__main__":
    # Clear destination directory to avoid errors when copying:
    clear_destination()

    # Walk through directory tree:
    list_copy_pdf_files()


