r = [1,2]
print(id(r))    # 리스트의 주소 정보 확인
r += [3,4]      # 리스트에 값을 추가
print(r)
print(id(r))    # 리스트의 주소가 바뀌지 않았음을 확인

t = (1,2)
print(id(t))
t += (3,4)      # 새로운 튜플이 만들어짐
print(t)
print(id(t))    # t에 저장된 튜플이 바뀌었음을 확인

