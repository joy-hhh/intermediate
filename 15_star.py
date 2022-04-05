def who(a,b,c):
    print(a,b,c, sep=', ')
    
who(*[1,2,3])
who(*(0.1,0.2,0.3))
who(*'abc')

d = dict(a = 1, b = 2, c = 3)
who(*d)   # *을 붙이면 키가 매개변수에 전달
who(**d)   # **을 붙이면 값이 매개변수에 전달

who(*(d.items()))   # items 함수를 호출해서 뷰 객체를 얻는다.

# def func(*args) 값들이 튜플로 묶여서 args에 전달된다.
# def func(**args) 전달되는 내용이 딕셔너리로 묶여서 args에 전달된다.

def func(*args):
    print(args)
    
func()
func(1)
func(1,2)
func(1,2,3)

def func(**args):
    print(args)
    
# key = value 형태로 전달해야 한다. 
func(a = 1)
func(a = 1, b =2)
func(a = 1, b =2, c = 3)



