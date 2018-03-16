def sumdiff(x , y):
    sum = x + y
    diff = x - y
    return sum, diff  # Return multiple variable

num1, num2 = eval(input("Please enter two numbers(num1, num2)"))
s, d = sumdiff(num1, num2)
print("The sum is", s, "\nThe difference is", d)
