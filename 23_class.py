# init 하지 않은 경우
class Simple:
    def seti(self, i):
        self.i = i
    def geti(self):
        print(self.i)

s1 = Simple()
s1.seti(200)
s1.geti()

## init 하지 않으면 seti로 i를 만들어 주지 않고 geti를 호출하면 에러가 발생한다. 

# init 하는 경우
class Simple:
    def __init__(self):
        self.i = 0
    def seti(self, i):
        self.i = i
    def geti(self):
        print(self.i)

s = Simple()
s.geti()
s.seti(25)
s.geti()

