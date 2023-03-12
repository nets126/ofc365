from sprites import *
 
# 新建屏幕
screen = Screen()
# 设定背景颜色
screen.bgcolor('dodger blue')
# 设定标题
screen.title('旋转的文字')
 
# 新建不可见的角色
t=Sprite(visible=False)
# 设定角色为白色
t.color('white')
# a是一个全局变量,这里代表角度
a= 0
# 要旋转的文字
info = '享受人生！'
# 定义字体样式
ft = ('黑体',32,'normal')
# 定义rotate函数
def rotate():
    # 申明a为全局变量
    global a
    # 清除以前所写内容
    t.clear()
 
    t.write(info,align='center',font=ft,angle=a)
    a = a + 10
    screen.ontimer(rotate,50)
rotate()
 
screen.mainloop()
