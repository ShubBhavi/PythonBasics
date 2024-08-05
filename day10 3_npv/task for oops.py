#car as class
#create 2 objects
#5 attributes and 5 methods

class car():
    color=None
    name=None
    tyre=None
    brand=None

    def speed(self):
        print(self.brand + "\truns very fast")

    def gears(self):
        print("has 6 gears" + self.brand)

    def Break(self):
        print("stop the car")

    def engine(self):
        print("has v8 engine ")


color_car=input("enter the color ")
car_name=input("enter the name of the car")
car_brand=input("entre the brand of car ")

car_obj=car()
car_obj.color=color_car
car_obj.name=car_name
car_obj.brand=car_brand

car_obj.gears()
car_obj.speed()
