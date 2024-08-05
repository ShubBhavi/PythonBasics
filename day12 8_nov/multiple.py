class father:

    def dad_money(self):
        print("take son,its your money")


class mother:

    def mom_money(self):
        print("take son,its your money")

class son(father,mother):
  pass

son=son()
son.mom_money()
son.dad_money()
