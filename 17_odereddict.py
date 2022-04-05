d1 = dict(a = 1, b = 2, c = 3)
d2 = dict(c = 3, b = 2, a = 1)
print(d1 == d2)
# 순서가 다르지만 내용이 같으므로 True 산출

from collections import OrderedDict

from pyparsing import Or
od1 = OrderedDict(a = 1, b = 2, c = 3)
od2 = OrderedDict(c = 3, b = 2, a = 1)
print(od1 == od2)
# 순서가 다르므로 False 산출

od = OrderedDict(a = 1, b = 2, c =3)
od.move_to_end('b')
for kv in od.items():
    print(kv, end = ' ')
    
print()
od.move_to_end('b', last=False)
for kv in od.items():
    print(kv, end = ' ')


## 저장 순서 자체가 하나의 정보로써 의미를 갖는다면,
## 저장 순서를 바꿔야 할 가능성도 존재한다면,
## OrderedDict를 선택한다. 