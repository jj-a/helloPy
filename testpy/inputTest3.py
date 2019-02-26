# input  test 3 (console input)

# 튜플(tuple), 리스트(list)로 입력받기

# eval() : 유효한 파이썬 표현식으로 변환
string = input("(1,2) 형식으로 입력하시오 ")
print(string, type(string))

string = eval( input("(1,2) 형식으로 입력하시오 "))
print(string, type(string))  # list

string = input("[1,2,3,4,5,6] 형식으로 입력하시오 ")
print(string, type(string))

string = eval( input("[1,2,3,4,5,6] 형식으로 입력하시오 "))
print(string, type(string))     # tuple

