# 얕은 복사가 문제가 되는 경우

J2021 = ['John', ('man', 'USA'), [175,23]]
J2022 = list(J2021)
J2022[2][1] += 1
print(J2021)
print(J2022)


## copy 모듈로 깊은 복사 (deepcopy)

J2021 = ['John', ('man', 'USA'), [175,23]]
import copy
J2022 = copy.deepcopy(J2021)
J2022[2][1] += 1
print(J2021)
print(J2022)
print((J2021[0] is J2022[0]) and (J2021[1] is J2022[1]))
print(J2021[2] is J2022[2])
# immutable 객체를 대상으로는 얕은 복사가 진행되었고 mutable 객체를 대상으로는 깊은 복사가 진행되었다.


