init python:

    import math,random

    class circleMenu(renpy.Displayable):

        def __init__(self, child, move_radius, speed, angle, action, **kwargs):

            # 向renpy.Displayable输送变量
            super(circleMenu, self).__init__(**kwargs)

            # 子类
            self.child = renpy.displayable(child)
            text = child.strip('.png')
            self.text = Text(text , color='#fff', size=20)

            # 参数
            self.move_radius = move_radius
            self.speed = speed
            self.Angle = angle
            self.x_pos = int(self.move_radius*math.sin(self.Angle/180.0*3.1415926535))
            self.y_pos = int(self.move_radius*math.cos(self.Angle/180.0*3.1415926535))
            self.width = 0
            self.height = 0
            self.click = False


            # 根据随机数抖动
            self.randcom = 30
            self.randlist_x = [random.randint(-5,5) for i in range (self.randcom)]
            self.randlist_x.append(-int(sum(self.randlist_x)))
            self.randlist_y = [random.randint(-5,5) for i in range (self.randcom)]
            self.randlist_y.append(-int(sum(self.randlist_y)))
            self.num = 0

            self.oldst = None
            self.Action = action

        def render(self, width, height, st, at):

            # 图像
            child_render = renpy.render(self.child, width, height, st, at)
            # 文字
            text_render = renpy.render(self.text, width, height, st, at)



            # 获取子类的尺寸
            self.width, self.height = child_render.get_size()
            # 计时器
            if self.oldst is None:
                self.oldst = st
            dtime = st - self.oldst
            self.oldst = st
            speed = dtime * self.speed

            if self.num < self.randcom:
                self.num += 1
            else:
                self.num = 0

            # 点击事件触发前，角度增加，坐标移动
            while not self.click:
                if self.Angle >= -7200:
                    self.Angle -= speed
                else:
                    self.Angle = 0
                self.x_pos = int(self.move_radius*math.sin(self.Angle/180.0*3.1415926535)) + self.randlist_x[self.num]
                self.y_pos = int(self.move_radius*math.cos(self.Angle/180.0*3.1415926535)) + self.randlist_y[self.num]




                # 创建渲染场景
                render = renpy.Render(self.width, self.height)

                render.blit(child_render, (int(self.x_pos - self.width / 2), int(self.y_pos - self.height / 2)))
                render.blit(text_render, (int(self.x_pos - self.width / 2), int(self.y_pos - self.height / 2) +40))
                renpy.redraw(self, 0)


                # 返回渲染
                return render

        def event(self, ev, x, y, st):
            import pygame

            # 定义触发事件
            if self.x_pos-10 < x  < self.x_pos + self.width+10 and\
            self.y_pos-10 < y  < self.y_pos + self.height+10 and\
            ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                self.click != self.click
                renpy.jump(self.Action)

        def visit(self):
            return [ self.child, self.text ]


screen circleMenu:

    # 确保覆盖除了快捷栏以外的其他屏幕
    tag menu

    # 把不同的选项放在均匀的位置
    default num_choice = 360/len(choices)

    for i, (choice, activity) in enumerate(zip(choices, activities)):
        
        add circleMenu(choice+'.png', 180.0 ,20.0 , i*num_choice , activity):
            xalign 0.5
            yalign 0.5
