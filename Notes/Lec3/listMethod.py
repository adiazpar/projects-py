# len()
spam = ['cat', 'dog', 'moose']
print(len(spam))
# 3
print(spam[len(spam)-1])
# 'moose'

# del statement
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
print(spam)
# ['cat', 'bat', 'elephant']
del spam[2]
print(spam)
# ['cat', 'bat']

# The Multiple Assignment Trick
cat = ['fat', 'black', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
# same as
cat = ['fat', 'black', 'loud']
size, color, disposition = cat
# number of variables must be equal
#size, color, disposition, name = cat
# ValueError: need more than 3 values to unpack

spam = ['hello', 'hi', 'howdy', 'hola']
print(spam.index('hello'))
# 0
print(spam.index('hola'))
# 3
#print(spam.index('howdy howdy howdy'))
# ValueError: 'howdy howdy howdy' is not in list

# Append/insert
spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam)
# ['cat', 'dog', 'bat', 'moose']
spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
print(spam)
# ['cat', 'chicken', 'dog', 'bat']

# Remove
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
print(spam)
# ['cat', 'rat', 'elephant']
spam = ['cat', 'bat', 'rat', 'elephant']
#spam.remove('chicken')
# ValueError: list.remove(x): x not in list

spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam.remove('cat')  # 'cat' appears multiple times,
                    # the first instance is removed
print(spam)
['bat', 'rat', 'cat', 'hat', 'cat']

# Sort
spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)
# [-7, 1, 2, 3.14, 5]
spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
print(spam)
# ['ants', 'badgers', 'cats', 'dogs', 'elephants']
spam.sort(reverse=True)
print(spam)
# ['elephants', 'dogs', 'cats', 'badgers', 'ants']
spam = [1, 3, 2, 4, 'Alice', 'Bob']
#print(spam.sort())
# TypeError: '<' not supported between instances of 'str' and 'int'

l = ['Z', 'a']
l.sort()  # show ord('Z') and ord('a')
print(l)
# ['Z', 'a']
l.sort(key=str.lower)
print(l)
#['a', 'Z']
