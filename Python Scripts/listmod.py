def f(a, b):
    c = a
    a = b
    b = c

a = [1, 2, 3]
b = [4, 5, 6]
f(a, b)

print(a)
print(b)
