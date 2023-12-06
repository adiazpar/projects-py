spam = ['hello', 'hi', 'howdy', 'hola']

print(spam[-1])  # last item
print(spam[-2])  # second to last item

# slicing a list
print(spam[1:4])   # ['hi', 'howdy', 'hola']
print(spam[:4])    # ['hello', 'hi', 'howdy', 'hola']
print(spam[2:])    # ['howdy', 'hola']
print(spam[2:None]) # ['howdy', 'hola']

L = [0, 1, 2, 3, 4, 5, 6]
print(L[0:4:2])    # [0, 2]
print(L[::2])      # [0, 2, 4, 6]
print(L[::-1])     # [6, 5, 4, 3, 2, 1, 0]

print([1, 2, 3] + ['A', 'B', 'C'])
# [1, 2, 3, 'A', 'B', 'C']
print(['X', 'Y', 'Z'] * 3)
# ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']

spam = ['Bob']
spam += ['Alice']
print(spam)    # ['Bob', 'Alice']
spam *= 3
print(spam)
# ['Bob', 'Alice', 'Bob', 'Alice', 'Bob', 'Alice']

# Nested list - lists can contain lists! A list of lists... unga bunga
spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(spam[0])
# ['cat', 'bat']
print(spam[0][1] + "Concact" + str(spam[1][1]), spam[1][4])
# 'bat'
print(spam[1][4])
# 50
