from inspect import classify_class_attrs
from matplotlib.pyplot import cla


class Father:
    def run(self):
        print("so fast!!")
    
class Son(Father):
    def jump(self):
        print("so high!!")
        
def main():
    s = Son()
    s.run()
    s.jump()
    
main()

# method overiding
class Father():
    def run(self):
        print("so fast, dad style")
        
class Son(Father):
    def run(self):
        print("so fast, son style!")
    def run2(self):
        super().run()
        
def main():
    s = Son()
    s.run()
    s.run2()
    
main()

# 메소드 오버라이딩을 하면서 동시에 가려진 메소드를 호출해야만 하는 상황
class Car:
    def __init__(self, id, f):
        self.id = id
        self.fuel = f
    def drive(self):
        self.fuel -= 10
    def add_fuel(self, f):
        self.fuel += f
    def show_info(self):
        print("id:", self.id)
        print("fuel:", self.fuel)

class Truck(Car):
    def __init__(self, id, f, c):
        super().__init__(id, f)
        self.cargo = c
    def add_cargo(self, c):
        self.cargo += c
    def show_info(self):  
        super().show_info()   # Car의 show_info method 호출
        print("cargo:", self.cargo)   # 기능보강
        


def main():
    t = Truck("42럭5959", 0, 0)
    t.add_fuel(100)
    t.add_cargo(50)
    t.drive()
    t.show_info()
    
main()