# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print(a[1])

for x in "banana":
    print(x)

print(len(a)) # len of string

#Check String
txt = "The best things in life are free!"
print("free" in txt)
print("Free" in txt) # case sensitive

if "free" in txt:
    print("Yes, 'free' is present.")

#Check if NOT
print("expensive" not in txt) # True bool

if "expensive" not in txt:
  print("Yes, 'expensive' is NOT present.")

#Slicing Strings
b = "Hello, World!"
print(b[2:5]) #llo [2,5)
print(b[:5]) #Hello [first,5)
print(b[2:]) #llo, World! [2,last]

#Negative Indexing
print(b[-5:-2]) #orl
"""
From: "o" in "World!" (position -5)
To, but not included: "d" in "World!" (position -2):
"""
print(b[::-1]) # Reverse a String 

#Upper Case
print(b.upper())

#Lower Case
print(b.lower())

#Remove Whitespace
c = "  Hello, World!  "
print(c.strip()) # returns "Hello, World!"

#Replace String
print(b.replace("l", " ")) #He  o, Wor d!

#Split String
a = "apple, banana, hello"
print(a.split(","))
#return ['apple', ' banana', ' hello']
a = a.split(",")
print(type(a)) #<class 'list'>
a = "1 2 3 4 5 6   7" # The spacing doesn't have to be the same.
a = a.split()
print(a) #['1', '2', '3', '4', '5', '6', '7']

#How to use format
age = 19
txt = "Hello, I am {} year old."
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) # Index

# String function https://www.w3schools.com/python/python_strings_methods.asp

# Function isinstance()
x = 200
print(isinstance(x, int))
print(isinstance(x, bool))