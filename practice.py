import copy

a = [1,2,3,4,5]

b = copy.copy(a)

b[0] = 9

print(a)
print(b)