# Iterable 객체와 Iterator 객체
ds = [1,2,3,4]
for i in ds:
    print(i, end = ' ')

ir = iter(ds)   # iterator 객체를 얻는 방법

print()
print(next(ir))
print(next(ir))
print(next(ir))
print(next(ir))
print(next(ir))


