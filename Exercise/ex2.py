CHAR_X = 'x'
BLANK = ' '

n = int(input("Input number: "))

[print(n*(CHAR_X+' ')) for i in range(n)]
print()
[print((i+1)*(CHAR_X+' ')) for i in range(n)]
print()
[print(CHAR_X + ((n-2)*BLANK if (i!=0 and i!=n-1)
else (n-2)*CHAR_X) + (n!=1)*CHAR_X) for i in range(n)]
