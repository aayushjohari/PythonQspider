# factorial number
'''
def fact(n):
    if n == 0 or n ==1:
        return 1
    return n * fact(n-1)

print(fact(5))
print(fact(4))
'''

# sum of n natural numbers
'''
def sumofnumbers(n):
    if n < 1:
        return  0
    return n + sumofnumbers(n-1)

print(sumofnumbers(5))
'''
# product of n natural numbers
'''
def product_natural(n):
    if n < 1:
        return 1
    return n * product_natural(n-1)

print(product_natural(5))
'''
# fibonacci series
'''
def fibonacci_no(n):
    if n == 0:
        return 0 
    if n == 1:
        return 1
    return fibonacci_no(n-1) + fibonacci_no(n-2)

n = int(input("enter the number: "))
for i in range(n+1):
    print(fibonacci_no(i) , end = " ")
'''
'''
def fibonacci_series(n , a =0 , b= 1):
    if n < 1:
        return 
    print(a , end = " ")
    return fibonacci_series(n-1 , b , a+b)

(fibonacci_series(5))
'''

# palindrome number
'''
def palindrome(n):
    num = str(n)
    if len(num) ==0 or len(num)==1:
        return True
    elif num[0] != num[-1]:
        return False
    return palindrome(num[1:-1])

print(palindrome(121))
'''

#mirror number
'''
def mirror_no(n):
    if n ==1:
        print(1 , end=" ")
        return
    print(n,end=" ")
    mirror_no(n-1)
    print(n , end=" ")

mirror_no(4)
'''
'''
def mirror_number(n):
    if n ==1:
        return str(n)
    return str(n) + mirror_number(n-1) + str(n)
print(mirror_number(4))
'''
'''
def prime(n ,  i=2):
    if n <=1:
        return False
    if n ==i:
        return True
    elif  n %i ==0 :
        return False
    return prime(n , i+1)

print(prime(5))
print(prime(1))
print(prime(2))
'''

# print 10 to 1
'''
def num(n):
    if n == 0:
        return 
    print(n , end=" ")
    num(n-1)

num(10)
'''

# print sum of n natural numbers

def sum_natural(n):
    if n <= 1:
        return 0
    