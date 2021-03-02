s=input()
while '()' in s: s=s.replace("()","") #loop find () and replace ""
print(s)
print(str(len(s)==0).lower()) #true or flase 