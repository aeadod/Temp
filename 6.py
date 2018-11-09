import turtle

def drawSnake(rad,angle,len,neckrad):
    for i in range(len):
        turtle.circle(rad,angle)#沿圆形轨迹爬行，半径在距乌龟左侧rad的位置-表示右侧
        turtle.circle(-rad,angle)#angle表示沿圆形爬行的弧度值
    turtle.circle(rad,angle/2)
    turtle.fd(rad)#向前直线爬行的距离
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1300,800,0,0)#启动一个窗口宽1300高800，左上角
    pythonsize=30
    turtle.pensize(pythonsize)#轨迹宽度
    turtle.pencolor("red")#颜色或者 turtle.pencolor("#3B9909")
    turtle.seth(-40)#开始运动时方向，x正方向为0逆时针
    drawSnake(40,70,5,pythonsize/2)
#从这里执行
main()
