class parent:

    def dad(self):
     print("hello childerns")

class son(parent):

    def son(self):
        print("dad your son need a car ")

class sister(parent):

    def sis(self):
        print("dad i want iphone")


son=son()
sis=sister()

son.dad()
son.son()
sis.sis()