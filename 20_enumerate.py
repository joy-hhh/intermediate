# 리스트에 담긴 학생 이름을 정렬하고 1부터 번호를 매겨 딕셔너리에 번호, 이름으로
names = ['윤나은', '감현주', '장현지', '이지선', '박선주']

names.sort()
dnames = {}
i = 1
for n in names:
    dnames[i] = n
    i += 1
    
print(dnames)


# dictionary comprehension
names = ['윤나은', '감현주', '장현지', '이지선', '박선주']
dnames = {k : v for k, v in enumerate(sorted(names), 1)}
print(dnames)
