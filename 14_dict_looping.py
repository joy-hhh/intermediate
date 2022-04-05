d = dict(a = 1, b = 2, c = 3)
for k in d:
    print(d[k], end=', ')
    
for k in d.keys():
    print(k, end=', ')
    
for v in d.values():
    print(v, end = ', ')

print()
print()

for k, v in d.items():
    print(k, v, sep=', ')
    
# list comprehension
r1 = [1,2,3,4,5]
r2 = [x*2 for x in r1]
print(r2)

# dict comprehension
d1 = d
d2 = {k : v*2 for k, v in d1.items()}
d3 = {k : v*2 for k, v in d2.items()}

print(d2)
print(d3)

# 두 리스트에 저장되어 있는 값들을 이용해서 딕셔너리 생성
ks = ['a', 'b', 'c', 'd']
vs = [1,2,3,4]

ds = {k : v for k, v in zip(ks, vs)}
print(ds)

## 홀수만 남기기
ds = {k : v for k, v in zip(ks, vs) if v % 2}
print(ds)