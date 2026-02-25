# isalnum()
# it gives true for numeric or alphabet but false for special characters
# s = "hello"
# print(s.isalnum())
# a = "@"
# print(a.isalnum())

# check the guven character us uppercase , lower case , number or symbol
'''
s = input("enter the input: ")

if s.islower():
    print("the input is in lowercase")
elif s.isupper():
    print("the input is in uppercase")
elif s.isdigit():
    print("the input is number")
else :
    print("the input is symbol")
'''

# to check the given char is symbol character or not 
'''
s = input("enter the input: ")
if s.isalnum():
    print("not a spl. character")

else:
    print("sp. character")
'''
'''
s = input("enter the input: ")
if not (s.isalnum()):
    print("sp.charcter")
'''

# extract all the upeercase , lower case , digits and symbols from a given string
'''
s = input("enter the input: ")

upp =""
low =""
digits =""
symbols =""

for i in s:
    if i.isupper():
        upp += i
    elif i.islower():
        low +=i
    elif i.isdigit():
        digits +=i
    else:
        symbols += i

print(upp)
print(low)
print(digits)
print(symbols)
'''

## split function
# this is used to split the string
'''
s = "This is a string"
print(s.split())
list1 = s.split('s')
print(list1)
# count the number of words from a givrn string
print("No. of words are : ", len(list1))
'''  

# extract al the palindrome words from a string

s = "This is a beginer level eye catching Phone"

# s.split()
# out =[]
# for i in s.split():
#     if i == i[::-1]:
#         out.append(i)
# print(out)

#find the longest substring
list1 = s.split()
maxlength = ""

for i in list1:
    if len(i) > len(maxlength):
        maxlength = i
print(maxlength)
    
        
