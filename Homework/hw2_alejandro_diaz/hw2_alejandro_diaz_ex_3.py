"""
Homework 2 Exercise 3
Name: Alejandro Diaz
Due Date: 09/22/23

Exercise 3:
[v]    1. Create a list with strings 'Wallet', 'Phone', and 'Keys'. Print the list variable using a single line of code
[v]    2. Sort the list using the sort() function, then print the list again
[v]    3. Print the first item in the list
[v]    4. Print everything except the first item in the list as a list using slicing
[v]    5. Print the last item in the list using negative index
[v]    6. Print the index of 'Keys' using index()
[v]    7. Append 'Tablet' to the list, then print the list
[v]    8. Insert 'Mask' to the list as the second item in the list, then print the list
[v]    9. Remove 'Phone' from the list, then print the list
[v]    10. Reverse the list, then print the list
[x]    11. Finally, write a function strList() that takes this current list as an argument and returns a
           string with all the items separated by a comma and a space, with ‘and’ inserted before
           the last item. For example, if the current list value is ['Tablet', 'Wallet', 'Mask', 'Keys']
           (note this may not be the correct list at this point), then passing it to the function would
           return 'Tablet, Wallet, Mask, and Keys'. Call this function in your code. Your function
           should be able to work with any list value passed to it.
"""

# PART 1: Creating the list
items = ["Wallet", "Phone", "Keys"]
print(items)

# PART 2: Sorting the list in alphabetical order:
items.sort()
print(items)

# PART 3: Printing the first element in the list:
print(items[0])

# PART 4: Printing everything in the list except the first element, using slice:
print(items[1:])

# PART 5: Printing the last element of the list using negative index:
print(items[-1])

# PART 6: Printing the index of where "Keys" is located:
print(items.index("Keys"))

# PART 7: Appending "Tablet" to the list, then printing:
items.append("Tablet")
print(items)

# PART 8: Inserting "Mask" in the second index of the list, then printing:
items.insert(1, "Mask")
print(items)

# PART 9: Removing the item "Phone" from the list:
items.remove("Phone")
print(items)

# PART 10: Reversing the list:
items.reverse()
print(items)


# PART 11: Creating a function to print the list as a formal sentence:
def strList(items_local):
    out = ""

    for i in items_local:
        if i == items_local[-2]:
            out += i + ", and "
        elif i == items_local[-1]:
            out += i
        else:
            out += i + ", "

    return out


print(strList(items))


