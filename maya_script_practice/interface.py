# 스크립트가 한 두개면 상관 없지만, 많아질수록 Shelf탭이 복잡해지고, 나중에는 뭐가 뭔지 알 수 없게 될 수도 있다
# 따라서 인터페이스를 만들어서 스크립트의 기능을 넣으면 간편하게 스크립트를 실행하거나 정리할 수 있다!
# 또 다양한 기능을 가진 스크립트를 만들 때에는 인터페이스가 필수적이다.

# 마야 파이썬에서 쓸 수 있는 인터페이스, 그 중에서도 컨트롤러는 도움말에서 확인할 수 있다.
# http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/cat_Windows.html#Controls


# 버튼 ===============================================
# 가장 기본적인 버튼을 만들고, 버튼에 기능을 넣어보자

import maya.cmds as cmds

def first_(*args):
    print("First button pushed")               # 첫 번째 버튼을 눌렀을 때의 함수

def second_(*args):
    print("Second button pushed")              # 두 번째 버튼을 눌렀을 때의 함수

def third_(*args):
    print("Third button pushed")               # 세 번째 버튼을 눌렀을 때의 함수

cmds.window(width=200)                         # 넓이가 200인 윈도우를 만든다.
cmds.columnLayout(adjustableColumn=True)       # 버튼을 만든다?
cmds.button(label="Button 1", command=first_)  # 이름을 Button 1이라고 붙이고, 이걸 누르면 first_함수가 실행되도록 한다.
cmds.button(label="Button 2", command=second_)
cmds.button(label="Button 3", command=third_)
cmds.showWindow()                              # 윈도우를 화면에 띄운다!



# 자주 쓰는 컨트롤 ========================================
# 1. 체크박스(checkBox)
import maya.cmds as cmds
window = cmds.window("window", width = 150)
cmds.columnLayout(adjustableColumn=True)
cmds.checkBox(label="One")
cmds.checkBox(label="Two")
cmds.checkBox(label="Three")
cmds.checkBox(label="Four")
cmds.showWindow(window)


# 2. 체크박스 그룹(checkBoxGrp)
import maya.cmds as cmds
exampleWindow = cmds.window()
cmds.columnLayout()
cmds.checkBoxGrp(numberOfCheckBoxes=3, label = "Three Buttons", labelArray3=["One", "Two", "Three"])
cmds.checkBoxGrp(numberOfCheckBoxes=4, label = "Four Buttons", labelArray4=["1", "2", "3", "4"])
cmds.showWindow(exampleWindow)


# 3. 명령어 입력창(cmdScrollFieldExecuter)
import maya.cmds as cmds
cmds.window()
cmds.columnLayout()
cmds.cmdScrollFieldExecuter(width=200, height=100)
cmds.showWindow()


# 4. 결과출력창(cmdScrollFieldReporter)
import maya.cmds as cmds
cmds.window()
cmds.columnLayout()
cmds.cmdScrollFieldReporter(width=200, height=100)
cmds.showWindow()


# 5. 그래디언트 컨트롤(gradientControl)
import maya.cmds as cmds
cmds.window(title="Gradient Control For Attribute")
objName = cmds.createNode("polySplitRing")
cmds.columnLayout()
cmds.gradientControl(at="%s.profileCurve"%objName)
cmds.showWindow()


# 6. 씬에 슬라이더버튼 띄우기(hudSliderButton)
import maya.cmds as cmds
def translateXSliderButton(HUD):
    cmds.undoInfo(swf=True)
    selList = cmds.ls(sl=True)
    for object in selList:
        if cmds.objectType(object, isType = "transform"):
            cmds.setAttr(object+".tx", cmds.hudSliderButton(HUD, query=True, v=True))

cmds.hudSliderButton("HUDTranslateXSliderButton", s=5, b=5, vis=True, sl="Slider", value=0, type="int", min=-10, max=10,
slw=50, vw=50, sln=100, si=1, bl="Button", bw=60, bsh="rectangle", brc=lambda:translateXSliderButton("HUDTranslateXSliderButton"))


# 7. 아이콘텍스트버튼(iconTextButton)
import maya.cmds as cmds

window=cmds.window()
cmds.columnLayout(adjustableColumn=True)
cmds.iconTextButton(style="textOnly", image1="Sphere.png", label="sphere")
cmds.iconTextButton(style="iconOnly", image1="spotlight.png", label="spotlight")
cmds.iconTextButton(style="iconAndTextHorizontal", image1="cone.png", label="cone")
cmds.iconTextButton(style="iconAndTextVertical", image1="cube.png", label="cube")
cmds.showWindow(window)


# 8. 아이콘 텍스트 스크롤 리스트(iconTextScrollList)
import maya.cmds as cmds

cmds.window()
cmds.paneLayout()
cmds.iconTextScrollList(allowMultiSelection = True, append=("one", "two", "three", "four", "five", "six", "seven", "eight"
                                                            , "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
                                                            "fifteen"), selectItem="six")
cmds.showWindow()


# 9. 레이어 버튼(layerButton)
import maya.cmds as cmds

cmds.window()
cmds.columnLayout()
b = cmds.layerButton(name="defaultLayer", cl=(1.0, 0.0, 0.0), s=True)
cmds.showWindow()

width = cmds.layerButton(b, q=True, labelWidth=True)


# 10. 라디오 버튼 그룹(radioButtonGrp)
import maya.cmds as cmds

window = cmds.window()
cmds.columnLayout()
group1 = cmds.radioButtonGrp(numberOfRadioButtons=3, label="Colors", labelArray3=["Red", "Blue", "Green"])
cmds.radioButtonGrp(numberOfRadioButtons=3, shareCollection=group1, label="", labelArray3=["Yellow", "Orange", "Purple"])
cmds.showWindow(window)


