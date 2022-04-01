# map과 filter를 대신하는 리스트 컴프리헨션

# map 사용
st1 = [1,2,3]
st2 = list(map(lambda n: n ** 2, st1))
print(st2)

# list comprehension
st3 = [n ** 2 for n in st1]
print(st3)

# map 사용
st = [1,2,3,4,5]
ost = list(filter(lambda n: n % 2, st))
print(ost)

# list comprehension
ost = [n for n in st if n % 2]    # 홀수만 남겨서 리스트로 묶음
print(ost)

# 홀수 제곱 리스트 map, filter
st = list(range(1, 11))
fst = list(map(lambda n: n**2, filter(lambda n: n % 2, st)))
print(fst)

# 홀수 제곱 list comprehension
fst = [n**2 for n in st if n%2]
print(fst)


