# for i in range(1,6):
#     for j in range(1,6):
#         print(i,j)

# wap to get the following output
# s = 'Power star'.split()

# # out ={'Power':5, 'Star':4}

# out ={}

# for i in s:
#     count = 0
#     for j in i :
#         count +=1
#     out[i]=count
# print(out)


# wap to get the following output
s= 'kabab is love'.split()
out ={}
# out = {'kabab': ['babak',2,'kbb'] , 'is': ['si', 1, 'i'], 'love':['evol', 2,'lv']}
# vowels ='AEIOUaeiou'
# for i in s:
#     rev = i[::-1]


#     vowel  = 0
    
    #  for j in i :
#         if j in vowels:
#             vowel +=1
    
#     even_char = ''
#     for k in range(len(i)):
#         if k % 2 == 0:
#             even_char +=i[k]
    
#     out[i] = [rev , vowel , even_char]

# print(out)  


# for i in s:
#     count  =0
#     char =''

#     for j in range(len(i)):
#         if i[j] in 'AEIOUaeiou':
#             count +=1

#         if j % 2 ==0:
#             char += i[j]

#     out[i] = [i[::-1], count , char]
# print(out)

# wap to get the followiing output
'''
s = 'kabab is love'.split()

out ={}

for i in s:
    cons = 0
    char = ''

    for j in range(len(i)):

        if i[j] not in 'AEIOUaeiou':
            cons+=1
            char+=i[j]

    out[i[0]+i[-1]] = [char , cons , char[::-1]]

print(out)
'''

# wap to get the following output

# IN = 'bacbcaabbaa'
# # out = 'b4a5c2'
# out =''
# for i in IN:
#     if i not in out:
#         count = 0
#         for j in IN:
#             if j == i:
#                 count+=1
#         out += i + str(count)
# print(out)       

# wap tp get the following output

# In = [100, 200,50,400,300,150,125,175]
# N = 300
# out = [[100,200],[300],[150,150],[125,175]]


# In = ["hello", 227 , 3.4 , "last", 189, 34]
# # out = [722,981,43]
# out=[]
# for i in In:
#     s =0
#     if type(i)== int:
        
#         while i!=0:
#             ld = i%10
#             s =s*10 +ld
#             i = i//10
#     if s!=0:
#         out.append(s)
# print(out)

In = [100,200, 35, 40,60]
# # out = [335,235,400,395,375]
out =[]
# sum = 0
# for i in In:
#     sum +=i
    
# for num in In:
#     out.append(sum -num)

# print(out)
    
for i in In:
    to = 0
    for j in In:
        if i != j:
            to+=j
    out.append(to)
print(out)


    



       