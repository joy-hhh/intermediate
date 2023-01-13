# 스페셜 메소드 : 호출 시점이 약속된 메소드 (직접 그 이름을 명시하지 않고 다른 경로를 통해서 혹은 상황에 따라 자동으로 호출되는 메소드)
# __name__


t = (1,2,3)
print(len(t))   # t.__len__()

itr = iter(t)
for i in itr:
    print(i, end = ' ')
    
s = str(t)
print(s)

t = (1,2,3)
print(t.__len__())
itr = t.__iter__()
for i in itr:
    print(i, end=' ')

s = t.__str__()
print(s)


# 클래스에 스페셜 메소드 정의하기

class Car:
    def __init__(self, id):
        self.id = id
    def __len__(self):
        return len(self.id)
    def __str__(self):
        return 'Vehicle number : ' + self.id
    
def main():
    c = Car("32러5234")
    print(len(c))
    print(str(c))
    
main()


# iterable 객체가 되게끔 하기
class Car:
    def __init__(self, id):
        self.id = id
    def __iter__(self):
        return iter(self.id)
    
def main2():
    c = Car("32러5234")
    for i in c:
        print(i, end = ' ')
        
main2()

# iterator 객체가 되게끔 하기
class Coll:    ## 저장소 역할을 하는 클래스를 표현한 결과
    def __init__(self, d):
        self.ds = d
        self.cc = 0    # __next__ 메소드 호출 횟수
    def __next__(self):
        if len(self.ds) <= self.cc:
            raise StopIteration
        self.cc += 1
        return self.ds[self.cc -1]
    
def main3():
    co = Coll([1,2,3,4,5])
    while True:
        try:
            i = next(co)
            print(i, end = ' ')
        except StopIteration:
            break
        
main3()
   
# iterator 객체이자 iterable 객체가 되게끔 하기
class Coll2:
    def __init__(self, d):
        self.ds = d
    def __next__(self):
        if len(self.ds) <= self.cc:
            raise StopIteration
        self.cc += 1
        return self.ds[self.cc - 1]
    def __iter__(self):
        self.cc = 0
        print('iter 호출됨')
        return self   # 이 객체를 그대로 반환함
    
def main4():
    co = Coll2([1,2,3,4,5])
    for i in co:
        print(i, end = ' ')
    for i in co:
        print(i, end = ' ')

main4()




co = Coll2('hello')
itr = iter(co)
itr is co
