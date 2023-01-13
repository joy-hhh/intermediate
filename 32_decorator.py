def smile():
    print("^_^")
    
def confused():
    print("@_@")
    
smile()
confused()

def deco(func):     # 데코레이터 함수, 줄여서 데코레이터
    def df():
        print('emoticon!')   # 추가된 기능
        func()               # 원래 갖고 있던 기능
        print('emoticon!')   # 추가된 기능
    return df

smile = deco(smile)    # 정의된 smile 함수를 데코레이터에 통과 시킴
smile()

confused = deco(confused)
confused()

def adder2(n1, n2):   # 전달 인자가 두 개인 함수
    return n1 + n2

def adder3(n1, n2, n3):   # 전달 인자가 세 개인 함수
    return n1 + n2 + n3

print(adder2(3,4))
print(adder3(3,5,7))



def adder_deco(func):   # 데코레이터 함수
    def ad(*args):      # 전달 인자를 튜플로 묶는다. - 튜플 패킹
        print(*args, sep = ' + ', end=' ') 
        print("= {0}".format(func(*args)))   # 풀어서 전달해주기. - 튜플 언패킹
    return ad    

adder2 = adder_deco(adder2)
adder3 = adder_deco(adder3)

adder2(3,4)
adder3(1,2,3)

# 필요한 데코레이터가 이미 존재하는 상황에서 지금 정의하는 함수를 그 데코레이터에 통과

@adder_deco
def adder2(n1, n2):
    return n1 + n2

@adder_deco
def adder3(n1, n2, n3):
    return n1 + n2 + n3

def main():
    adder2(3,4)
    adder3(3,5,7)
    
main()

# 데코레이터 함수 두 번 이상 통과하기
def deco1(func):
    def inner():
        print('deco1')
        func()
    return inner

def deco2(func):
    def inner():
        print('deco2')
        func()
    return inner

@deco1
@deco2
def simple():
    print('simple')
    
simple()
