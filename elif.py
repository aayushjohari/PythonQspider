#### elif ##### 
# find the relation between two integers

''' 
n1 = int(input("enter the number1: "))
n2 = int(input("enter the number2: "))
if n1> n2:
    print(n1, "is greater than ", n2)
elif n1< n2:
    print(n2 , "is greater than ", n1)
else:
    print("both", n1,"and", n2 ,"are equal")
'''

# wap tp check whether the character is uppercase or lower case or digit or specical character
'''
ch = input("enter the character: ")
if 'A' <=ch<='Z':
    print('uppercase')
elif 'a' <=ch<='z':
    print('lowercase')
elif '0'<=ch<='9':
    print('digit')
else:
    print("special character")

 '''

# wap to check whether the number is 1 digit 2 digit or 3 digit or more than 3 digit 
'''
n = abs(int(input("enter the number: ")))
if n >= 0 and n < 10:
    print("the number ", n , "is 1 digit")
elif n >= 10 and n < 100:
    print("the number ",n, "is 2 digit number")
elif n >= 100 and n < 1000:
    print("the number", n , "is 3 digit number")
else:
    print("the number ",n,"is more than 3 digit number")

'''

# greatest number among 4
'''
a = int(input("enter the number1: "))
b = int(input("enter the number2: "))
c =  int(input("enter the number3: "))
d = int(input("enter the number4: "))
if a>b and a>c and a>d:
    print(a, "is greatest")
elif b>=a and b>=c and b>=d:
    print(b , "is greatest")
elif c>=a and c>=b and c>=d:
    print(c, "is greatest")
else:
    print(d , 'is greatest')
'''
# wap to predict the grades of the student based on the marks

# wap to check the given points are lying in ehich quadrant
'''
x = int(input("enter the number1: "))
y = int(input("enter the number2: "))
if x > 0 and y > 0:
    print("the given points ",x,"and",y,"lies on 1st quadrant")
elif x > 0 and y < 0:
    print("the given points", x,"and",y,"lies on 2nd quadrant")
elif x < 0 and y < 0 :
    print("the given points",x,"and",y,"lies on 3rd quadrant")
elif x > 0 and y < 0:
    print("the given points", x,"and",y,"lies on 4th quadrant")
else:
    print("origin")
'''

# comsider a character input if it is upper case convert it into lower case , if it is lower case convert it into upper case 
'''
ch = input("enter the character: ")
if 'A' <=ch<='Z':
    print(chr(ord(ch)+32))
elif 'a'<=ch<='z':
    print(chr(ord(ch)-32))
elif '0'<=ch<='9':
    if int(ch)%3==0:
        print(int(ch)%3)
else:
    print(ord(ch))
'''

# wap to print Fizz if the gievn number is multiple fo three , print buzz if the given number is multiple of 5 and print Fizzbuzz is the number is mutliple of both 3 and 5

#wap tp find the smallest of two numbers
'''
a = int(input("enter the number1: "))
b = int(input("enter the number2: "))
c = int(input("enter the number3: "))

if a <= b  and a <= c :
    print("a is smallest")
elif b <= a and b <= c:
    print("b is smallest")
elif c <= a and c <= b:
    print("c is smallest")
'''
