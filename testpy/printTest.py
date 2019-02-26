# print test (console output)

print("하나", "두울", "세엣", 1, 2, 3)
print("하나", "두울", "세엣", 1, 2, 3, sep='-')   # sep='구분자' (default: ' ')

# 다른 줄에 출력
print("AAA")
print("BBB")

# 한줄에 출력
print("CCC", end=" -> ")    # end='마지막 출력문자' (default: '\n')
print("DDD")

# 출력 방향 변경 (default: sys.stdout)
file = open("print.txt", "w")
print("Hello Python!!", file=file)   # 파일로 출력 (print.txt)
file.close()

print("Hello Python!")
print('-'*40)   # 문자열 반복 출력 (문자열*횟수)

# Formatting
# '출력 {} 문자열'.format('괄호 안에 들어갈 문자열')
# '출력 {0}{1}{2}'.format('문자열1', '문자열2', '문자열3')
print('id = {}'.format('jj-a'))
print('email = {0}@{1}.{2}'.format('jxxbom', 'gmail', 'com'))
print('id = {id} / email = {email}'.format(email='jxxbom@gmail.com', id='jj-a'))

