class car:

     def __init__(self,make,model):
         self.make=make
         self.model=model
         print("i will be called first")

     def star(self):
         print("start the car",self.make,self.model)

car_obj=car("toyota","camry")
car1_obj=car("merc","s class")

car_obj.star()