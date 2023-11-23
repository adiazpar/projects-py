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

import re
import os
import shutil


def convert(american_date, pattern):

    # This function converts MM-DD-YYYY to DD-MM-YYYY
    date_regex = re.search(pattern, american_date)
    file_other = american_date.split(date_regex.group(0))[0]
    file_extension = american_date.split(date_regex.group(0))[1]
    old_date = date_regex.group(0)

    date_split = old_date.split("-")
    new_date = date_split[1] + "-" + date_split[0] + "-" + date_split[2]

    asian_date = file_other + new_date + file_extension
    return asian_date


if __name__ == "__main__":

    # Get the list of all files in the given directory:
    file_list = os.listdir('dates_test')

    # Define the Regex for American Dates:
    date_patrn = "([0-9]{2}-[0-9]{2}-[0-9]{4})"

    # Changing the current working directory to folder with test dates:
    os.chdir(os.getcwd() + '/dates_test')

    # Loop over each file in the list to match with the regex:
    for file in file_list:
        if re.search(date_patrn, file):
            # Creating the asian date and renaming original file:
            asian_date_file = convert(file, date_patrn)

            print("Renamed " + file + " -> " + asian_date_file)
            shutil.move(file, asian_date_file)


"""
    Interestingly enough, you can run the program again and
    change back to American style dates. Run again, change back to
    Asian style dates. 
    
    I may implement error checking and a way to identify different 
    style dates so the program can categorize them properly.
    
    At it's current state, it just flips the first 2 groups
    of the date regex.
"""
