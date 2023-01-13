def add_last(m,n):
    m += n
    
r = [1,2]
add_last(r, [3,4])
print(r)

t = (1,3)
add_last(t, (5,7))
print(t)
### t가 참조하는 튜플과 함수 내의 변수 m이 참조하는 튜플은 별개의 것이 된다.

def add_tuple(t1, t2):
    t1 += t2
    return t1 # 새로 만들어진 튜플을 return으로 반환

tp = (1,3)
tp = add_tuple(tp, (5,7))
print(tp)
