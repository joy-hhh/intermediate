class Simple:
    pass

s = Simple()

# 이 객체는 저 클래스의 객체인가?
print(isinstance(s, Simple))
print(isinstance([1,2], list))

# 파이썬의 모든 클래스는 object 클래스를 직접 혹은 간접 상속한다.
print(isinstance(Simple, object))


class A:
    pass

class Z(A):
    pass

issubclass(Z,A)

issubclass(type, object)

print(dir(object))

