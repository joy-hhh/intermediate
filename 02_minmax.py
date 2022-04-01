def min_max(d):
    d.sort()   # 리스트를 오름차순으로 정렬
    print(d[0], d[-1], sep = ', ')   # 맨 앞의 값과 마지막 값을 출력

l = [3,1,5,4]
min_max(l)
print(l)   # 리스트의 순서가 변경되었다. 

# 순서를 변경하지 않아야 하는 경우에는 리스트를 복사한 다음 정렬

def min_max2(d):
    d = list(d)
    d.sort()
    print(d[0], d[-1], sep = ', ')

l = [3,1,5,4]
min_max2(l)
print(l)   # 원본이 수정되지 않았다.
