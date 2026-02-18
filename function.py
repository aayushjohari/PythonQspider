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