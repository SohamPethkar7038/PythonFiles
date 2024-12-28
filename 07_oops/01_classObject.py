# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.

# make the class name capital

'''
1. Basic Class and Object
Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.

2. Class Method and Self
Problem: Add a method to the Car class that displays the full name of the car (brand and model).

3. Inheritance
Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

4. Encapsulation
Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

5. Polymorphism
Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

6. Class Variables
Problem: Add a class variable to Car that keeps track of the number of cars created.


7. Static Method
Problem: Add a static method to the Car class that returns a general description of a car.

8. Property Decorators
Problem: Use a property decorator in the Car class to make the model attribute read-only.

9. Class Inheritance and isinstance() Function
Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.
10. Multiple Inheritance

Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

'''


class Car:
    
    total_car=0;
    def __init__(self,userbrand,usermodel):
        self.__brand=userbrand
        self.model=usermodel
        Car.total_car+=1;
        
    def fullName(self):
        return f"{self.brand} {self.model}"
    
    def get_brand(self):
        return self.__brand+"!";
    
    def fuelType(self):
        return "Petrol or Diesel";
    
    @staticmethod
    def generalDescription():
        return "transport purpose"


class ElectricCar(Car):
    def __init__(self,userbrand,usermodel,battery_size):
        super().__init__(userbrand,usermodel)
        self.batterySize=battery_size;
    
    def fuelType(self):
        return "Electri charge";
    
my_tesla=ElectricCar("tesla","model W","85khw");
#print(my_tesla.model)
# print(my_tesla.fuelType())

safari=Car("tata","Safari 123");
# print(safari.fuelType())

# print(Car.generalDescription())   # access by clas Car not by object i.e static method
# 


my_Car=Car("Toyata","fortuner")
# print(my_Car.brand)
# print(my_Car.model)
# print(my_Car.fullName())

my_newCar=Car("tata","Nexon")
# print(my_newCar.brand)
# print(my_newCar.fullName())


# print(Car.total_car)


# print(isinstance(my_tesla,Car))


class Battery:
    def battery_info(self):
        return "this is battery";

class Engine:
    def engineInfo():
        return "this is engine";


class ElectricCarTwo(Battery,Engine,Car):
    pass

my_new_tesla=ElectricCarTwo("tesla","model E")