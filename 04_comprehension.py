r1 = [1,2,3,4,5]
r2 = []

# for loop
for i in r1:
    r2.append(i * 2)

print(r2)

# list comprehension
r3 = [x * 2 for x in r1]
print(r3)

r4 = [x + 10 for x in r1]
print(r4)

# 조건 필터 추가하기
r5 = []
for i in r1:
    if i % 2:
        r5.append(i * 2)

print(r5)

# if list comprehension
r5 = [x * 2 for x in r1 if x %2]   # if절이 추가된 list comprehension
print(r5)

# 중첩 for
r1 = ['Black', 'White']
r2 = ['Red', 'Blue', 'Green']
r3 = []
for t in r1:
    for p in r2:
        r3.append(t + p)

print(r3)

# 중첩 list comprehension
r3 = [t + p for t in r1 for p in r2]
print(r3)

r = [n * m for n in range(2,10) for m in range(1,10)]
print(r)

# 이중 for loop에 조건 필터 추가
r = [n * m for n in range(2,10) for m in range(1,10) if ( n * m ) % 2]
print(r)   # 결과가 홀수인 값들만 리스트에 포함시킨 예


