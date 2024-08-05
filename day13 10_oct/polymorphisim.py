#polymorphism: it allows objects of different classes to be treated as objects of common superclasses

class shape:

   def area(self):
       print("area of shape")

class rectangle(shape):

    def __init__(self,length,breath):
        self.length=length
        self.breath=breath

    def area(self):
        return self.breath*self.length


class circle(shape):

    def __init__(self,radius) :
        self.radius = radius

    def area(self):
        return 3.14* self.radius


shape1=rectangle(3,4)
print(shape1.area())

shape2=circle(20)
print(shape2.area())

shape3=shape()
shape3.area()

print(shape2.area())

#if rect dosent have are then it will call parent area



from abc import ABC,abstractmethod

class animal(ABC):
    @abstractmethod
    def shape(abc):
        print("nothing imp")



