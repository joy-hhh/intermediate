# while
ir = iter([1,2,3])
while True:
    try:
        i = next(ir)
        print(i, end = ' ')
    except StopIteration:
        break

# for
ir = iter([1,2,3])
for i in ir:
    print(i, end = ' ')

print()
print()

# object
ir1 = iter([1,2,3])
ir2 = iter(ir1)
print(ir1 is ir2)
print(ir1)
print(ir2)

# "iterable 객체와 iterator 객체 모두 for 루프의 반복 대상이 될 수 있다.
# "iterable 객체가 와야 하는 위치에는 iterator 객체가 올 수 있다.

