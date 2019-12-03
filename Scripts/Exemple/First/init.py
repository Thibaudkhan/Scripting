from Scripts.Exemple.First.Age_Person.Age_Person import Age_Person
from Scripts.Exemple.First.Name_Person.Name_Person import Name_Person


class Init:

    def __init__(self, name, list_name):
        self.name = name
        self.list_name = list_name

    def init(self):

        print("function Init")
        print("Je m'appelle", self.name)

        Age_Person([self.name, 21]).age_person()
        Name_Person(self.list_name, 20).name_person()




name = "Antoine"
list_name = ["Antonin", "Thibaude", "Quentin", "Antoine"]

# launch init file
Init(name, list_name).init()
