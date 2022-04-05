fs = '{0}...{1}...{2}'
ms = fs.format('Robot', 125, 'Box')
print(ms)

my = ['Robot', 125, 'Box']
print('{0}...{1}...{2}'.format(*my))   # 인자 전달 과정에서 리스트 대상으로 언패킹


print('%f' % 3.14)
print('{0:f}'.format(3.14))
print('%.2f' % 3.14)
print('{0:.2f}'.format(3.14))
print('%9.2f' % 3.14)   # 9칸을 확보하고 오른쪽으로 붙여 출력
print('{0:9.2f}'.format(3.14))
print('{0:<10.2f}'.format(3.14))
print('{0:>10.2f}'.format(3.14))
print('{0:^10.2f}'.format(3.14))
print('{0:*^10.2f}'.format(3.14))  # 빈 공간 * 로 채움

