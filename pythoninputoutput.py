## write a program to check whether the number is even or not
'''
n = int(input("enter the number: "))

if n % 2 ==0:
        print("n is even")
else:
    print("n is odd")
'''
## program to check whether thr string has exactly 5 characters in it
'''
s = input("enter the string: ")
if len(s) == 5:
    print("the string has 5 charcters")
else:
    print("no it doesnot have 5 characters")
'''
# program to check the number is greater than 200
'''
n = int(input("enter the number: "))
if n > 200:
    print("true")
'''
# program to print square of a number only if it is multiple of 3
'''
n = int(input("enter the number: "))
if n % 3 == 0:
    print(n**2)
'''

#wap to print the square of a number if it is even
'''
n = int(input("enter the number: "))
if n %2 ==0:
    print(n**2)
else:
    print("n is not even")
'''
## wap to check whther the character is vowel
'''
s = input("enter the character: ")
vowel = 'aeiou'
if s in vowel :
    print("yes , the char is vowel")
else:
    print("the char is not a vowel")
'''

## wap to print ascii value only if it uppercase
'''
s = input("enter the charater: ")

if s == s.upper():
    print(ord(s))
'''
##
'''
n = int(input("enter the number: "))
if n % 9 == 0 and n % 6 ==0:
    print(n**3)
else:
    print("the number is not divisible by 9 and 6")
'''

##

n = int(input("enter the number: "))
count = 0
n  = n%10
