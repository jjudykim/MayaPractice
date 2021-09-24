# 패키지
# 파이썬에서 모듈은 하나의 .py 파일이며, 패키지는 이러한 모듈들을 디렉토리 형식으로 묶은 것이다.
# 모듈들을 담은 폴더가 패키지의 이름이 되며, 폴더 안에는 또 다른 서브 폴더를 만들 수 있다.
# 즉, 패키지는 폴더에 있는 모듈들의 집합을 의미한다.

# 각 폴더에는 이 폴더가 패키지라는 것을 파이썬에서 인식하기 위해 __init__.py라는 패키지 초기화 파일이 있어야 한다.
# 주의할 점은, 파이썬 버전 3.3 이후부터는 __init__.py 파일이 없어도 패키지로 인식하지만,
# 마야 2019에 있는 파이썬은 2.7.11 버전이기 때문에 각 폴더에 이 팔이이 있어야 한다.

# 앞에서 sys.path를 써서 모듈이 들어있는 위치, 즉 파이썬에서 인식할 수 있는 폴더를 확인할 수 있었는데,
# 이러한 폴더에 새로운 이름의 폴더를 만들어서 패키지를 만들 수 있고, 아예 새로운 폴더를 만들어 패키지를 만들 수도 있다.

# 새로운 폴더를 만들려면 다음처럼 경로를 추가해야한다
# E:\___Study\Maya\maya_script_practice

import sys
sys.path.append("E:/___Study/Maya/maya_script_practice/test")

# 이 폴더에 pack이라는 이름의 폴더를 만들고, 폴더의 안에 ani, na라는 이름의 서브 폴더를 만든다.
# 각 폴더의 안에 텍스트 형식으로 __init__.py라는 빈 파일을 만들어 넣는다.

# 다음과 같은 내용의 animal.py를 만들어서 ani 폴더 안에 저장한다.

def dog():
    print("dog!!!")

def cat():
    print("cat!!!")


# 이제 pack이라는 패키지가 만들어져다! 패키지 안의, animal 모듈의 dog 함수를 사용하려면 다음처럼 한다.
# 방법1
import pack.ani.animal as ani
ani.dog()

# 방법2
from pack.ani import animal
animal.dog()

# 방법3
from pack.ani.animal import dog
dog()

# 이렇게 다양한 방식으로 패키지의 모듈에 있는 함수를 사용할 수 있다.
# 모듈을 부르는 방법이 짧으면 사용방법은 길고, 모듈을 부르는 방법이 길면 사용방법은 짧다
# 편의성을 생각하면 아래의 방법이, 이름이 충돌하는 문제를 예방하려면 위의 방법이 좋다.

from pack.na.name import name_1
print(name_1())