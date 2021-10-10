# copy 모듈로 깊은 복사 (deepcopy)

J2021 = ['John', ('man', 'USA'), [175,23]]
import copy
J2022 = copy.deepcopy(J2021)
J2022[2][1] += 1
print(J2021)
print(J2022)
print((J2021[0] is J2022[0]) and (J2021[1] is J2022[1]))
print(J2021[2] is J2022[2])