# 11. 세퍼레이터(separator) = 구분선임!
import maya.cmds as cmds

cmds.window()
cmds.rowColumnLayout(numberOfColumns=2, columnAlign=(1, "right"), columnAttach=(2, "both", 0), columnWidth=(2, 150))
cmds.text(label="Default")
cmds.separator()

cmds.text(label="None")
cmds.separator(style="none")

cmds.text(label="Single")
cmds.separator(style="single")

cmds.text(label="Etched In")
cmds.separator(height=40, style="in")

cmds.text(label="Etched Out")
cmds.separator(height=40, style="out")

cmds.setParent("..")
cmds.showWindow()


# 12. 쉘프 버튼(shelfButton)
import maya.cmds as cmds
window = cmds.window(title="ShelfButton Example")
tabs = cmds.tabLayout()
shelf = cmds.shelfLayout()
cmds.shelfButton(annotation = 'Print "Hello".', image1="commandButton.png", command='print "Hello\\n"')
cmds.shelfButton(annotation="Create a sphere.", image1="Sphere.png", command="cmds.sphere()")
cmds.shelfButton(annotation="Show the Attribute Editor.", image1 = "menulconWindow.png", command='import maya.mel; maya.mel.eval("openAEWindow")')
cmds.shelfButton(annotation="Create a cone.", image1="cone.png", command="cmds.cone()", imageOverlayLabel="4th")
cmds.shelfButton(annotation="Undo last operation.", image1="undo.png", command="undo", imageOverlayLabel="undo", overlayLabelColor=(1, .25, .25))
cmds.shelfButton(annotation="Redo last operation.", image1 = "redo.png", command="redo", imageOverlayLabel="redo", overlayLabelColor=(1, 1, .25), overlayLabelBackColor=(.15, .9, .1, .4))
cmds.tabLayout(tabs, edit=True, tabLabel=(shelf, "ExampleShelf"))
cmds.showWindow(window)


# 13. 심볼 체크박스(symbolCheckBox)
import maya.cmds as cmds
cmds.window()
cmds.columnLayout()
cmds.symbolCheckBox(image="circle.png")
cmds.symbolCheckBox(image="sphere.png")
cmds.symbolCheckBox(image="cube.png")
cmds.showWindow()


# 14. 어트리뷰트 필드 그룹(attrFieldGrp)
import maya.cmds as cmds
object = cmds.sphere()
window = cmds.window(title="attrFieldGrp Example")
cmds.columnLayout()
cmds.attrFieldGrp(attribute="%s.translate"%object[0])
cmds.showWindow()


# 15. 컬러 슬라이더 그룹(colorSliderGrp)
import maya.cmds as cmds
cmds.window()
cmds.columnLayout()
cmds.colorSliderGrp(label="Blue", rgb=(0,0,1))
cmds.colorSliderGrp(label="Green", hsv=(120, 1, 1))
cmds.showWindow()


# 16. 플롯 슬라이더 버튼 그룹(floatSliderButtonGrp)
import maya.cmds as cmds
window = cmds.window()
cmds.columnLayout()
cmds.floatSliderButtonGrp(label="Label",field=True, buttonLabel="Button", symbolButtonDisplay=True, columnWidth=(5, 23), image="cmdWndIcon.xpm")
cmds.showWindow(window)


# 17. 프레임 레이아웃(frameLayout)
import maya.cmds as cmds

cmds.window()
cmds.scrollLayout("scrollLayout")
cmds.columnLayout(adjustableColumn=True)
cmds.frameLayout(label="Buttons")
cmds.columnLayout()
cmds.button()
cmds.button()
cmds.button()
cmds.setParent("..")
cmds.setParent("..")
cmds.frameLayout(label="ScrollBars")
cmds.columnLayout()
cmds.intSlider()
cmds.intSlider()
cmds.intSlider()
cmds.setParent("..")
cmds.setParent("..")
cmds.frameLayout(label="Fields")
cmds.columnLayout()
cmds.intField()
cmds.intField()
cmds.intField()
cmds.setParent("..")
cmds.setParent("..")
cmds.frameLayout(label="Check Boxes")
cmds.checkBox()
cmds.checkBox()
cmds.checkBox()
cmds.setParent("..")
cmds.setParent("..")
cmds.showWindow()


# 18. 폼 레이아웃(formLayout)
import maya.cmds as cmds
window = cmds.window()
form = cmds.formLayout(numberOfDivisions = 100)
b1 = cmds.button()
b2 = cmds.button()
column = cmds.columnLayout()
cmds.button()
cmds.button()
cmds.button()
cmds.formLayout(form, edit=True,
                attachForm=[(b1, "top", 5), (b1, "left", 5),(b2, "left", 5), (b2, "bottom", 5), (b2, "right",5),
                            (column, "top", 5), (column, "right", 5)],
                attachControl=[(b1, "bottom", 5, b2), (column, "bottom", 5, b2)],
                attachPosition=[(b1, "right", 5, 75), (column, "left", 0, 75)],
                attachNone=(b2, "top"))
cmds.showWindow(window)


# 19. 패널 레이아웃(paneLayout)
import maya.cmds as cmds
cmds.window()
cmds.paneLayout(configuration="quad")
cmds.button()
cmds.textScrollList(append=["one", "two", "three"])
cmds.scrollField()
cmds.scrollLayout()
cmds.columnLayout()
cmds.button()
cmds.button()
cmds.button()
cmds.showWindow()