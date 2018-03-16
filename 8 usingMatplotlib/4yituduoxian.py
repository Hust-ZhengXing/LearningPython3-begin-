import matplotlib.pyplot as plt

# ******************Plot***********************************************
y1 = [10, 13, 5, 40, 30, 60, 70, 12, 55, 25]
x1 = range(0, 10)
x2 = range(0, 9)
y2 = [5, 8, 0, 30, 20, 40, 50, 10, 40]
plt.figure(figsize=(12, 6))
plt.plot(x1, y1, label='Frist line', linewidth=3, color='r', marker='o',
         markerfacecolor='blue', markersize=6)
plt.plot(x2, y2, label='second line')
plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
fig1 = plt.figure('fig1')
plt.show()

# *******************BAR************************
fig2 = plt.figure('fig2')
y1 = [10, 13, 5, 40, 30, 60, 70, 12, 55, 25]
x1 = range(0, 20, 2)
x2 = range(1, 21, 2)
y2 = [5, 8, 0, 30, 20, 40, 50, 10, 40, 15]
plt.bar(x1, y1, label='Frist line')
plt.bar(x2,y2,label='second line',color='r')
plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()

