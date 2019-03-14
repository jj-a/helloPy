# module test

# 모듈(Module) 사용하기
import datetime
import math     #  math module import (모듈명.함수명 호출)
import math as m        # math module 'm'으로 import (별명.함수명 호출)
from math import pi     # math module중 pi 함수만 import (함수명만 써서 호출)
from math import *      # math module의 모든 함수 import (함수명만 써서 호출)

# import datetime
now = datetime.datetime.now()
print(now)

# import math
print("The value of pi is", math.pi)

# import math as m
print("The value of pi is", m.pi)

# from math import pi
print("The value of pi is", pi)

# from math import *
print("The value of e is", e)
