# 클래스 변수

class Simple:
    count = 0
    def __init__(self):
        Simple.count += 1
    def get_count(self):
        return Simple.count
    
def main():
    s1 = Simple()
    print(s1.get_count())
    s2 = Simple()
    print(s1.get_count())
    s3 = Simple()
    print(s1.get_count())
    
main()

# static 메소드 (클래스에 속하는 메소드)

class Simple:
    def sm():
        print('static method!')
    sm = staticmethod(sm)   # sm 메소드를 staticmethod로 만드는 방법
    
def main():
    Simple.sm()    # staticmethod는 클래스 이름을 통해 호출 가능
    s = Simple
    s.sm()     # static 메소드는 객체를 통해서도 호출 가능
    
main()


class Simple:
    count = 0
    def __init__(self):
        Simple.count += 1
        
    @staticmethod
    def get_count():
        return Simple.count
    
def main():
    print(Simple.get_count())    # 객체가 없는 상태에서도 객체의 수를 물을 수 있다.
    s = Simple()
    print(Simple.get_count())
    
main()