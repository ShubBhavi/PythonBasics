#multilevel inheritance

class grandparents:

      def grandparent(self):
          return "garandparent are savage"


class parent(grandparents):

    def parent(self):
        return "partens are very cool"

class kids(parent):

    def kid(self):
        return "kids are dope"


child=kids()

print(child.grandparent())
print(child.parent())
print(child.kid())