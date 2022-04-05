from audioop import reverse


ns = [3,1,4,2]
ns.sort()
print(ns)

ns = [3,1,4,2]
ns.sort(reverse=True)
print(ns)

ns = [('Yoon', 33), ('Lee', 12), ('Park', 29)]
def age(t):
    return t[1]

ns.sort(key=age)
print(ns)

ns.sort(key=age, reverse=True)
print(ns)

ns = [('Yoon', 33), ('Lee', 12), ('Park', 29)]
def name(t):
    return t[0]

ns.sort(key=name)
print(ns)

# lambda 
ns = [('Yoon', 33), ('Lee', 12), ('Park', 29)]
ns.sort(key=lambda t: t[1], reverse=True)
print(ns)

names = ['Julia', 'Yoon', 'Steven']
names.sort(key=len)
print(names)

nums = [(3,1), (2,9), (0,5)]
nums.sort(key=lambda t: t[0]+t[1], reverse=True)
print(nums)

# sort 메서드는 리스트 자체를 수정해버린다.
# sorted 함수는 사본을 얻을 수 있고 튜플을 수정하여 리스트를 생성할 수 있다.

org = [('Yoon', 33), ('Lee', 12), ('Park', 29)]
cpy = sorted(org, key=lambda t : t[1], reverse=True)
print(org)
print(cpy)

org = (3,1,2)
cpy = sorted(org)
print(cpy)

org = (3,1,2)
cpy = tuple(sorted(org))
print(cpy)

# 문자열을 숫자로 인식하여 정렬
org = ('321', '214', '197')
cpy = tuple(sorted(org, key=lambda s: int(s[0])))
print(cpy)
