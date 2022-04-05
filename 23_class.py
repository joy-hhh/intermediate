class Simple:
    def seti(self, i):
        self.i = i
    def geti(self):
        print(self.i)

s1 = Simple()
s1.seti(200)
s1.geti()

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

