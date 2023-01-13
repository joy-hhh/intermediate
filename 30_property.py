
class Natural:
    def __init__(self, n):
        self.setn(n)
    def getn(self):
        return self.__n
    def setn(self, n):
        if(n<1):
            self.__n = 1
        else:
            self.__n = n
    n = property(getn, setn)    #### 프로퍼티 설정
    
def main():
    n1 = Natural(1)
    n2 = Natural(2)
    n3 = Natural(3)
    n1.n = n2.n + n3.n     ##### 프로퍼티 설정하면 이렇게 쓸 수 있다. 
                           #### n1.setn(n2.getn + n3.getn())
    print(n1.n)
    
main()


# property 객체 생성으로 같은 결과
class Natural:
    def __init__(self, n):
        self.setn(n)
    n = property()       ### 프로퍼티 객체 생성
    def getn(self):
        return self.__n
    n = n.getter(getn)       #### 바로 위의 getn 메소드를 게터로 등록
    def setn(self, n):
        if(n<1):
            self.__n = 1
        else:
            self.__n = n
    n = n.setter(setn)       #### 바로 위의 setn 메소드를 세터로 등록

    
main()


# property에 등록할 이름을 동일하게 두는 경우
class Natural:
    def __init__(self, n):
        self.n = n     # property n을 통하여 접근
    n = property()       
    def pm(self):          ## getn 을 pm으로 변경
        return self.__n
    n = n.getter(pm)       
    def pm(self, n):       ## setn 을 pm으로 변경
        if(n<1):
            self.__n = 1
        else:
            self.__n = n
    n = n.setter(pm)       

    
main()


# 데코레이터를 기반으로 프로퍼티를 지정하는 방법
# property에 등록할 이름을 동일하게 두는 경우
class Natural:
    def __init__(self, n):
        self.n = n       # property n을 통하여 접근
    @property
    def n(self):
        return self.__n
    @n.setter
    def n(self, n):
        if(n < 1):
            self.__n = 1
        else:
            self.__n = n

    
main()

