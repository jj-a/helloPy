# print test 2 (console output)

# Zero-fill (남는 공간을 0으로 채움)
print('12'.zfill(5))
print('-3.141'.zfill(7))
print('문자열'.zfill(10))
print('-' * 40)

# {:길이} : 출력할 데이터의 길이를 지정합니다. (default: 문자열=왼쪽 정렬, 숫자=오른쪽 정렬)
# {:<길이} : 왼쪽 정렬  /  {:>길이} : 오른쪽 정렬  /  {:^길이} : 가운데 정렬
print('Python is [{:15}]'.format('good'))
print('Python is [{:<15}]'.format('good'))
print('Python is [{:>15}]'.format('good'))
print('Python is [{:^15}]'.format('good'))
print('당신의 나이는 [{:8}]세'.format(27))
print('당신의 나이는 [{:<8}]세'.format(27))
print('-' * 40)

# 왼쪽 정렬
for x in range(1, 4):
    print('[{0:2d}] [{1:3d}] [{2:4d}]'.format(x, x*x, x*x*x))
print()

# 가운데 정렬
for x in range(1, 4):
    print('[{0:^2d}] [{1:^3d}] [{2:^4d}]'.format(x, x*x, x*x*x))
print()

# 오른쪽 정렬
for x in range(1, 4):
    print('[{0:<2d}] [{1:<3d}] [{2:<4d}]'.format(x, x*x, x*x*x))
print()

# 0으로 채우기
for x in range(1, 4):
    print('[{0:02d}] [{1:03d}] [{2:04d}]'.format(x, x*x, x*x*x))
print()

# 부호 출력
print('[{0:05d}] [{1:05d}] [{2:05d}]'.format(1, -2, 3))    # 음수만 부호
print('[{0:+05d}] [{1:+05d}] [{2:+05d}]'.format(1, -2, 3))  # 부호
print('[{0:<5d}] [{1:<5d}] [{2:<5d}]'.format(1, -2, 3))     # 정렬
print('-' * 40)

