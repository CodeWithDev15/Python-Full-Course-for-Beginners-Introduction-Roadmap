# What is type casting?

# The concerstion of one data type into other data type is known as type casting in python.

a = "Harry"
b = "Bhai"
# It will concatinat both values

print(a+b)
a_a = "1"
b_b = "2"
print(a_a+b_b)
# It will concatinate not add because both are strings so the output will be 12 not 3

# Type casting try to convert but it can not convert harry + bhai because it is not a number so it will concatinate it.


print(int(a_a)+int(b_b))

x = "Harry1"
y = "2"

# print(int(x)+int(y)) # It will give you can an error because it is not a valid integer the x and y it is.

# Home_Work_Code:

string = "15"
number = 7
string_number = string
sum = number + int(string_number)
print("The sum of both the numbers is: ", sum)

o = "12"
g = 12
f = g + int(o)
print("The sum of both numbers is: ", f)

# There are types of type casting, which are: Explicit typecasting that we do to covert one value into another value. And, implicttypecasting is that python do to covert lower order into higher order, for eg:

s = 1.2
c = 5.0
print(s+c)

# or

j = 9.0
l = 2.5
l_l = l + j
print(l_l)