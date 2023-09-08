a = [1, 2]
b = []
b.append(a)
b.append(a)
b.append(a)

print(b)  # [[1, 2], [1, 2], [1, 2]]
print(len(b))  # 3
b[1][1] = 3
print(b)  # [[1, 3], [1, 3], [1, 3]]
print(a)  # [1, 3]

a[1] = 2
print(b)  # [[1, 2], [1, 2], [1, 2]]
print(a)  # [1, 2]


