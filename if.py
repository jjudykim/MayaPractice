# if는 어떠한 조건을 만족해야 실행하는 구문이다
i = 3
if i > 5:
    print("i가 크다")
else:
    print("i가 작다")


# elif를 써서 다양한 조건을 만들 수 있다
import datetime
today = datetime.datetime.now()
print(today)
weekday = today.weekday()
print(weekday)
if weekday == 0:
    print("왠지 바쁜 월요일")
elif weekday == 1:
    print("정신없던 화요일")
elif weekday == 5:
    print("황금같은 토요일")
else:
    print("목, 금")

# if문에서도 break와 continue를 써서 반복문을 탈출하거나 조건문으로 돌아갈 수 있다.
for i in [1, 2, 3]:
    print (i)
    if i == 2:      # i가 2이면 반복문을 종료한다.
        break

for x in [1, 2, 3, 4, 5]:
    if x % 2 == 1:  # x가 홀수면 출력하지 않는다.
        continue
    print (x)

# enumerate로 이름 정리하기
# enumerate를 쓰면 for ~ in ~ 과 for ~ in range(len(~))을 섞어서 쓰는게 가능하다.
# 오브젝트들을 선택하고 다음을 실행하면, 선택된 오브젝트의 이름이 node_숫자로 바뀌게 된다.
from maya import cmds
sel_ = cmds.ls(sl = 1)
for serial, list_ in enumerate(sel_):
    cmds.rename(list_, "node_" + str(serial))
