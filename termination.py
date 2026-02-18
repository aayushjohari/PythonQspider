# guess the game 
# import random 
# random.randint(SV, EV)
# It will take the random integer from the specified limits
'''
import random 

system_number = random.randint(1,101)

while True :
    number = int(input("enter the number(1-100): "))

    if number < 1 or number > system_number:
        print("NUMBER SHOUULD BE BETWEEN 1 and 100")
    elif system_number == number:
        print("congratulations you have won")
        break
    else:
        print("Try again")

'''

# prime number with loop
'''
n = int(input("enter the number : "))
count  = 0
for i in range(1 , n+1):
    if n%i  ==  0:
        count +=1
    
if count == 2:
    print("prime number")
else:
    print("not a prime number ")
'''

# otp in 3 attempts

# import random

# otp = random.randint(1000, 9999)

# for i in range(3):

#     n = int(input("enter the otp: "))
    


    


