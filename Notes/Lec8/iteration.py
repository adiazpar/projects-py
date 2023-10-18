x = iter([1, 2, 3])
print(type(x))
#<class 'list_iterator'>

print(next(x))
print(next(x))
print(next(x))
#print(next(x))  # StopIteration


r = iter(range(3))  # iter() takes an iterable object and returns an iterator
print(type(r))
#<class 'range_iterator'>
print(next(r))
print(next(r))
print(next(r))
#print(next(r))  # StopIteration
