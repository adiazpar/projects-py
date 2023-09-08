# strings are immutable
name = 'Zophie'
print(name[0])
# Z
#name[0] = 'S'
# TypeError: 'str' object does not support item assignment
newName = 'S' + name[1:]
print(newName)
# Sophie

# tuples
eggs = ('hello', 42, 0.5)
print(eggs[0])
# hello
print(eggs[1:3])
# (42, 0.5)
print(len(eggs))
# 3
#eggs[0] = 99
# TypeError: 'tuple' object does not support item assignment

# lists are mutable
spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'hello!'
print(cheese)
# [0, 'hello!', 2, 3, 4, 5]
print(spam)
# [0, 'hello!', 2, 3, 4, 5]
