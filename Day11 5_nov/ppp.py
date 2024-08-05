class Password:

    def __init__(self,password):
        self.__password=password

    def  get_pass(self):
        return  self.__password

    def set_pass(self,password ):
        if len(password)>10:
            self.__password=password

        else:
            print("weak password")


    def print_len(self):
        print("length of my password is ",len(self.__password))

pass_obj=Password("hacker")

pass_obj.print_len()

print(pass_obj.get_pass())

pass_obj.set_pass("danger1234565432")


print(pass_obj.get_pass())