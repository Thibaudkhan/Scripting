
class Name_Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def name_person(self):

        listing = {}

        for x in self.name:
            listing[x] = {"age": self.age}

        for x, y in listing.items():
            print(x)
            for z, zz in y.items():
                print(z, zz)