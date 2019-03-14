# assert test (디버깅)
# assert [condition], [message]

# assert 디버깅 목적으로 사용
# 조건이 True이면 아무것도 반환하지 않고, False이면 AssertionError를 반환
a = 10
assert a > 5, "a의 값이 정상입니다."
# assert a < 5
assert a < 5, "a의 값이 너무 큽니다."   # 출력

