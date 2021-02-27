# Day - 01
## Variable

## Casting
#If you want to specify the data type of a variable, this can be done with casting.
x = 4 # int
x = "Hello" # str 
print(x)

x = str(3) # '3'
y = int(3) # 3
z = float(3) # 3.0

print(x,y,z)
print(type(x)) ##Get the Type

x = "Hello"
# is the same as
x = 'Hello'

a = 4
A = "Hi"
# A will not over write a

##Many Values to Multiple Variables
x, y, z = "Hi", "Hello", "Bye"
print(x)
print(y)
print(z)

x = y = z = "Hi"
print(x)
print(y)
print(z)

#From list
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)



