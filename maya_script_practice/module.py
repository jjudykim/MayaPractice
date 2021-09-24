# 파이썬에서 자주 사용하거나 유용한 함수, 클래스, 변수를 모아 놓은 파일이 모듈(Module)이다.
# 보통 하나의 파이썬 .py 파일이 하나의 모듈이 된다.
# 모듈 안에는 함수, 클래스, 혹은 변수들이 정의될 수 있고 실행 코드를 포함할 수도 있다.

# 내장 모듈 확인하기 ================
help('modules')



# 모듈의 사용 ======================
# import 모듈
# import 모듈1, 모듈2, 모듈3...
# import 모듈이름 as 별명

# 모듈의 모든 내용을 부르지 않고 함수만 부르기 위해서는 다음처럼 쓸 수 있다
# from 모듈 import 함수
# from 모듈 improt 함수1, 함수2, 함수3...
# from 모듈 import *
# from 모듈 import 함수 as 별명

# 다음처럼 모듈을 부르고, 모듈의 함수를 사용할 수 있다
import datetime
# 날짜에 관한 내용이 있는 datetime이라는 모듈을 부른다

import datetime as dt
# datetime 모듈을 부르고 dt라는 별명을 붙인다

import math
# 수학에 관한 내용이 있는 math라는 모듈을 부른다

import math as m
# math 모듈을 부르고 m이라는 별명을 붙인다

from math import pi
# math 모듈의 pi 함수를 부른다

from math import pi as boss
# math의 pi 함수를 부르고 boss라는 별명을 붙인다

from math import *
# math 모듈 전체를 부른다

print(datetime.datetime.now())
# datetime 모듈의 함수를 써서 현재의 날짜를 출력한다
print(dt.datetime.now())
# datetime 모듈의 별명인 dt를 써서 현재의 날짜를 출력한다
print("pi is", math.pi)
# math 모듈의 pi 함수를 써서 원주율을 출력한다
print("pi is", m.pi)
# math 모듈의 별명인 m을 써서 pi 함수를 부르고 원주율을 출력한다
print("pi is", boss)
# math 모듈의 pi 함수의 별명인 boss를 써서 원주율을 출력한다
print("pi is", pi)
# math 모듈의 pi 함수를 불러서 원주율을 출력한다



# 모듈 위치 확인하기 ==============================
import sys
print(sys.path)



# 모듈 생성하고 불러와 실행하기 =====================
import name as n
print(n.name_1())
print(n.name_2())



# 난수 모듈 ======================================
import random
print(random.random())

# random 모듈의 random() 함수는 0 이상 1 미만의 숫자 중에서 아무 숫자나 하나 뽑아서 돌려준다
# 주사위처럼 1에서 6까지의 정수 중 하나를 무작위로 얻으려면 randrange() 함수를 써서 편하게 할 수 있다

import random
print(random.randrange(1, 7))    # 1 이상 7 미만의 난수

import random
test_data = ["a", "b", "c", "d", "e"]
random.shuffle(test_data)
print(test_data)
# test_data 라는 리스트에 들어있는 항목이 무작위로 섞여있다

import random
test_data = ["a", "b", "c", "d", "e"]
print(random.choice(test_data))
# 리스트에 있는 항목을 무작위로 하나 뽑아주는 choice라는 함수도 있다

import random
test_data = ["a", "b", "c", "d", "e"]
print(random.sample(test_data, 3))
# 리스트 또는 튜플에서 특정 개수의 항목을 추출할 수 있다.

import random
test_data = {"a", "b", "c", "d", "e"}
print(random.sample(test_data, 3))
# 튜플에서는 이렇게 추출!


# 이 외에도 다음과 같은 함수를 사용할 수 있습니당~
# randint(최소, 최대) : 최소부터 최대까지의 수 중에서 임의의 정수를 리턴.
# uniform(최소, 최대) : 최소부터 최대까지의 수 중에서 임의의 부동소수점(float) 숫자를 돌려줌



# 오브젝트를 무작위로 선택하기==============================
# 먼저 다음 코드를 입력해 16개의 큐브를 만들고 정렬한다
import maya.cmds as cmds
for i in range(0, 4):
    # 4회 반복하면서
    for j in range(0, 4):
        # 각 반복에서 4회 반복!
        cmds.polyCube()           # 폴리콘 큐브를 만든다
        cmds.move(i*2, 1, j*2)    # 만든 큐브를 x, y, z 방향으로 옮긴다

