# set을 기반으로 하는 4가지 연산
a = {'a', 'c', 'd', 'f'}
b = {'a', 'b', 'd', 'e'}
print(a - b)   # 차집합
print(a & b)   # 교집합
print(a | b)   # 합집합
print(a ^ b)   # 대칭 차집합 (a-b) (b-a)


# set 함수에 iterable 객체 전달해서 set 생성
a = set(['a', 'c', 'd', 'f'])
b = set('fdca')

print(a == b)
print('a' in a)
print('b' not in a)

# iterable 객체이므로 for 루프의 구성 가능
for c in a & b:
    print(c, end = ' ')
    
print()

# 빈 딕셔너리 만드는 방법 : d = {}
# 빈 set 생성
s = set()
print(type(s))


# set : mutable 객체, frozenset : immutable 객체
a = frozenset(['a', 'c', 'd', 'f'])
b = frozenset(['a', 'b', 'd', 'e'])
print(a - b)

os = {1,2,3,4,5}
os.add(6)
os.discard(1)
print(os)

os.update({7,8,9})
os &= {2,4,6,8}
print(os)

os -= {2,4}
print(os)

os^= {1,3,6}
print(os)

# set comprehension
s1 = {x for x in range(1,11)}
print(s1)

s2 = {x**2 for x in s1}
print(s2)

s3 = {x for x in s2 if x <50}
print(s3)