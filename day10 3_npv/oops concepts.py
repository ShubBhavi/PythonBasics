#car
#objects: tesla ,lambo,merc

class car:
    name=None
    colour=None
    Mode=None
    speed=None

    def start(self):
        return "engine started"

    def drive(self):
        return "automatic"

    def Break(self):
        return "the stopped car name is "+self.name



tesla=car()         #car is a objecta nd tesla is just a reference
tesla.name="Tesla"
tesla.speed="very fast"

print(tesla.name)
print(tesla.drive())


lambo= car()
lambo.name="Lambo"

print(tesla.Break())
print(lambo.Break())

