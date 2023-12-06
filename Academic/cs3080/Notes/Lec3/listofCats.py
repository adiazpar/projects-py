
# catNames is known as the 'list'
# Therefore, the individual items in a list can be referenced as catNames[0], catNames[1], etc.
# The things inside a list are known as 'items'

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1)
          + ' (Or enter nothing to stop):')
    name = input()
    if name == '':
        break
    catNames += [name]  # list concatenation
    print(catNames)


print('The cat names are:')
for name in catNames:
    print(' ' + name)

print('Another way to print cat names:')
for i in range(len(catNames)):
    print(catNames[i])

print('Print the list:')
print(catNames)

'''
Notes:

I believe you can also refer to items in a list with negative indexes. 
This means that catNames[-1] will return the LAST item in a list, and so on...

SUBLISTS WITH SLICES:
    - Refer to listOperations.py
    - A 'slice' in a list can get several values from it, in the form of a new list.
                                
        Slice in a list -> catNames[1:4]       Refer to items catNames[1] - catNames[3]
        catNames[:4]                           Refer to everything up to but not including 4
        
    - This means I can refer to items of a list from index 1 to index 3, because 4 is non inclusive.
    
    - Slicing can also be extended to a third number:
        
        catNames[n:m:k]
        Where k is a skipping element, meaning this slice returns every kth element from n to m.

'''
# Questions:
