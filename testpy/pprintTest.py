# pprint test 2 (console output)

from collections import OrderedDict
from pprint import pprint

quotes = OrderedDict([('Moe',  'A wise guy, huh?'), ('Larry', 'Ow!'), ('Curly', 'Nyuk nyuk!'), ])

print(quotes)  # 일반 출력
pprint(quotes)  # pprint 출력


print('-'*50)
######################


info = dict(name='kim', age=20, addr='yongin')

print(info)
print(*info)

# 출력 결과
# {'addr': 'yongin', 'age': 20, 'name': 'kim'}
# addr age name

print('-'*50)

print([k for k in info])
print([(k, info[k]) for k in info])
print(*[(k, info[k]) for k in info])

# 출력 결과
# ['addr', 'age', 'name']
# [('addr', 'yongin'), ('age', 20), ('name', 'kim')]
# ('addr', 'yongin') ('age', 20) ('name', 'kim')

print('-'*50)

print(*[(k, info[k]) for k in info], sep='\n')
print(*['{}: {}'.format(k, v) for k, v in info.items()], sep='\n')

# 출력 결과
# ('addr', 'yongin')
# ('age', 20)
# ('name', 'kim')
# addr: yongin
# age: 20
# name: kim

print('-'*50)

print('** pprint **')
pprint.pprint(info)
pprint.pprint(info, width=20)
pprint.pprint(info, width=20, indent=4)

# 출력 결과
# {'addr': 'yongin', 'age': 20, 'name': 'kim'}
# {'addr': 'yongin',
#  'age': 20,
#  'name': 'kim'}
# {   'addr': 'yongin',
#     'age': 20,
#     'name': 'kim'}

print('** pprint.PrettyPrinter **')
pp = pprint.PrettyPrinter(width=20, indent=4)
pp.pprint(info)

# 출력 결과
# {   'addr': 'yongin',
#     'age': 20,
#     'name': 'kim'}
