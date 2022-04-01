

d = {'a' :1, 'b' :2, 'c' :3}
print(d)
print(type(d))

d_dict = dict([('a',1), ('b',2), ('c',3)])
print(d_dict)

d_dict = dict(a = 1, b = 2, c = 3)
print(d_dict)

d_dict_zip = dict(zip(['a', 'b', 'c'], [1,2,3]))
print(d_dict_zip)
print(d == d_dict == d_dict_zip)

d['d'] = 4   # 추가된 값은 맨 뒤에 저장된다.
print(d)
for k in d:
    print(d[k], end = ', ')

# zip example 1
z = zip(['a','b','c'], [1,2,3])
for i in z:
    print(i, end = ', ')

# zip example 2
z = zip(('a','b','c'), (1,2,3))  # 두 개의 튜플 조합
for i in z:
    print(i, end = ', ')

# zip example 3
z = zip('abc', (1,2,3))
for i in z:
    print(i, end = ', ')



