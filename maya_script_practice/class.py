# 클래스는 파이썬에서 객체지향 프로그래밍(OOP)을 구현하는 도구이다.
# 객체지향 프로그래밍은 프로그램을 단순히 데이터와 처리 방법으로 나누는 것이 아니라, 프로그램을 수많은 '객체'라는 기본 단위로 나누고
# 이 객체들의 상호작용으로 서술하는 방식이다.
# 객체란 하나의 역할을 수행하는 데이터의 묶음이다.
class clcl:
    pass

class mate_:
    def func_1(self):
        print("클래스 mate_의 첫 번째 함수입니다~")
    def func_2(self):
        print("클래스 mate_의 두 번째 함수입니다~")

run = mate_()
# run이라는 임의의 변수에 mate_라는 클래스를 호출(instance)한다.
run.func_1()
# 클래스가 호출된 run에 점을 찍고, 클래스 안의 함수의 이름을 쓰면 함수가 호출된다.
run.func_2()
# 같은 방법으로 클래스 안의 func_2라는 함수를 호출한다.

# 클래스에서 정의하는 변수를 속성, 함수를 메소드라고 한다.
# 메소드는 첫 번째 인자로 self를 전달한다.
# self는 하나의 클래스에서 만들 여러 객체(인스턴스)를 구별하기 위해 사용된다.
# 다른 이름을 써도 되지만, 관행으로 self를 주로 사용한다.



# 생성자와 소멸자 ===============================
# 객체가 만들어질 때 호출되는 함수를 생성자라고 하며, __init__로 표시한다. 생성자는 객체를 초기화할 때 사용된다.
# 객체가 사라질 때 호출되는 함수를 소멸자라고 하며, __del__로 표시한다.
class mate_:
    name = "sds"
    age = 17
    def __init__(self, name, age):
        print("생성자 호출 완료!!")
        self.name = name
        self.age = age
    def __del__(self):
        print("소멸자 호출 완료!!")
    def inform(self):
        print(f"저의 이름은 {self.name} 입니다~")
        print(f"나이는 {self.age}살 입니다~")

run = mate_("dongsun", 19)
run.inform()
del run

# x, y, z값을 넣고, 출력하는 클래스를 만들어보자.
import math
class vector_(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def length(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    def __add__(self, vec):
        return vector_(self.x + vec.x, self.y + vec.y, self.z + vec.z)

vec = vector_(0, 1, 2)
print(vec.x)
print(vec.y)
print(vec.z)

vec_a = vector_(0, 1, 2)
vec_b = vector_(2, 4, 10)
print(vec_a.x, vec_a.y, vec_a.z)
print(vec.b.x, vec_b.y, vec_b.z)

vec_a = vector_(0, 1, 2)
vec_b = vector_(2, 4, 8)
vec_c = vec_a + vec_b
print(vec_c.x, vec_c.y, vec_c.z)

# 사칙연산
class love_calculator:
    def data_in(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        print("add = ", end = "")
        return result
    def mul(self):
        result = self.first * self.second
        print("mul = ", end = "")
        return result
    def sub(self):
        result = self.first - self.second
        print("sub = ", end = "")
        return result
    def div(self):
        result = self.first / self.second
        print("div = ", end = "")
        return result

run = love_calculator()
run.data_in(10, 5)
print(run.add())
print(run.mul())
print(run.sub())
print(run.div())