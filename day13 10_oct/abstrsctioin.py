# abstraction: Hiding the imp details and showing what is required
# hiding the core implementation and show only the imp details
# to represent complex systems by simplifying  and hiding unecessary details
# ABC: Abstract base class
#other child function who extendes from the parent has to complete the functionality .


from abc import ABC,abstractmethod

class animal(ABC):
        @abstractmethod
        def sound(self):
             print("unknown task for animal")

class dog(animal):

    def sound(self):
       print("bow bow ")

class cat(animal):

  def sound(self):
            print("meow meow ")

class tiger(animal):

    def sound(self):
        print("grgrrrrrrr!!")

animal=cat()
animal.sound()

animal1=dog()
animal1.sound()

animal1=tiger()
animal1.sound()


