from math import pi, tan, cos

gravity = 9.81
v = 44
theta = 80 * pi / 180
distance = 0.5
bh = 1

# brackets first
brackets = v * cos(theta)

# indecies as variables
a = brackets ** 2
b = 0.5 ** 2

# full equation split into smaller variables so i can see step by step how it works
var1 = distance * tan(theta)
var2 = (gravity * b)/(2 * a)
var3 = bh + var1
answer = var3 - var2

# condensed into one line rather than all the different variables

p = bh + distance * tan(theta) - (gravity * 0.5 ** 2)/(2 * (v * cos(theta)) ** 2)
# printing both my answer from the breakdown and from the equation in one line
print(p)
print(answer)

# answer as per victorias creation

y = bh + distance * tan(theta) - (gravity * distance ** 2) / (2 * ((v * cos(theta)) ** 2))


print(y)
