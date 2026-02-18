# for a in [1,2,3,4]:
#     print(a)

# print every element of tuple
'''
t = (2,4,5,9,'hii' , True)
for i in t:
    print(i)
'''

# print the character of string
'''
st = 'Hello'
for i in st:
    print(i, end=" ")
'''

#find the lenth of the string whithout len function
'''
st ="python is easy language"
count  = 0
for i in st:
    if i == " ":
        continue
    else:
        count = count+1
print(count)
'''

# wap to extract vowels from the given string

# st = "python is easy language"
# out= ''
# vowels = "AEIOUaeiou"
# for i in st:
#     if i in vowels:
#         out = out+i

# print(out,end =" ")


# wap to replace space by underscore in agiven string

# st = input("entter the string: ")
# out =" "
# for i in st:
#     if i == " ":
#         out = out + "_"
#     else:
#         out=out + i
# print(out)

# wap to check whether the string is palindrome or not without slicing

# st = input("enter the string: ")

# out = ""
# for i in st:
#     out = i + out
# if out == st:
#     print("palindrome")
# else:
#     print("not a palindrome")



# wap to remove the duplicates value from the list

# l = [1,2,3,4,1,2,6,7,4,8,22,4,3,6,6]
# lst= []

# for i in l:
#     if i not in lst:
#         lst.append(i)
# print(lst)

# wap to print all the integers present in the list 

# l = [1,2,4,3,5,5+6j, "True", 2.34]
# lst=  []
# for i in l:
#     if type(i) == int:
#        lst.append(i)

# print(lst) 

# wap to extract all tge lowercases characters in a string only if the ascii value is even 
'''
st = "Hi Nana"
out =""
for i in st:
    if 'a'<=i<='z':
        if ord(i)% 2 == 0:
            out = out+i
print(out)
'''
# wap to extract all the key value pairs frm the dict only if the keys are of string datatype and value are of integers

# d = {"name":"AAYUSH", "age" : 23 , "rollno" : 121}

# for i in d:
#     if d.keys(i) == type(str) and d:

# wap tp extract key value pair only if both are exactly same 

# d = {"name":"AAYUSH", "age" : 23 , "rollno" : 121 , "address": "address"}
# out  ={}
# for i in d:
#     if i == d[i]:
#         out[i] = d[i]
# print(out)

# wap to get the following output  using len function
# output = {'power': 5 , "star": 4}
'''
s = "Power star"
S =s.split()
out  = {}
for i in S:
    out[i] = len(i)
print(out)
'''

# wap to extract all thennon default values from a list
'''
l=['hello' , False , 0.1, 0j, "", set(), 55, 9-3j, [3,3,3]]

for i in l:
    if bool(i) == True:
        print(i , end =" ")
'''


# wap to count the number of occuirences of a specfied character
'''
s = input("enter the string: ")
c = input("enter the character : ")
count = 0

for i in s:
    if i == c:
        count +=1
print(count)
'''

# wap to get the following output
# S= "always keep smiling"
# output = "syawla peek ,gnilims"

# S = "always keep smiling"
# s=S.split()
# out =""
# for i in s:
#     out += i[::-1]+" "
# print(out)

# wap to get the following output

# In = 'push maadi kushi padi'
# # out= {'push': 'ph', 'maadi': 'a', 'kushi':'s', 'padi':'pi'}

# out={}
# d = In.split()
# for i in d:
#     if len(i) % 2 == 0:
#         out[i]=i[0]+i[-1]
#     else:
#         out[i]= i[len(i)//2]
# print(out)

# S=['jiocinema.com' , 'file.py' , 'web.html' , 'amazon.com', 'www.org']
# out =['com' , 'pi' , 'html', 'org']
'''
out  =[]

for i in S:
    ext = i.split('.')[-1]
    if ext not in out:
        out.append(ext)

print(out)
'''

# wap to get the follwoing output
'''
S = ['jiocinema.com' , 'file.py' , 'web.html' , 'amazon.com' ,'www.org' , 'python.py']
# out = {'com':['jiocinema' , 'amazon'] , 'py': ['file','python'], 'html':['web'] ,'org': ['www']}

out={}

for i in S:
    ext = i.split('.')[-1]
    name  = i.split()[0]
    if ext not in out:
        out[ext] = []

    out[ext].append(name)

print(out)
'''

#wap to extract all the string values present in list only if the string is palindrome
'''
lst=['hi','mom','python','madam',True,33,'dad',(1,2,3,9)]

out=[]

for i in lst:
    if type(i)==str:
        if i == i[::-1]:
            out.append(i)
print(out)
'''

# wap to get the follwoing output 
'''
IN = 'abacbaacc'

out = {}

for ch in IN:
    if ch not in out:
        out[ch] = 1
    else:
        out[ch] += 1

print(out)
'''

# wap to retrun the posiitons of  vowels in a string

# st= "aayush"

# for i in range(len(st)):
#     if st[i] in 'AEIOUaeiou':
#         print(st[i], 'is present of',i,'position')

# wap to find the longest word in list

l =['indian', 'hello', 'bye', 'jiocinema', 'bye baby']

gr =l[0]
for i in l :
    if len(i) > len(gr):
        gr =i
print(gr)