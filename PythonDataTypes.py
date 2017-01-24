# Expressions are evaluated from using the left-to-right evaluation rule
print("left-to-right evaluation rule" + str(3 - 2 + 1))

''' When two int values are added, subtracted, or multiplied, the result is an int
If at least one float value appears in the expression, however, the result is always a
float value'''
value1 = 2
value2 = 5

# String representation of inter value
print("The output of two integer is " + str(value1 + value2))

# x power y is computed using the Python expression x**y
xVal = 2
yVal = 5
print("The power of x in y is " + str(xVal ** yVal))

# obtain the integer quotient and the remainder when two integer values are
# divided, operators // and % are used
print("Integer quotient obtained " + str(12 // 3))
print("Integer remainder obtained " + str(10 % 3))

# Python supports built in mathematical functions
print("Absolute value of -4 is " + str(abs(-4)))
print("Absolute value of -3.2 is " + str(abs(-3.2)))

'''Some other functions that Python makes available are min() and max(), which return
the minimum or maximum, respectively'''
print("Minimum value is " + str(min(6, -2)))
print("Minimum value is " + str(min(2, -4, 6, -2)))
print("Maximum value is " + str(max(6, -2)))
print("Maximum value is " + str(max(12, 26.5, 3.5)))
