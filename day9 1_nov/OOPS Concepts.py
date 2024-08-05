# // create class and objects

# person
# Attributes-name,age,ph.no,height,
# methods-walk(),talk(),run(),sleep(),eat(),learn()

# objects-amit and durga


# class Person:
#     name = None
#     age = None
#     phno = None
#     gender = None
#     height = None
#
#     # methods
#     def talk(self):
#         print("talk")
#
#     def walk(self):
#         print("walk")
#
#     def run(self):
#         return "i am on the run mode"
#     def sleep(self):
#         return ("i am sleeping")
#
#
# amit_obj= Person()
# amit_obj.name="amit"
# amit_obj.age=25
# amit_obj.phno=345678888
# amit_obj.gender="male"
#
# print(amit_obj)
# print(amit_obj.sleep())
# print(amit_obj.run())

class person:

    def __init__(self,name,age,height):
        self.name=name
        self.height=height
        self.age=age

    def talk(self):
        print(self.name,"can run very fast")

    def act(self):
        print("his age is" ,self.age ,"for a movie role")

Shubham=person('shubham',20,'6ft')
Shubham.talk()
Shubham.act()
