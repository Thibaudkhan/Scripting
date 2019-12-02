from Exemple.Age_Person.Age_Person import Age_Person


class Init:

    def __init__(self, name):
        self.name = name

    def init(self):

        print("function Init")
        print("Je m'appelle", self.name)

        Age_Person([self.name, 21],3).age_person()


name = "Antoine"

# launch init file
Init(name).init()
