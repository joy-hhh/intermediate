
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


# 둘 이상의 클래스 상속 - 고려사항이 많아지므로 권하지 않는 기능
class Mother:
    def dive(self):
        print("so deep!")

class Son(Father, Mother):
    def jump(self):
        print("so high!")

def main():
    s = Son()
    s.run()
    s.dive()
    s.jump()
    
main()


# method overiding(자식 클래스가 동일한 부모 클래스 이름의 메소드를 정의하여 부모 메소드가 가려짐)과 super
class Father():
    def run(self):
        print("so fast, dad style")
        
class Son(Father):
    def run(self):
        print("so fast, son style!")
    def run2(self):
        super().run()  ## 부모 클래스의 run 호출 방법, 가려진 run 호출 방법
        
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
        super().__init__(id, f)    # 필수- Car의 init method 호출 
        self.cargo = c   # 차에 실려 있는 짐의 양
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