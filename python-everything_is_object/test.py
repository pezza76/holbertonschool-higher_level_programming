a = [1, 2, 3]

print(id(a) % 10)

a += [4]

print(a)
print(id(a) % 10)