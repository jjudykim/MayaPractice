# 상속(Inheritance)이란 "물려받다"라는 뜻으로,
# 어떤 클래스를 만들 때 다른 클래스의 기능을 그대로 물려받을 수 있다.
# 보통 기존의 클래스를 변경하지 않고 기능을 추가하거나 변경하려고 할 때 사용한다.
# 기존의 클래스가 라이브러리 형태로 제공되거나 수정이 불가능한 상황일 때 상속을 사용한다.

# class 클래스 이름(상속할 클래스 이름)

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
        print("div = ")
        if self.second == 0:
            return 0
        else:
            result = self.first / self.second
            return result

class heir_(love_calculator):
    def pow(self):
        result = self.first ** self.second
        print("pow = ")
        return result

#heir_라는 클래스는 love_calculator라는 클래스를 상속했기 때문에 모든 기능을 쓸 수 있다. 다음처럼,,
runrun = heir_()
runrun.data_in(4, 2)
print(runrun.pow())


# 메소드 오버라이딩 ========================================
run  = love_calculator()
run.data_in(2,0)
print(run.add())
print(run.mul())
print(run.sub())
#print(run.div())
# div()에서 에러가 발생한다. 예외 처리 넣어주기!

# 아니면 새로운 클래스를 만들어서 기존의 클래스를 상속받고, 새로운 내용을 추가해준다
class received__calculator(love_calculator):
    def div(self):
        print("div = ")
        if self.second == 0:
            return 0
        else:
            result = self.first/self.second
            return result

run = received__calculator()
run.data_in(2, 0)
print(run.add())
print(run.mul())
print(run.sub())
print(run.div())

#received__calculator 클래스는 love_calculator 클래스에 있는 div 메서드를 동일한 이름으로 다시 만든 것이다.
# 이렇게 부모 클래스(상속한 클래스)에 있는 메소드를 동일한 이름으로 다시 만드는 것을 메소드 오버라이딩이라고 한다.
# 이렇게 메소드 오버라이딩을 하면 부모 클래스의 메소드 대신 오버라이딩한 메소드가 호출된다.



# 클래스 변수 =====================================
class class_variable:
    drink = "cola"

print(class_variable.drink)
a = class_variable
print(a.drink)

class_variable.drink = "water"
print(class_variable.drink)
