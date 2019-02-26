# input  test (console input)

print('이름을 입력하세요 : ', end="")
name = input()
print("이름 : {0}, type : {1}".format(name, type(name)))
name = input('이름을 입력하세요 : ')
print("이름 : {0}, type : {1}".format(name, type(name)))
name = input('아무것도 입력하지 말고 EOF(Ctrl+D 또는 Ctrl+Z+Enter)를 입력해보세요')
# EOF (ctrl+D/ctrl+Z+enter) 입력 시 EOFError 발생
