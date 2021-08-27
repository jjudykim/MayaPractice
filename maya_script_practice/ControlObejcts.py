# **************************
# *      오브젝트 다루기      *
# **************************

# 1. 오브젝트를 선택하는 방법 ======================================
import maya.cmds as cmds

cmds.select(all=True)
# cmds.select('*')
# 위 코드를 사용해서 '모든(카메라 포함)' 객체들을 선택할 수 있다



# 2. 선택한 오브젝트의 목록 다루기 ===================================
import maya.cmds as cmds
select_object = cmds.ls(sl=1)
# 선택한 오브젝트의 목록을 select_object라는 변수에 넣는다.

cmds.select(clear = 1)
# 선택했던 것을 해제

cmds.select(select_object)
# select_obejct에 들어있던 목록의 오브젝트들이 다시 선택됨

cmds.select(select_object[0])
# 리스트에 가장 처음에 있는, 첫번째로 선택했던 오브젝트만을 선택하려면 index 사용
# 비슷하게 [1], [2], [10]... 등 가능

cmds.select(select_object[10:20])
# 앞부터 10개 이후 10개를 선택

cmds.select(select_object[-20:])
# 뒤부터 20개를 선택

cmds.select(select_object[::2])
# 리스트에 있는 오브젝트를 하나씩 건너뛰면서 선택

# 이렇게 다양한 방법으로 "선택한" 오브젝트의 목록을 다룰 수 있다.


# 3. 오브젝트의 속성을 알아내는 방법 ======================================
# getAttr 명령을 통해 오브젝트의 속성을 알아낼 수 있다.
import maya.cmds as mcds

selected = cmds.ls(selection = True)
for sel_ in selected:
	translated_x = cmds.getAttr("%s.translateX" % sel_)
	translated_y = cmds.getAttr("%s.translateY" % sel_)
	translated_z = cmds.getAttr("%s.translateZ" % sel_)
	print(sel_)
	print translated_x
	print translated_y
	print translated_z

# getAttr 명령은 Attribute Editor의 정보를 알아내는 것이기 때문에, 같은 방법으로 Rotate, Scale 등의 값도 알아낼 수 있다.
import maya.cmds as cmds

selected = cmds.ls(selection = True)
for sel_ in selected:
	rotated_x = cmds.getAttr("%s.rotateX" % sel_)
	rotated_y = cmds.getAttr("%s.rotateY" % sel_)
	rotated_z = cmds.getAttr("%s.rotateZ" % sel_)
	print(sel_)
	print rotated_x
	print rotated_y
	print rotated_z

# getAttr가 아닌 xform 명령어를 이용해 오브젝트의 위치를 알아낼 수도 있다
import maya.cmds as cmds

selected = cmds.ls(sl = 1, fl = 1)
for sel_ in selected :
	print sel_
	get_position = cmds.xform(sel_, q=1, ws= 1, t=1)
	print get_position

# vertex에도 사용 가능!
import maya.cmds as cmds

get_position = [cmds.xform(i, q=1, ws=1, t=1) for i in cmds.ls(sl = 1, fl=1)]
print get_position


# 4. 포인트의 위치를 알아내는 방법 ======================================
# 커브의 CV, Object의 vertex와 같이 점으로 된 포인트의 위치만 알아내는 명령어.
# curve1의 cv 위치를 지정해보겠다
import maya.cmds as cmds
print cmds.pointPosition('curve1.cv[1]')
# -> curve의 point위치가 나타난다!

#선택한 커브의 CV, 혹은 오브젝트의 버텍스들의 위치를 알아내기

import maya.cmds as cmds
selected = cmds.ls(selection = True, flatten = True)
#fi 플래그가 핵심!
for sel_ in selected:
	print(sel_)
	position = cmds.pointPosition(sel_)
	print position


# 번외로 ================================================================
# 마야에 포함된 파이썬 버전 확인하기
import sys
print sys.version