# **************************
# *      오브젝트 다루기      *
# **************************

# 1. 오브젝트를 선택하는 방법

import maya.cmds as cmds

cmds.select(all=True)
# cmds.select('*')
# 위 코드를 사용해서 '모든(카메라 포함)' 객체들을 선택할 수 있다


# 2. 선택한 오브젝트의 목록 다루기
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
