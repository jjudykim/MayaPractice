# maya.cmds라는 모듈을 cmds라는 이름으로 읽는다.
# 오브젝트를 나타내고 숨기는 명령이 여기에 들어있다.
import maya.cmds as cmds
import random

# data라는 이름의 리스트를 만들고 안에 kawi, bawi, bo라는 데이터를 넣었다!
data = ['kawi', 'bawi', 'bo']

#data라는 이름을 가진 리스트에서 한 개의 데이터를 무작위로 선택해 result에 넣는다
result = random.choice(data)

print(result)

if result == 'kawi':
    cmds.showHidden('pCube1')
    cmds.hide('pPlane1')
    cmds.hide('pSphere1')
elif result == 'bawi':
    cmds.showHidden('pSphere1')
    cmds.hide('pCube1')
    cmds.hide('pPlane1')
elif result == 'bo':
    cmds.showHidden('pPlane1')
    cmds.hide('pCube1')
    cmds.hide('pSphere1')



