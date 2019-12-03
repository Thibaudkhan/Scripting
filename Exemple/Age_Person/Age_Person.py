
class Age_Person:

    def __init__(self, info,test):
        self.info = info
        self.test = test

    def name(self, val):
        print(val)
        if val:
            return "toto"

    def other(self):
        print("function Init")

    def age_person(self):

        print()
        print(self.info)

        print("function Init")
        print("Je m'appelle", self.info[0], "et j'ai", self.info[1])
        print("Je m'appelle " + self.info[0] + " et j'ai " + str(self.info[1]))
        print("Je m'appelle %s" % self.info[0], "et j'ai %s" % self.info[1])
        self.other()

        print("test val =>", self.name(True))

