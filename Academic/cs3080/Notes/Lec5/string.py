# String literals
#print('That is Alice's cat.')
# SyntaxError: invalid syntax

# Double quotes
print("That is Alice's cat.")

# Escape characters
print('Hello there!\nHow are you?\nI\'m doing fine.')
# Hello there!
# How are you?
# I'm doing fine.

# Raw string
print(r'That is Carol\'s cat.')
# That is Carol\'s cat.

# When a backslash is followed by a quote in a raw string, the quote
# is escaped. However, the backslash still shows up in the result.
# https://www.digitalocean.com/community/tutorials/python-raw-string
#print(r'That is Carol\\'s cat.')
# SyntaxError: invalid syntax
#print(r'That is Carol\\\'s cat.')
# That is Carol\\\'s cat.

# Multiline string
print("""Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob""")
# Same as
print('Dear Alice,\n\nEve\'s cat has been arrested for catnapping, cat burglary, and extortion.\n\nSincerely,\nBob')

# Indexing and slicing strings
spam = 'Hello world!'
print(spam[0])
# 'H'
print(spam[-1])
# '!'
print(spam[0:5])
# 'Hello'
print(spam[:5])
# 'Hello'
print(spam[6:])
# 'world!'

# in and not in operators (case sensitive)
print('Hello' in 'Hello World')
# True
print('Hello' in 'Hello')
# True
print('HELLO' in 'Hello World')
# False
print('' in 'spam')
# True
print('cats' not in 'cats and dogs')
# False