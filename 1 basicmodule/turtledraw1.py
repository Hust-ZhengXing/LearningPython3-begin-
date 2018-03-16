# turtle 画图 五角星
from turtle import *
fillcolor("red")     # 设置填充颜色
begin_fill()  
while True:  
    forward(200)     # 设置五角星的大小
    right(144)  
    if abs(pos()) < 1:  
        break  
end_fill()  