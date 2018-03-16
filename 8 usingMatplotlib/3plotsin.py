# ***************************Plot sin(x)*****************************************************
import numpy as np
import matplotlib.pyplot as plt

# 设置x,y轴的数值（y=sinx）
x1 = np.linspace(0, 10, 1000)
y1 = np.sin(x1)

# 创建绘图对象，figsize参数可以指定绘图对象的宽度和高度，单位为英寸，一英寸=80px
plt.figure(figsize=(8, 4))

# 在当前绘图对象中画图（x轴,y轴,给所绘制的曲线的名字，画线颜色，画线宽度）
plt.plot(x1, y1, label="$sin(x)$", color="red", linewidth=2)

# X轴的文字
plt.xlabel("x")

# Y轴的文字
plt.ylabel("Sin(x)")

# 图表的标题
plt.title("Plot Sin(x)")

# Y轴的范围
plt.ylim(-1.2, 1.2)

# 填充颜色 http://blog.csdn.net/you_are_my_dream/article/details/53457960
# plt.fill(x1, y1, 'r', alpha=0.3)
plt.fill_between(x1, y1, where=(2.3 < x1) & (x1 < 4.3) | (x1 > 10), facecolor='purple')
# 可以填充多次
plt.fill_between(x1, y1, where=(-0.5 < y1) & (y1 < 0.5), facecolor='green')

# 显示网格
plt.grid(True)

# 显示图示
plt.legend()

# 显示图
plt.show()

# 保存图
plt.savefig("sinx.jpg")
