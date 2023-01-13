# 매개변수에 함수를 전달할 수 있다.
def say1():
    print('hello')

def say2():
    print('hi~')

def caller(fct):
    fct()   # fct를 통해 전달된 함수를 호출

caller(say1)
caller(say2)


# 같은 함수 내에서 함수를 만들어서 이를 반환할 수 있다.
def fct_fac(n):
    def exp(x):
        return x ** n
    return exp

f2 = fct_fac(2)
f3 = fct_fac(3)

print(f2(4))
print(f3(4))

# lambda

def show(s):
    print(s)

ref = show
ref('hi~')

ref = lambda s: print(s)
ref('oh~')

# 람다식으로 간결하게 함수 내 함수 구현
def fct_fac2(n):
    return lambda x: x ** n

f4 = fct_fac2(2)
f5 = fct_fac2(3)

print(f4(4))
print(f5(4))