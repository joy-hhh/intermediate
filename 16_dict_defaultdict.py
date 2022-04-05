# 상황별 실행 코드 구분
s = 'robbot'
d = {}
for k in s:
    if k in d:
        d[k] += 1
    else:
        d[k] = 1

print(d)

# setdelault
d = {}
for k in s:
    d[k] = d.setdefault(k, 0) +1

print(d)

# defaultdict
from collections import defaultdict
d = defaultdict(int)   # int 함수를 등록하면서 defaultdict 호출
for k in s:
    d[k] += 1

print(d)
print(d['r'], d['o'], d['b'], d['t'], sep=', ')

def ret_zero():
    return 0

d = defaultdict(ret_zero)
d['a']
print(d)

d = defaultdict(lambda : 7)
d['z']
print(d)
