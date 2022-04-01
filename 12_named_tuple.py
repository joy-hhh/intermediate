tri_one = (12,15) # 삼각형 밑변 12와 높이 15를 묶어 놓은 것

from collections import namedtuple
Tri = namedtuple('Triangle', ['bottom', 'height'])
t = Tri(3,7)
print(t[0], t[1])
print(t.bottom, t.height) # 일반 튜플과 달리 이름으로 접근 가능

Tri = namedtuple('Tri', 'bottom height')
t2 = Tri(4,8)
print(t2.bottom, t2.height)

