#Python Data Type
import random
"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
"""
x = "Hello World" #str
print(x)
x = 20 #int
x = 20.5 #float
x = 1j #complex
print(x)
print(type(x))

x = ["Hi", "Hello", "Bye"] #list
print(x)
#['Hi', 'Hello', 'Bye']

x = ("Hi", "Hello", "Bye") # Tuple
print(x)
#('Hi', 'Hello', 'Bye')

x = range(6) # range
print(x)
#range(0, 6)
print(type(x))

x = {"name" : "John", "age": 36}
print(x)
#{'name': 'John', 'age': 36}
print(type(x))

x = {"apple", "banana", "cherry"} #set
print(x)
#{'cherry', 'apple', 'banana'}
x = frozenset({"apple", "banana", "cherry"}) #frozenset
print(x)

x = True # bool
print(x)

x = b"Hello" # bytes
print(x)
# b'Hello'

x = bytearray(5)
print(x)
# bytearray(b'\x00\x00\x00\x00\x00')
# <class 'bytearray'>

x = memoryview(bytes(5)) 
print(x)
#<memory at 0x0000027AFDFD5880>

print(random.randrange(1,10)) # random



