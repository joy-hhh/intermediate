# 제네레이터 함수(function)
# 제네레이터 표현식(expression)

def gen_num():
    print('first number')
    yield 1   # yield가 하나라도 들어가면 제네레이터
    print('second number')
    yield 2
    print('third number')
    yield 3

gen = gen_num()   # 제네레이터 객체 생성

type(gen)

next(gen)
next(gen)
next(gen)

def pows(s):
    r = []
    for i in s:
        r.append(i ** 2)
    return r

st = pows([1,2,3,4,5,6,7,8,9])
for i in st:
    print(i, end = ' ')

import sys
print(sys.getsizeof(st))


