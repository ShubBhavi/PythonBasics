class A:
    def methodA(self):
        print("method A")

class B(A):
    def methodb(self):
        print("method A")

class C(A):
    def methodc(self):
        print("method A")

class D(B,C):
    def methodd(self):
        print("method A")

Bigd=D()

Bigd.methodA()
Bigd.methodb()
Bigd.methodc()
Bigd.methodd()