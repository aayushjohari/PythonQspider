class Person:
    def __init__(self , name  ,age):
        self.__name = name
        self.__age = age

    @property
    def info(self):
        print(f'Name is {self.__name} , Age is {self.__age}')

    @info.setter
    def info(self, val):
        self.__name = val

    @info.deleter
    def info(self):
        del self.__name 
        # del self.__age


ob1 = Person('Aayush' , 23)
del ob1.info
ob1.info

