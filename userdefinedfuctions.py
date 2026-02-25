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

def count_float(n):
    num =str(n).split('.')
    return len(num[-1])
    # x = num[1]
    # # count = 0
    # # for i in x:
    # #     count+=1
    # # return count
n = float(input("enter the number: "))
print(count_float(n))
        




# n = 5.45
# num = str(n)
# x =num.split('.')
# print()
# print(x[1])
