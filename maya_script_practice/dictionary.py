# 파이썬에서는 사전과 비슷한 형태의 자료형을 제공하는데, 이름 그대로 -> 딕셔너리(dictionary)라고 한다.
# 딕셔너리 자료형은 값을 묶어서 표현할 수 있다.
# 즉, 키(key)와 그 값에 해당하는 값(value)를 한 쌍으로 갖는 자료형이다.
# 딕셔너리는 리스트나 튜플처럼 자료가 들어있는 순서대로 해당되는 값을 부르지 않고 키를 통해 값을 부른다.
# 딕셔너리는 {}로 묶어서 표현한다.

room_number = {1 : "Kim", 7 : "Lee", 9 : "Shin"}
print(room_number[7])
# print(room_number[2]) 이 명령은 2라는 키에 해당하는 값이 없으므로 오류가 나온다!

room_string_number = {"one" : "Kim", "seven" : "Lee", "Nine" : "Shin"}
print(room_string_number["one"])



# 딕셔너리에 들어있는 값의 개수 알아내기 ===================================
print(len(room_number))
#len을 써서 개수를 알아낸다. 결과로 3이 출력된다.



# 빈 딕셔너리 만들고 데이터 추가하기 ======================================
# 빈 사전은 중괄호를 써서 만들 수 있다.
empty_dict = {}

# 빈 사전에 키와 데이터를 추가할 수 있다.
empty_dict["jajangmyeon"] = 2
empty_dict["ulmyeon"] = 5
empty_dict["tangsuyuk_is_squirt_not_dip"] = 6
print(empty_dict)



# 딕셔너리에 데이터 추가하기 =============================================
ordered = {1 : "자장면", 7 : "울면", 9 : "탕수육은 찍먹으로"}
ordered[2] = "만두"
# 주문한 음식에 만두를 추가하면서 영수증 2번째 칸에 찍히도록 했다
print(ordered)



# 딕셔너리에 오브젝트 넣고 확인하기
import maya.cmds as cmds
dict_maya = {1 : "pCube1", 2 : "pCube2", 3 : "pCube3"}
dict_maya[4] = "pCube4"
#dict_maya라는 딕셔너리에 pCube 별로 키 값을 붙여주었다.