# turtle(Turtle graphics) test 2
import turtle

# 제목 변경
turtle.title('거북아 거북아')

# 거북이 색상 지정
turtle.color('black', 'yellow')
# 거북이 보여주기
turtle.shape('turtle')


# 함수 정의
def move(length):
        turtle.penup()
        turtle.forward(length)
        turtle.pendown()


move(-200)  # 함수 호출

# 사각형 그리기
for _ in range(4):  # 반복문
    turtle.forward(50)  # 앞으로 이동
    turtle.left(90) # 왼쪽으로 방향 전환

move(100)  # 함수 호출

# 도장 찍기
colors = ['red', 'green', 'yellow', 'blue']  # 리스트
for color in colors:
    turtle.color('black', color)    # 거북이 색상 변경
    turtle.forward(50)
    turtle.stamp()  # 도장 꽝

move(150)

# 삼각형 그리기
for i in range(3):
    turtle.left(120)
    turtle.color('black', colors[i])    # 거북이 색상 변경
    turtle.forward(100)
    turtle.stamp()  # 도장 꽝


# 클릭 시 종료(닫기)
turtle.exitonclick()
