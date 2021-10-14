# 불편한 코드
def pow(n):
    return n ** 2

st1 = [1,2,3]

st2 = [pow(st1[0]), pow(st1[1]), pow(st1[2])]
print(st2)

print()

# map 함수를 사용
st2 = list(map(pow, st1))
print(st2)

st = [1,2,3]
ir = map(pow, st)
for i in ir:   # ir은 iterator 객체이므로 for 루프에 올 수 있음
    print(i, end = ' ')

print()
print()

def dbl(e):
    return e * 2

print(list(map(dbl, (1,3,4))))   # 튜플에 map 전달
print(list(map(dbl, 'hello')))   # 문자열 'hello'를 map에 전달

print()

def sum(n1,n2):
    return n1 + n2

st10 = [1,2,3]
st20 = [3,2,1]
st30 = list(map(sum, st10, st20))
print(st30)

print()

# 슬라이싱
st = [1,2,3,4,5,6,7,8]
print(st[:])
print(st[: : 1])
print(st[: : 2])
print(st[: : 3])
print(st[: : -1])

print()

def rev(s):
    return s[: : -1]

st = ['one', 'two', 'three']
rst = list(map(rev, st))
print(rst)

rst = list(map(lambda s: s[: : -1], st))   # lambda로 완전히 같은 함수
print(rst)

print()

# filter
def is_odd(n):
    return n % 2

st = [1,2,3,4,5]
ost = list(filter(is_odd, st))
print(ost)

# lambda filter
ost = list(filter(lambda n: n % 2, st))
print(ost)

st = list(range(1,11))
fst = list(filter(lambda n: not(n%3), map(lambda n : n**2, st)))
print(fst)


