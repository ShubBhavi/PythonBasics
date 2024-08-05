class animal:

      def car(self):
          print("merc")


      def speak(self):
          print("animal speak")

class dog(animal):

    def speak(self):
        print("bow bow ")

    def drive(self):
        animal() .car()

Dog=dog()
Dog.speak()
Dog.car()
Dog.drive()
Dog.speak()


#


class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Dog barks")

# Creating an instance of Dog
my_dog = Dog()

# Accessing methods from the parent class
my_dog.speak()  # Output: Animal speaks

# Accessing method from the subclass
my_dog.bark()   # Output: Dog barks
# In this example:
#
# Animal is the parent class with the speak() method.
# Dog is the subclass inheriting from Animal.
# Both classes have their respective methods, and the subclass Dog can access methods from the parent class Animal.