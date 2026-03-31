

# operator overloading
'''
class Arithmetic:
    pass

ob1 = Arithmetic()
ob2 = Arithmetic()

print(ob1+ob2)
'''

class Arithmetic:
    def __init__(self , a):
        self.a = a

    def __add__(self , other):#magic_method
        return self.a + other.a
    

ob1 = Arithmetic(10)
ob2 = Arithmetic(20)

# print(ob1 +ob2)
print(ob1 + ob2)
print(ob1-ob2)

