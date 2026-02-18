# wap to login into insta with valid username and password 
'''
user  = 'aayush0403'
passw  = 'aayush123'

user = input("enter the username:  ")

if user == user:
    password = input("enter the password: ")
    if password == passw:
        print("login successfully")
    else:
        print("incorrect password")
else:
    print("incorrect username ")
'''

# wap to print middle value of a list only if it is a string
'''
l = [True , 2 , 'hello', 3-7j, 6.9]

if len(l) %2 !=0:
    if type(l[len(l)//2]) == str:
        print(l[len(l)//2]) 
    else:
        print("the middle value is not string")
else:
    print("the length of the list is even ")
'''

#wap to check whther the character is vowel or consonant 
'''
chr = input("enter the character: ")
vowel = 'AEIOUaeiou'
if chr in vowel :
    print(chr, "is the vowel")
else:
    print(chr , 'is the consonant')
'''    
#WAP TO find the greatest of 4 numbers using nestedif
'''
a = int(input("enter the number1: "))
b = int(input("enter the number2: "))
c = int(input("enter the number3: "))
d = int(input("enter the number4: "))

if a > b:
    if a > c:
        if a > d:
            print(a, "is greatest")
        else:
            print(d, "is greatest")
    else:
        if c > d:
            print(c, "is greatest")
        else:
            print(d,"is greatest")
else:
    if b > c:
        if b > d:
            print(b, "is greatest")
        else:
            print(d,"is greatest")
    else:
        if c> d:
            print(c ,"is greatest")
        else:
            print(d, "is greatest")
'''
# wap to print the value if it is even length
'''
n = input("enter the value : ")

if len(n)%2 == 0:
    print(n)
'''

# wap to print the reversed string only if it is starting wuth vowel and ending with consonant and having middle value
'''
s = input("enter the string: ")
vowels = "AEIOUaeiou"
if len(s) %2 != 0:
    if s[0] in vowels:
        if s[-1] not in vowels:
            print(s[::-1])
        else:
            print("ending is not with consonant")
    else:
        print("starting is not with vowels")
else:
    print("string is not odd")
'''

# wap to find the middle characater of a string only if it is a uppercase character
'''
s = input("enter the string: ")

if len(s)%2 != 0:
    if 'A'<= s[len(s)//2]<='Z':
        print(s[len(s)//2])
    else:
        print("the middle value is not uppercase")
else:
    print("the string is even")
'''

# WAP TO FIND THE SECOND GREATEST OF 4 VALUES

a = int(input("enter the number1: "))
b = int(input("enter the number2: "))
c = int(input("enter the number3: "))
d = int(input("enter the number4: "))

if a>b:
    if a>c:
        if a>d:
            if b>c:
                if b>d:
                    print(b , "is 2nd number greatest")
                else:
                    print(d ,"is 2nd greatest")
            else:
                if c>d:
                    print(c , "is 2nd greatest")
        else:
            print(d, "is 2nd greatest")
elif b>a and b>c and b>d:
    if a>c:
        if a>d:
            print(a,"is 2nd greatest")
        else:
            print(d,"is 2nd greatest")
    else:
        if c>d:
            print(c,"is 2nd greatest")
        else:
            print(d,"is 2nd greatest")

elif c >a and c>b and c >d:
    if a>b :
        if a>d:
            print(a,'is 2nd greatest number')
        else:
            print(d,'is 2nd greatest')
    else:
        if b>d:
            print(b ,"is 2nd greatest number")
        else:
            print(d,"is 2nd greatest number")
elif d>a and d>b and d>c:
    if a>b :
        if a>c :
            print(a,"is the 2nd greatest")
        else:
            print(c,"is the 2nd greatest")
    else:
        if b>c:
            print(b,"is the 2nd greatest")
        else:
            print(c,"is the 2nd greatest")
else:
    print("all the numbers are equal")        

# wap to print the last value of a list only if it palindrome string starting with vowel
'''
lst =[10, 20, "level", "madam", "ada"]

vowels = 'AEIOUaeiou'

if type(lst[-1]) == str:
    if lst[-1] == lst[-1][::-1]:
        if lst[-1][0] in vowels:
            print(lst[-1])
        else:
            print("the last element does not start with vowel")
    else:
        print("the last element is not palindrome")
else:
    print("the last element is not string")
'''