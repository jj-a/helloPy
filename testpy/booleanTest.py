# boolean (True/False)  & null(None) test

# 참/거짓
# 첫글자 대문자로 작성 (True, False)
print("참 : ", True)
print("거짓 : ", False)
print(1 == 1)
print(3 > 5)
print(3 < 5)
print(True or False)
print(True and False)
print(not False)
print(True == 1)
print(False == 0)
print(True + True)

# None
print("None : ", None)
print(None == 0)
print(None == [])
print(None == False)
print(None == "")
x = None
y = None
print(x == y)

# 아무값도 리턴하지 않는 함수
def void_function():
    a = 10
    b = 20
    c = a + b

result = void_function()
print(result)
print("값이 없음" if result ==None else result)
# x==None을 수행할 때는 가급적 is None 으로 쓸 것



