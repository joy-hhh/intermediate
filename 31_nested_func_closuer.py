def maker(m):
    def inner(n):
        return m * n
    return inner

f1 = maker(2)
f2 = maker(3)

print(f1(7))
print(f2(7))


def maker(m):
    def inner(n):
        return m*n
    return inner

f1 = maker(101)
f2 = maker(75)

print(f1.__closure__[0].cell_contents)
print(f2.__closure__[0].cell_contents)

