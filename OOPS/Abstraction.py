from abc import ABC , abstractmethod

class Vehicle:
    @abstractmethod
    def check_engine(self):
        pass

    def check_light(self):
        pass

class Car(Vehicle):
    def check_engine(self):
        print("Engine is checked ....")

    def check_light(self):
        print("Light is checked.....")


ob1 =  Car()
ob1.check_engine()
ob1.check_light()