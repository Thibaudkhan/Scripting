
class Age_Person:

    def __init__(self, info):
        self.info = info

    def age_person(self):

        print("function Init")
        print("Je m'appelle", self.info[0], "et j'ai", self.info[1])
        print("Je m'appelle " + self.info[0] + " et j'ai " + str(self.info[1]))
        print("Je m'appelle %s" % self.info[0], "et j'ai %s" % self.info[1])