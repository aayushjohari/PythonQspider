# class Demo:

#     def  __init__(self):
#         print("This is constructor")
#         print(id(self))

# ob1 = Demo()
# print(f"the address of obj1--{id(ob1)}")
# # ob2 = Demo()

# ob2= Demo()
# print(f"the address of obj2 ---{id(ob2)}")


class Bank:

    def __init__(self , owner_name , balance = 0):
        self.owner_name  = owner_name 
        self.balance = balance

    def deposit(self , amount):
        self.balance = self.balance + amount
        print(f"the amount is deposited , now your new balance is {self.balance}")
        

ob1 = Bank("Aayush" , 5000)
print(ob1.owner_name, ob1.balance)

