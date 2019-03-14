# turtle(Turtle graphics) test
import turtle   #as trtl

# 제목 변경
turtle.title('거북아 거북아')

# 일시정지
#turtle.done()

# 거북이 색상 지정
turtle.color('black','pink')
# 거북이 보여주기
turtle.shape('turtle')

turtle.stamp()  #도장찍기

# 달이 밝았습니다. 거북이는 펜을 들어주세요 [penup()] or [pu()]
turtle.penup();

# 거북이 옆에 문자열 출력
turtle.write("꼬북꼬북")

# 앞으로 80 이동 [foward(이동거리)] or [fd(이동거리)]
turtle.forward(80)

turtle.color('black', 'green')
turtle.stamp()  #도장찍기

# 펜 내려주세요 [pendown()] or [pd()]
turtle.pendown();

# 뒤로 100 이동 [backward(이동거리)] or [back(이동거리)] or [bk(이동거리)]
turtle.backward(100)

# 방향 전환 [right(각도)] or [rt(각도)] or [left(각도)] or [lt(각도)]
#turtle.left(180)

turtle.color('black','yellow')
turtle.stamp()  #도장찍기

# 펜을 들고 이동하면 이동하는 선이 그려지지 않고, 내리고 이동하면 선이 그려짐
turtle.left(90); turtle.fd(20);
turtle.right(90); turtle.fd(100);
turtle.right(90); turtle.fd(20);
turtle.right(90); turtle.fd(100);

turtle.left(180)

turtle.color('black','red')
turtle.stamp()  #도장찍기

# 클릭 시 종료(닫기)
turtle.exitonclick()
