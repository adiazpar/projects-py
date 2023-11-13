"""
Homework 6 Exercise 1
Name: Alejandro Diaz
Due Date: 11/26/23

Exercise 1:
Your boss emailed you thousands of files with American-style dates (MM-DD-YYYY) in their names
and need them renamed to Asian-style dates (YYYY-MM-DD).

Note that filenames cannot contain slashes (/), otherwise your file system would confuse it
with the path separation. This boring task could take all day to do by hand.
Let’s write a program to do it instead!

Here’s what the program should do:
- Search all filenames in the current working directory for American-style dates in the names.
- When one is found, rename the file to make the date portion Asian style (the rest of the filename does not change).

This means the code will need to do the following:
    1. Create a regex that can identify the text pattern of American-style dates in a filename.
       Please note that the MM and DD parts have different ranges of numbers. You can manually create
       a few files for testing.

    2. Call os.listdir() to find all the files in the current working directory.

    3. Loop over each filename and use the regex to check whether the name contains an American style date,
       if so then rename the file with shutil.move().

"""


if __name__ == "__main__":
    print("Hello!")
