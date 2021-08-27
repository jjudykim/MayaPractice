# 함수
# 프로그래밍을 하다 보면 똑같은 내용을 반복하는 경우가 있는데, 이때 함수가 필요하다.
# 함수를 사용하는 또 다른 이유는 프로그램을 함수화하면 프로그램의 흐름을 일목요연하게 볼 수 있기 때문이다.
# 함수를 쓰면 프로그램의 흐름을 잘 파악할 수 있고 오류가 생기는 부분도 쉽게 알아낼 수 있다.

# 함수 만들기
def a():
    print("함수 a입니다~")
def b():
    print("함수 b입니다~")

a()
b()

_list = [1, 2, 3]
a = len(_list)    #len함수의 역할을 보여주는 코드엿다..!
print(a)

def my_first_func():
    i = 10
    return i

print(my_first_func())


# 함수의 변수를 글로벌로 정의하기
# 변수를 글로벌로 정의하면 하나의 변수를 여러 함수에서 사용할 수 있다.
number = 10
def increase():
    global number            #전역변수 number에 접근하기 위해 global을 써야 합니다.
    number = number + 1

def decrease():
    global number
    number = number - 1

print("=============")
print (number)
increase()
print (number)
increase()
print (number)
decrease()
print (number)
decrease()
print (number)
decrease()
print (number)



# 오브젝트의 이름을 바꾸는 함수 =================================
# import maya.cmds as cmds
# def arr_(name_, st_number):
#     sel_ = cmds.ls(sl = 1)
#     for serial in sel_:
#         cmds.rename(serial, name_ + str(st_number))
#         st_number = st_number + 1
# arr_("sds_", 100)



# 값을 받아서 계산해서 돌려주는 함수 만들기
def my_first_func(give_me):
    i = 5 + give_me
    print(i)
    return i

my_first_func(1000)

def add(n1, n2):
    result = n1 * n2
    return result

print(add(10, 15))



# 리스트를 받아서 리스트의 내용을 바꾸는 함수 ========================
def changeList(lst1):
    print("Original value:", lst1)      # 받은 리스트의 내용을 출력
    lst1[0] = 55                        # 리스트의 첫번째 값에 55를 넣는다
    print("Changed value:", lst1)       # 바뀐 리스트의 내용을 출력
    return lst1                         # 바뀐 리스트를 돌려준다

lst1 = [22, 33, 44]                     # 리스트를 하나 만들었음!
changeList(lst1)                        # changeList라는 함수에 리스트를 보낸다
print("Returned value:", lst1)          # 돌려받은 리스트를 출력한다