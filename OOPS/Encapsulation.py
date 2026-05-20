## Encapsulation can be done through different access specifier
## public members
##  protected members
## private members 


class Bank :
    bank_name  = "SBI"
    __securitypin = 2421
    def __init__(self , name , addr , bal , pin):
        self.name = name
        self.addr = addr
        self.bal = bal
        self.__pin =  pin

    def get_pin(self):  #get the private members(getter method)
        p = int(input("enter the pin: "))
        if  p == self.__pin:
              print(self.__pin)
        else:
             print("invalid user")

    def change_pin(self):    # set the private method(settter methods)
         p = int(input("enter the pin: "))
         if p == self.__pin:
              new_pin = int(input("New pin: "))
              self.__pin = new_pin
              print("Pin changed succesfully")
         else:
              print("you dont havw access for this operation")

obj1 = Bank("Ayush" , 'Noida' , 1000 , pin = 2026)
# print(obj1.__pin)
# obj1.get_pin()
obj1.change_pin()