#car as class
#create 2 objects
#2 attributes and 2 methods

class car:

    def __init__(self,color,brand):
        self.color=color
        self.brand=brand

    def start(self):
        print(f"start the engine of {self.brand} which is {self.color} in color")

    def amazing(self):
        print("this car has amazing color that is ",self.color)


car1=car("red","mercedes")
car2=car("black","BMW")

car1.start()
car2.amazing()

