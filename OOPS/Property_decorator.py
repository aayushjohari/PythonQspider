# class Person:
#     def __init__(self , name  ,age):
#         self.__name = name
#         self.__age = age

#     @property
#     def info(self):
#         print(f'Name is {self.__name} , Age is {self.__age}')

#     @info.setter
#     def info(self, val):
#         self.__name = val

#     @info.deleter
#     def info(self):
#         del self.__name 
#         del self.__age


# ob1 = Person('Aayush' , 23)
# print("Before deletion")
# ob1.info

# del ob1.info
# print('After deletion')
# ob1.info

# class Circle:
#     def __init__(self , radius):
#         self.radius = radius
#     @property
#     def area(self):
#         print(3.14*self.radius**2)

# c1 = Circle(7)
# # print(c1.radius)
# c1.area


class Person:
    def __init__(self , name  ,age):
        self.name = name
        self.__age = age

    
    @property
    def age(self):
        print(self.__age)

    @age.setter
    def age(self, new):
        self.__age = new

ob1 = Person('Aayush' , 23)
print(ob1.name)
ob1.age
print("after modification")
ob1.age =21
ob1.age