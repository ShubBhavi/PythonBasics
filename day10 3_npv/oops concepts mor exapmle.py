class Myclass():
    name=None
    height=None


    def myname(self,lastname,age,gender):
        print("your name is "+ self.name,lastname,age,gender)

    def Run(self):
        print("running with a height of "+str(self.height))


shubham_obj= Myclass()
rahul_obj=Myclass()

shubham_obj.name="shubham"
rahul_obj.name="rahul"
shubham_obj.height=6
rahul_obj.height=5
shubham_obj.myname("bhavi",24,"male")
rahul_obj.myname("buchadi",26,"male")
shubham_obj.Run()
rahul_obj.Run()
