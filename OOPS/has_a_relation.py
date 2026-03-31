class Address:
    def __init__(self , state , city , pin):
        self.state = state
        self.city = city
        self.pin = pin
addr1 = Address('Delhi' , 'New Delhi' , 200100)

class Student:
    pass

class Customer:
    def __init__(self , name , phone , addr):
        self.name = name
        self.phone = phone
        self.addr = addr
c1 = Customer('Jai', 876277, addr1)

print(c1.name)
print(c1.phone)
print(c1.addr.city)
print(c1.addr.state)
print(c1.addr.pin)