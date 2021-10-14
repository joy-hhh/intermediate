tri_one = (12,15)
tri_two = 23, 12   # 소괄호 없이 튜플 생성

tri_three = (12,25)
bt, ht = tri_three
bt
ht

nums = 1,2,3,4,5
n1, n2, *others = nums   # 둘 이상의 값을 묶을 때 *를 사용
n1
n2
others   # 언패킹 되어 리스트로 묶인다


nums = 1,2,3,4,5
first, *others, last = nums
first
others
last


def show_nums(n1, n2, *other):   # 세 번째 이후 값들은 튜플로 묶여 other에 전달
    print(n1, n2, other, sep=', ')
    
show_nums(1,2,3,4)
show_nums(1,2,3,4,5)


def sum(*nums):   # 전달되는 모든 값들을 하나의 튜플로 묶어서 nums에 저장 (묶는다.)
    s = 0
    for i in nums:
        s += i
    return s

sum(1,2,3)
sum(1,2,3,4)
sum(1,2,3,4,5)

def show_man(name, age, height):
    print(name, age, height, sep= ', ')

p = ('Yoon', 22, 180)
show_man(*p) # p에 담간 값을 풀어서 각각의 매개변수에 전달! (호출할 때는 푼다.)

t = (1,2,(3,4))
a, b, (c, d) = t
print(a,b,c,d, sep = ', ')


# 튜플에서 일부 정보만 필요한 경우 관례 _ 로 변수 표시
p = 'Hong', (32, 178), '010-1234-56XX', 'Korea' # 32세 178cm의 한국에 사는 Hong
na, (ag, he), ph, ad = p
print(na, he)

na, (_, he), _, _ = p   # 불필요한 변수명 생략하는 기술 _
print(na, he)

# for 루프에서의 언패킹
ps = [('Lee', 172), ('Jung', 182), ('Yoon', 179)]
for n, h in ps:
    print(n, h, sep=', ')

