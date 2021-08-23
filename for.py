sum = 0
for i in range(11):
    sum += i
print(sum)



# 리스트의 내용을 출력하기 ===================================
list = ["object_1", "object_2", "object_3"]
for x in list:
    print(x)

# for문을 사용해서 평균 구하기
input_list = [1, 2, 3, 4]
avg = 0.0
for val in input_list:
    avg = avg + val
    print(val)
avg /= len(input_list)
print("avg : ", avg)



# 튜플의 내용을 출력하기 =====================================
t = (22, 11, 33, 44, 66)
for x in t :
    print(x)



# 딕셔너리의 내용을 출력하기 ==================================
dic = {"key_1" : "a", "key_2" : "b", "key_3" : "c"}
for x in dic:
    print(x)
    print(dic[x])



# 문자열 출력 방법 ==========================================
for x in "abcdefg":
    print(x)



# range를 써서 값을 발생시키기 ===============================
for a in range(4):
    print(a)

for a in range(1, 9):
    print(a)

for a in range(1, 10, 2): #1에서 9까지 2씩 건너뛰면서 값을 발생시킨다
    print(a)



# 응용)) range를 써서 오브젝트의 이름 바꾸기
import maya.cmds as cmds
sel_ = cmds.ls(sl = 1)                       # 선택한 오브젝트들이 sel_이라는 변수에 담겨있다.
for serial in range(len(sel_)):              # 선택한 오브젝트들의 개수를 알아내고 그만큼 반복한다.
    cmds.rename(sel_[serial], "range_#")     # 오브젝트의 이름을 'range_숫자'로 바꾼다.



# 응용)) for문을 써서 많은 오브젝트 만들기
# 마야에서 for문을 써서 9개의 큐브를 만들어보자.
# 9개의 큐브가 만들어지고, 만들어진 순서로 이름 뒤에 숫자가 붙는다.
import maya.cmds as cmds
for i in range(9):
    cmds.polyCube()

# 만약 높이가 5, 넓이가 3, 깊이가 3인 오브젝트를 9개 만들고, sds_cube라는 이름과 일련번호를 붙이려면 다음과 같이 실행한다.
import maya.cdms as cmds
for i in range(9):
    cmds.polyCube(h = 5, w = 3, d = 1, n = "sds_cube#")

# 9개의 큐브를 만들고 3줄로 정렬하기 위해서는 for를 2번 사용해야 한다(이중 for문)
import maya.cmds as cmds
for i in range(3):
    for j in range(3):
        cmds.polyCube()
        cmds.move(i * 2, 1 * 2, j * 2)



# 응용)) for문을 써서 오브젝트의 이름 정리하기
import maya.cmds as cmds
sel_ = cmds.ls(sl = 1)
for serial in sel_:
    cmds.rename(serial, "object_#")