# 16개의 큐브를 선택하고 다음을 실행한다
import maya.cmds as cmds
select_object = cmds.ls(sl = 1)   # 이 결과로 select_object 라는 리스트에 선택한 모든 큐브가 담김

# 큐브를 무작위로 선택하기 위해서는 리스트에 들어있는 목록을 무작위로 섞어야 한다
# 이를 위해선 random 모듈을 불러와 명령어를 사용해야 한다
import random
random.shuffle(select_object)        # shuffle 명령을 써서 select_object 라는 리스트의 목록을 섞는다

# 바뀐 리스트의 내용 확인!
select_object

# shuffle 명령을 써서 리스트의 목록을 섞고, 섞인 상태에서 리스트이 앞에서부터 4개를 선택한다!
cmds.select(select_object[:4])

# 계속 다른 것을 선택하기 위해서는 다시 한 번 더 섞고, 앞에서부터 목록을 선택하면 된다
import maya.cmds as cmds
import random
random.shuffle(select_object)
cmds.select(select_object[:4])



# 오브젝트를 많이 만들고 랜덤으로 퍼뜨리기 ===================
import maya.cmds as cmds
import random
for num in range(100):
    cmds.polyCube()
    x = random.random() * 10
    y = random.random() * 10
    z = random.random() * 10
    cmds.move(x, y, z, a = True)

from random import random as rand
print(rand())



# 랜덤의 범위를 지정할 때에는 uniform 함수를 쓴다 ============
import maya.cmds as cmds
import random
for num in range(100):
    cmds.polyCube()
    x = random.uniform(-10, 10)
    y = random.uniform(-10, 10)
    z = random.uniform(-10, 10)
    cmds.move(x, y, z, a = True)


# 감마 분포와 가우스 분포에 따라 난수 생성 ====================
# 감마 분포
import maya.cmds as cmds
import random

for number in range(100):
    cmds.polyCube()
    x = random.gammavariate(1, 10)
    y = random.gammavariate(1, 10)
    z = random.gammavariate(1, 10)
    cmds.move(x, y, z, a = True)

# 가우스 분포
import maya.cmds as cmds
import random

for number in range(100):
    cmds.polyCube()
    x = random.gauss(1, 10)
    y = random.gauss(1, 10)
    z = random.gauss(1, 10)
    cmds.move(x, y, z, a = True)


# 앞서 설명한 이 외에도 파이썬에서 지원하는 다양한 분포에 따라 난수를 생성할 수 있다.
# 베타 분포 : random.betavariate()
# 지수 분포 : random.expovariate()
# 로그 정규 분포 : random.lognormvariate()
# 정규 분포 : random.normalvariate()
# 폰 미제스 : random.vonmisesvariate()
# 파레토 분포 : random.paretovariate()
# 베이불 분포 : random.weibullvariate()



# 세포핵 만들기 ===========================================
# 1. 크기가 다른 원을 여러개 만들어서 둥글게 배치한다
# 2. 원을 새로 만들어서 ShrinkWarp 기능으로 덮어씌워서 속이 빈 세포핵을 만든다

import maya.cmds as cmds
import random                #random 명령을 쓸 것이기 때문에 random 모듈을 부른다.
import maya.mel as mel       #mel 명령어를 쓸 것이기 때문에 mel 라이브러리를 부른다.

for number in range(300):
    cmds.polySphere(r=random.uniform(1, 4))
    #uniform 명령으로 1에서 4 사이의 난수를 생성한 후,
    # r 파라미터를 써서 난수값을 가지는 원을 만든다
    
    rand_in_sphere = mel.eval('sphrand(10)')
    # eval 명령어를 써서 mel 명령어인 sphrand(10)을 실행한 후 rand_in_sphere에 넣는다.
    # sphrand(10)은 0에서 10까지의 위치값을 원형으로 생성하는 명령어이다.

    x = rand_in_sphere[0]
    y = rand_in_sphere[1]
    z = rand_in_sphere[2]
    # x, y, z에 랜덤으로 생성한 값을 넣는다.

    cmds.move(x, y, z, a = True)
    # 랜덤 크기로 생성한 원을, 랜덤으로 생성한 값을 써서 x, y, z로 이동한다.