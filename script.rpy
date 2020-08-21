# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define e = Character("艾琳")

default choices = []
default activities = []



label start:



    scene bg room
    show eileen happy

    e '以下是可以旋转的图像菜单'

    # 把选项填在choices后面的''里，把要跳转的label名填在activities后面的''里。
    $ choices = ['第一个', '第二个', '第三个']
    $ activities = ['选项一', '选项二', '选项三']

    call screen circleMenu


    label 选项一:
        '你选择了选项一'
        jump 继续

    label 选项二:
        '你选择了选项二'
        jump 继续

    label 选项三:
        '你选择了选项三'
        jump 继续

    label 继续:
    e "您已创建一个新的 Ren'Py 游戏。"

    e "当您完善了故事、图片和音乐之后，您就可以向全世界发布了！"

    # 此处为游戏结尾。

    return
