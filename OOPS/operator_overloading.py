

# operator overloading
'''
class Arithmetic:
    pass

ob1 = Arithmetic()
ob2 = Arithmetic()

print(ob1+ob2)
'''
'''
class Arithmetic:
    def __init__(self , a):
        self.a = a

    def __add__(self , other):   #magic_method
        return self.a  - other.a
    

ob1 = Arithmetic(10)
ob2 = Arithmetic(20)

# print(ob1 +ob2)
# print(ob1 + ob2)
print(ob1+ob2) 
'''

class Myclass:
    def __init__(self , var):
        self.item = var

    def __len__(self):
        return len(self.item)
    
    def __getitem(self , index):
        return self.item(index)

    def __setitem(self , index , value):
        self.item[index] =  value

    def __contains__(self, var):
        return var  in self.item

ob1 = Myclass(10,20,30)
print(ob1[0])
print(ob1[-1])
ob1[-1] = 300



