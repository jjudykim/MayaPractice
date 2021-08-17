# 마야에서 위치를 출력하면 기본적으로 소수점 15자리까지 나오게 된다.
# 너무 자세하게 필요하지 않을 때, 파이썬의 내장 함수인 round를 써서 소수점을 조절한다.
# round 함수는 round(입력, 출력하고자 하는 자릿수)로 사용한다.

# ex1
print(round(3.245, 2))

# ex2
print(round(3.245, 1))

x = 11.123
y = int(x)
print(y)

# 실수형을 정수로 만드는 방법은 소수점의 값에 상관없이 제거하는 방법 외에도 올림, 내림이 가능하다
# 올림, 내림을 위해서는 math 모듈에 들어있는 함수를 사용한다

# ceil() 함수 : 소수점 이하의 값의 크기에 상관없이 무조건 올림의 결과를 반환
import math
x = 11.123
y = math.ceil(x)
print(y)

# floor() 함수 : 소수점 이하의 값에 상관없이 무조건 내림을 시행
import math
x = 11.999
y = math.floor(x)
print(y)

# trunc() 함수 : 소수점 이하의 값을 버리고, 정수 부분만을 반환합니다.
import math
x = 11.999
y = math.trunc(x)
