# 리스트는 ,(콤마)로 구분하고 [](대괄호)로 감싸서 만들 수 있으며, 하나의 리스트에 숫자와 문자를 넣을 수 잇다

list = [11, 22, "text"]
print(list)
print(list*2)

# 특정 원소의 위치 찾기
print(list.index("text"))
print(list.index(11))

# 인덱스를 이용해서 리스트의 내용 출력하기
print(list[0])
print(list[1])
print(list[2])

print(list[1:])
print(list[:2])

# 리스트의 특정 부분을 변수에 넣어 출력할 수도 있다
a1 = list[2]
print(a1)

# 리스트의 index는 0 이하의 수로 접근할 수 있다
print(list[-1])
print(list[::-1])



# 리스트의 내용 변경하기 ===============================
list[0] = 55
print(list)

# 리스트에 요소를 추가할 때에는 append를 사용한다.
list.append("added")
print(list)

# 특정 위치에 넣을 때에는 insert를 쓰고, 앞에 넣을 위치, 뒤에 넣을 요소를 쓴다.
list2 = [11, 22, "text"]
list2.insert(1, "added")
print(list2)

# 리스트 원소의 삭제는 pop을 사용한다 (해당 index의 원소를 삭제함)
list3 = [11, 22, "text"]
list3.pop(1)
print(list3)

# 직접 원소의 값을 지정해 삭제할 때에는 remove를 사용한다.
list4 = [11, 22, 'text']
print("list4 :", list4)
list4.remove(22)
print(list4)



# 리스트를 더하기 ========================================
# 산술연산자 +로 간단하게 더할 수 있다.
list_a = [11, 22, "text"]
list_b = ["a", "b", "c"]
list_c = list_a + list_b
print(list_c)

# extend를 써서 하나의 리스트에 다른 리스트를 더할 수 있다.
list_a.extend(list_b)
print(list_a)



# 리스트의 내용 정렬하기 ==================================
input_list = ["banana", "apple", "melon", "grape", "peach", "watermelon"]
input_list.sort()
print(input_list)

# 그럼 리스트에 오브젝트를 넣고 선택할 수도 있을 것이다.
# 먼저 명령어를 사용해 큐브를 제작하자
import maya.cmds as cmds
cmds.polyCube()

# 그리고 오브젝트를 만든 후 다음을 실행한다
import maya.cmds as cmds
select_object = cmds.ls(sl = 1)         # 선택한 오브젝트의 목록을 select_object라는 변수에 넣는다.
print(select_object)

# 목록을 이제 index로 접근해 선택할 수 있다.
cmds.select(select_object[0])

# 리스트의 내용을 정렬하려면
select_object.sort()
print(select_object) # 정렬한 내용을 확인

# 이제 첫번째 목록을 선택하는 명령을 실행하면 첫번째로 정렬되어 들어있는 pCube1이 선택된다

# 같은 방법으로 슬라이딩을 이용해 여러가지 방법으로 선택을 할 수 있다.
cmds.select(select_object[:5])
cmds.select(select_object[-5:])
cmds.select(select_object[::2])

# 오브젝트를 직접 선택해서 리스트에 넣는것이 아니라, 이름을 직접 지정해 선택해서 넣을 수도 있다.
import maya.cmds as cmds
cmds.select("pCube1", "pCube2", "pCube3")
select_object = cmds.ls(sl=1)

print(select_object)

# 아니면 아예 이름으로 리스트를 넣을 수도 있긴 하다
import maya.cmds as cmds
list_input = ["pCube1", "pCube2", "pCube3"]
print(list_input)

#이 리스트에 append 명령을 써서 큐브를 추가할 수 있다.
list_input.append("pCube4")
print(list_input)

#이 리스트에 들어있는 오브젝트들만 선택하려면 select 명령어를 사용해서 할 수 있다
import maya.cmds as cmds
cmds.select(list_input)