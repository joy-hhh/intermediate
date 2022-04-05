# 스페셜메소드 : 호출 시점이 약속된 메소드
t = (1,2,3)
print(len(t))
itr = iter(t)
for i in itr:
    print(i, end = ' ')
    
s = str(t)
print(s)

print(t.__len__())
itr = t.__iter__()
for i in itr:
    print(i, end=' ')

s = t.__str__()
print(s)
