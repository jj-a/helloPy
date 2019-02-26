# input  test 2 (console input)

# 표준 입력
data = input("정수를 입력하시오 : ")
print(data, type(data))
# print(data, type(data), data + 1) 에러 문자열과 정수를 +(더하기)할 수 없습니다.

# eval() : 유효한 파이썬 표현식으로 변환
data = eval(input("정수를 입력하시오 : "))
print(data, type(data), data + 1)

# int() : 정수형으로 변환
data = int(input("2진수를 입력하시오 : "), 2)
print(data, type(data), data + 1)

data = int(input("8진수를 입력하시오 : "), 8)
print(data, type(data), data + 1)

data = int(input("10진수를 입력하시오 : "), 10)
print(data, type(data), data + 1)

data = int(input("16진수를 입력하시오 : "), 16)
print(data, type(data), data + 1)


data = input("실수를 입력하시오 : ")
print(data, type(data))
# 에러 문자열과 실수를 +(더하기)할 수 없습니다.
# print(data, type(data), data + 1.2)

data = eval(input("실수를 입력하시오 : "))
print(data, type(data), data + 1.2)

#  float() : 실수형으로 변환
data = float(input("정수를 입력하시오 : "))
print(data, type(data), data + 1.2)