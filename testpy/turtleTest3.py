# turtle(Turtle graphics) test 3
import turtle

# 제목 변경
turtle.title('거북아 거북아')

# 거북이 색상 지정
turtle.color('black', 'blue')
# 거북이 보여주기
# turtle.shape('turtle')


# 함수 정의
def move(length):
        turtle.penup()
        turtle.forward(length)
        turtle.pendown()


move(-300)  # 함수 호출

# 사각형 그리기
for i in range(3, 15):  # 반복문
    turtle.begin_fill()
    turtle.circle(20, steps=i)
    move(50)
    turtle.end_fill()


# 클릭 시 종료(닫기)
turtle.exitonclick()
