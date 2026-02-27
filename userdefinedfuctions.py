# create alist of 5 values using the input from the user
'''
def list_of_five(n): #parameter / fromal argument
    list1 =[]
    for i in range(n):
        data  = eval(input("enter the data: "))
        list1.append(data)
    
    print(list1) 
list_of_five(3) #value / actual argument
'''

## Positional argument vs keyword argument  vs default argument
'''
def person_info(name , age , email):
    print(f"Name is {name}")
    print(f"Age is {age}")
    print(f"Email is {email}")

person_info("Python" , 18 , "abc@gmail.com")

def person_info(name , age , email):
    print(f"Name is {name}")
    print(f"Age is {age}")
    print(f"Email is {email}")

person_info(name = "Python" , age = 18 , email = "abc@gmail.com")

def person_info(name , age , email ="NA"):
    print(f"Name is {name}")
    print(f"Age is {age}")
    print(f"Email is {email}")

person_info(name = "Python" ,age =18 ,)
'''

## variable length argument vs variable lemgth keyword argument
'''
def collect_students(*args):
    print(args)

collect_students("AAYUSH" ,"PYTHON")
collect_students()

def get_sum(*args):
    sum(args)

get_sum(100,200,200,300)

def collect_students(**kwargs):
    print(kwargs)

collect_students(name = "AAYUSH" , sub ="PYTHON")
collect_students()
'''

# create a function which can extract all the palindrome number from a list
'''
def filter_palindrome(list1):
    out= []
    for i in list1:
        if type(i) == int and str(i)[::-1] == str(i):
                out.append(i)
    print(out)
filter_palindrome([45,22,3,"level"])
'''

# create a function which gives the factorial of a number 
'''
def factorial(num):
     fact = 1
     for i in range(1, num+1):
          fact = fact*i
     print(fact)

factorial(5)
'''
#fucntion with return keyword
'''
l1 = [10,20,'hi' , 'java']

value = l1.pop(-2) # return the value
print("romoved value --" , value)
print(l1)
'''
'''
l1 = [10,20,'hi' , 'java']

value = l1.remove('java') # does not return the value
print("romoved value --" , value)
print(l1)
'''
'''
def demo():
    return 10

data = demo()
print(data)

'''
'''
def mul_10(n):
    return n*10
# print(mul_10(10))
'''

# li = ['hi' , 2.33 , 3 , 'python',8,5,6-4j]
# out =30,50,80

#print the integers my multiplying 10 from given list
'''
def filter_int(list1):

    for i in list1 :
        if type(i) == int:
            print(mul_10(i))

filter_int([1,2,3,'python','java'])
'''

# create a function which pop first value from the list 
'''
def remove_first(list1):

    value = list1.pop(0)
    print(value)
l = [1,2,3,"hy","bye"]
remove_first(l)
print(l)

def removefirst_withoutpop(list1):
    first_value = list1[0]
    list1.remove(first_value)
    return first_value

l1 = ["bye",2,3,"hi"]
print(removefirst_withoutpop(l1))
print(l1)
'''
# find the function which return the length of the collection
'''
def count_length(list1):
    count  =0 
    for i in list1:
        count+=1
    return count

# l1 = [1,2,3,4,5]
print(count_length("hello"))
print(count_length({10 , 'hello' , (1,2,3) , (10,20,30)}))
'''
# create a functuon to count the digits of a given number
# with while loop
'''
def count_digits(n):
    n = abs(n)
    if n == 0:
        return 1
    
    count  = 0
    while n != 0:
        count +=1
        n=n//10
    return count

num  = int(input("enter the number: "))
print(count_digits(num))
'''

# with for loop
'''
def count_digits(n):
    num  = abs(n)
    count = 0
    for i in str(num):
        count+=1
    return count

print(count_digits(000))
'''

# count the floating values of the given number

# def count_float(n):
#     num =str(n).split('.')
#     return len(num[-1])
    # x = num[1]
    # # count = 0
    # # for i in x:
    # #     count+=1
    # # return count
# n = float(input("enter the number: "))
# print(count_float(n))
        


# create a function returns bolean value
'''
def is_odd(val):
    if val %2 != 0:
        return True
    return False

n = int(input("enter the number: "))
print(is_odd(n))
'''

'''
def is_even(val):
    
    if n %2 == 0:
        return True
    return False

n = int(input("enter the number: "))
print(is_even(n))
'''
 
'''
def is_palindrome(val):
    if str(val) == str(val)[::-1]:
        return True
    return False

# n = input("enter the value: ")
# print(is_palindrome(n))
'''


def is_prime(val):
    if val <= 1:
        return False
    for i in range(2 , int(val**0.5)+1):
        if val%i == 0:
            return False
    return True

# val = int(input("enter the value : "))
# print(is_prime(val))


def is_armstorng(val):

    num = val
    total= 0
    power = len(str(num))
    while num > 0:
        ld   = num%10
        total  += ld ** power
        num  = num//10
    
    if total == val:
        return True
    return False

# val = int(input("enter the number: "))
# print(is_armstorng(val))

'''
def is_spy(val):
    if val  < 0:
        return False
    
    total  = 0
    product = 1
    while val > 0:
        ld  = val%10
        total  +=ld
        product *=ld
        val = val//10
    if total  == product:
        return True
    return False

val = int(input("enter the number: "))
print(is_spy(val))
'''
# create a function to extract all the vowels from a given string , it should return list
'''
def extract_vowels(string):
    out =[]
    for i in string:
        if i in "AEIOUaeiou":
            out.append(i)
    print(out)
string = input("enter the string: ")
extract_vowels(string)
'''
'''
def extract_consonants(string):
    out =[]
    for i in string:
        if i not in "AEIOUaeiou":
            out.append(i)
    print(out)
string = input("enter the string: ")
extract_consonants(string)
'''
'''
def filter_digits(string):
    for i in string: 
        if i.isdigit():
            print(i)
string = input("enter the string: ")
filter_digits(string)
'''
'''
def filter_zeros(string):
    result =""
    for i in string:
        if i !="0":
            result +=i
    return result

string = input("enter the string: ")
print(filter_zeros(string))
'''

# def floating_count(n):
#     count  = 0
#     while n!= int(n):
#         count +=1
#         n *=10
#     return count

# print(floating_count(1.23445))

# extract all the float values having only two flaoting values

'''
li = [2.32,10,5,5.231,98,32,42,3.141]

def extract_floating(li):
    for i in li:
        if type(i) == float and count_float(i) ==2:
            print(i)

extract_floating(li)
'''

#wap to print all the palindrome number in a  given range
'''
n = int(input("enter the number: "))
def palindrome_series():
    for i in range(1,n+1):
        if is_palindrome((i)):
            print(i , end=" ")

palindrome_series()
'''

# filter all the plaindrome numbers from a given list
'''
def filter_palindrome(list1):
    for i in list1:
        if is_palindrome(i):
            print(i , end= " ")

l1 = eval(input("enter the list: "))
filter_palindrome(l1)
'''

# primeno. series
'''
def prime_no_series(n):
    for i in range(1, n):
        if is_prime(i):
            print(i , end=" ")
n = int(input("enter the number: "))
prime_no_series(n)
'''
'''
def armstrong_series(n):
    for i in range(1, n+1):
        if is_armstorng(i):
            print(i , end=" ")

n = int(input("enter the number: "))
armstrong_series(n)
'''

# nth prime number

def nth_prime_no(n):
    count  = 0
    num  =1
    while count  < n :
        num+=1
        if is_prime(num):
            count+=1

    return num

n = int(input("enter the n : "))
print(nth_prime_no(n))
