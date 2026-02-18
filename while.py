# wap to print helloworld 5 times
'''
a= 1
while a<6:
    print("hello world")
    a=a+1
'''

# 3 wap to print first 10 natural numbers
'''
i = 1
while i<11:
    print(i)
    i+=1
'''

# wap to print all the even numbers from 1 t0 10
'''
i =1
while i < 11:
    if i % 2 == 0:
        print(i)
    i=i+1
'''
#wap to print sum of n natural numbers
'''
n = int(input("enter the number: "))

i = 0
sum = 0
while i <=n:
    sum = sum + i
    i=i+1
print(sum)
'''

# wap to print multiplications table for n 
'''
n = int(input("enter the table number: "))
i =1
while i <= 10 :
    print(f"{n} * {i} ={n*i}")
    i= i+1
'''

# wap to find the product of n natural number of factorial of a number
'''
n = int(input("enter the number :  "))
fact  = 1
i =1
while  i  <= n:
    fact  = fact * i
    i+=1
print(fact)
'''

# wap to print all the characters of a string
'''
s = input("enter the string: ")
i = 0
while i < len(s):
    print(s[i])
    i+=1
'''

# wap to print all the characters present at even index of a string
'''
s = input("enter the string: ")

i = 0
while i < len(s):
    if i%2 == 0:
        print(s[i])
    i+=1
'''

# wap to extrext all the lowercase letters in a string
'''
s = input("enter the string: ")

i = 0
while i < len(s):
    if 'a'<=s[i]<='z':
        print(s[i] , end =" ")
    i+=1
'''

# wap to to extract all the vowels in a string
'''
s = input("enter the string: ")
vowels = 'AEIOUaeiou'
i =0
while i < len(s):
    if s[i] in vowels:
        print(s[i])
    i +=1
'''

# wap to print factors of a integer number
'''
n = int(input("enter the number: "))

i =2
while  i < n :
    if n % i ==0:
        print(i , end =" ")
    i+=1
'''

# wap to toggle the string
'''
s = input("enter the string: ")
result = ""
i = 0
while i < len(s):
    
    if 'a'<=s[i]<='z':
        result += chr(ord(s[i])-32)
    elif 'A'<= s[i] <='Z':
        result += chr(ord(s[i])+32)
    else:
        result += s[i]
    i+=1

print(result)
'''

# wap to reverse the given number
'''
n= int(input("enter the number: "))
rev = 0 
while n > 0 :
    ld = n % 10 
    rev = rev*10 + ld
    n = n//10

print(rev)
'''    
# wap to find the sum of individual digits of a number
'''
n = int(input("enter the number: "))

sum = 0

i = 1

while n > 0 :

    digit = n % 10

    sum = sum + digit

    n= n//10

print(sum)
'''

# wap to check whether the number is perfect or not 
'''
n = int(input("enter the number: "))
sum  = 0
original = n
i=1
while i < n:
    if n % i == 0:
        sum = sum + i
    i+=1

if sum == original :
    print("yes the given number is perfect")
else:
    print("the number is not the perfect number")
'''

# wap to extract all the even integers present in a tuple at odd index 
'''
t = (1,22,3,44,5,'hello', True , 3 , 44 , 66 , 7,7,77,89,96)
out =[]
i = 0
while i < len(t):
    if i%2 != 0:
        if type(t[i])==int and t[i]%2 == 0:
            out.append(t[i])
    i+=1
print(out)
'''

# wap to remove duplicates from a list without converting into set
'''
l = [2,3,4,5,6,7,5,54,3,3,3,344,5,6,7,8,7,6,4,3,2,2]
lst =[]
i = 0
while i < len(l):
    if l[i] not in lst:
        lst.append(l[i])
    i+=1
print(lst)
               
'''
#wap  to find the greatest number in a given list

# l = eval(input("enter the list: "))

# gr = l[0]
# i = 0
# while i < len(l):
#     if l[i]> gr:
#         gr = l[i]
#     i+=1

# print(gr)

# wap tp finf the cube of a number ina string
'''
st = 'Hel5_3 uE9'
total = 0
i = 0
while i < len(st):
    if '0' <= st[i] <= '9':
        total = total + int(st[i])**3
    i+=1
print(total)
'''

# wap to check whether the number is Armstrong or not 

# n = int(input("enter the number: "))

# num = n
# k = len(str(num))
# total = 0

# if n == 0:
#     total = 0
# else:
#     while n > 0:
#         last_digit = n % 10
#         total += last_digit ** k
#         n //= 10

# if total == num:
#     print("the number is armstrong")
# else:
#     print("no it is not armstrong")

# wap to chevk whther the number is prime 

# n = int(input("enter the number:  "))

# c = 0
# i=2

# while i < n :
#     if n % i == 0:
#         c+=1
#     i+=1
# if c == 0:
#     print("prime number")
# else:
#     print("not a prime number")
