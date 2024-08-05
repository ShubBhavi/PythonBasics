# #Encapsulation
# #Data members and methods together in class
# #person -> name,age
# #methods-> eat(),sleep()
#
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand             # Public attribute
#         self._model = model            # Protected attribute
#         self.__serial_number = 12345   # Private attribute
#
#     def drive(self):
#         print("Driving")
#
#     def _repair(self):
#         print("Repairing")
#
#     def __upgrade(self):
#         print("Upgrading",self.brand)
#
#
# # Creating an instance of the Car class
# my_car = Car("Toyota", "Corolla")
#
# # Accessing public attributes and methods
# print(my_car.brand)     # Output: Toyota
# my_car.drive()          # Output: Driving
#
# # Accessing protected attributes and methods
# print(my_car._model)    # Output: Corolla
# my_car._repair()        # Output: Repairing
#
#
# print(my_car.drove())'



class person:

    def __init__(self,name,height):
        self.name=name
        self._height=height
        self.__age=451

    def talk(self):
        print("he speaks very loud and his name is",self.name)

    def _hei(self):
        print("his height is",self._height)

    def __ag(self):
        print("his age is ",self.__age)

    def getage(self):
        print(self.__age)


per=person('shubham',5)

print(per.name)

print(per._height)


per.getage()