import os

# os.walk() returns a generator that creates a tuple of
# (current_path, sub-directories in current_path, files in current_path)
for folderName, subfolders, filenames in os.walk('.'):
    # Every time the generator is called it will follow each directory
    # recursively until no further sub-directories are available

    print('folderName:', folderName, 'subfolders:', subfolders,
          'filenames', filenames)

    print('The current folder is ' + os.path.abspath(folderName)
          + ' (or ' + folderName + ')')

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)

    print('')
