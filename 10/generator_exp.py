# 제네레이터 표현식의 문법 구성이 리스트 컴프리헨션과 거의 똑같다.

def show_all(s):
    for i in s:
        print(i, end = ' ')
        
st = [2 * i for i in range(1,10)]   # 리스트 컴프리헨션으로 구구단 2단 리스트 생성
show_all(st)

# 제네레이터 함수
def times2():
    for i in range(1,10):
        yield 2 * i
        
g = times2()
show_all(g)

 # 제네레이터 표현식
 g = (2* i for i in range(1,10))   # 대괄호는 리스트 컴프리헨션, 소괄호는 제네레이터 표현식
 show_all(g)

next(g) 

def two():
    print('two')   # two 함수 호출 시에 two라는 문자열 출력
    return 2

g = (two() * i for i in range(1,10))

next(g)

# 제네레이터 표현식을 직접 전달하기
def show_all(s):
    for i in s:
        print(i, end = ' ')
        
show_all(2** i for i in range(1,10))