i = 1
while i <= 10:
    print(i)
    i += 1

# random 모듈을 사용해서 해부자!
import random
rand = 0
while rand != 4:                     # rand가 4가 아니라면 아래의 명령을 실행한다.
    rand = random.randint(0, 10)     # rand에 0과 10 사이의 값을 넣는다.
    print(rand)



# while을 사용해 여러 개의 폴리곤 만들기=======================================
#import maya.cmds as cmds
number = 0
while number < 20:
#    cmds.polyCube()
    number += 1



# break로 반복문 탈출하기====================================================
# break를 사용하면 while문 실행 중에 강제로 while문을 탈출할 수 있다.
i = 1
while i:
    print(i)
    i += 1
    if i > 5:
        break



# continue로 조건문 돌아가기 ================================================
i = 0
while i < 11:
    i = i+1
    if i % 2 != 0:          # i를 2로 나눈 값이 1이면 continue를 실행한다. (즉, 홀수는 패스)
        continue
    print(i)



# 무한 루프 ================================================================
# while 조건문에 1이나 true 처럼 항상 참인 값을 넣어주면 break가 실행되기 전까지 무한히 반복한다.
# 조건이 언제 만족될 지 모르지만 만족될 때 까지 실행해야 할 때, 계속 반복되어 실행해야 하는 경우에 사용
i = 0
while 1:
    i = i + 1
    print(i)
    if i > 5:
        break



# while 문을 써서 오브젝트의 이름 정리하기 =======================================
import maya.cmds as cmds
sel_ = cmds.ls(sl = 1)
# 선택한 오브젝트들이 sel_라는 변수에 담겼습니다.
serial = 0
while serial < len(sel_):
    cmds.rename(sel_[serial], "while_" + str(serial))
    serial = serial + 1