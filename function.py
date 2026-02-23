# fuction without argument and with return key word
'''
def add():
    a = int(input("enter the number1: "))
    b = int(input("enter the number2: "))
    # print(a+b)
    return a+b

print(add())
'''

# to check whether the string is palindrome or not
'''
def palindrome():
    s = input("enter the string: ")
    out =""
    for i in s:
        out = i+out
    if s == out:
            return 'palindrome'
            return True
    else:
         return "Not"
print(palindrome())
'''

# to check whther the number is palindrome or not 
'''
def palindrome():
    n  = int(input("enter the number: "))
    original = n
    rev =0
    while n != 0:
        ld  = n%10 
        rev = rev * 10 + ld
        n = n//10
    if  rev == original :
        return "palindrome"
    return "not palindrome"

print(palindrome())
'''


# to check whether the number is strong or not 
'''
def strong():
    n = int(input("enter the number: "))
    original = n
    sum = 0

    while n != 0:
        ld = n%10

        fact = 1
        for i in range(1,ld+1):
            fact = fact*i

        sum+=fact
        n=n//10

    if sum == original :
        return "strong"
    return "not strong"

print(strong())
'''

## function with argument and with return keyword

# to add_2 number
'''
def add(a,b):
    return a+b
print(add(3,4))
'''

# to check whether the number is strong or not without while loop
'''
def strong(num):

    original  =  num

    sum  = 0

    for i in str(num):
        # i = int(i)
        fact = 1
        for j in range(1 , int(i)+1):
            fact = fact*j
        sum = sum + fact
    if sum == original:
        return "strong"
    return "not strong"

num = int(input("enter the number: "))
print(strong(num))
'''

# find the strong number between the given range
'''
def strong(num):

    original  =  num

    sum  = 0

    for i in str(num):
        # i = int(i)
        fact = 1
        for j in range(1 , int(i)+1):
            fact = fact*j
        sum = sum + fact

    return sum  == original

for i in range(1, 1000001):
    if strong(i):
        print(i)
'''

# find the second largest element in the list

def second_largest():

    l = eval(input("enter the list: "))

    if len(l) <=1:
        return None
    
    larg = l[0]

    slarg = None

    for i in l:
        if i > larg:
            slarg = larg
            larg = i

        elif i != larg:
            if slarg == None or slarg < i :
                slarg = i

    return slarg

print(second_largest())

    
# to find the third largest number

def third_largest():

    l = eval(input("enter the list: "))

    larg = l[0]

    slarg = None

    tlarg = None

    