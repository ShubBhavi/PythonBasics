#overriding : same fucntion name in the parent and child

class animal:

    def sound(self):
        print("animal sound")

class dog(animal):

     def sound(self):
         # super().sound()
         print("dog sound")

#if u remove the sound function from the dog and call the dog clas it wil take it from the
#parent. comment it and give it a pass it will work
#
animal=animal()
animal.sound()

dog=dog()
dog.sound()

# by using the dog object we can call the parent function by using the super() key>
