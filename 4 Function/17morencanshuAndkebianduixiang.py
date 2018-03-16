# 默认参数与可变对象


def saver(x=[]):  # Saves away a list object
    x.append(1)  # Changes same object each time!
    print(x)

saver([2])  # Default not used
saver()  # Default used
saver()
saver()  # Grows on each call!


def saver1(x=None):
    if x is None:  # No argument passed?
        x = []  # Run code to make a new list
    x.append(1)  # Changes new list object
    print(x)

saver1([2])
saver1()                       # Doesn't grow here
saver1()
