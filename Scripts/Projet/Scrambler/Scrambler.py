from Scripts.Projet.Scrambler.Rotor.Rotor import Rotor


class Scrambler:

    def __init__(self, CONFIG):
        self.CONFIG = CONFIG

    def scrambler(self):

        print(" ")
        print("# ------------------------------------------------------------------ #")
        print("# =========================== Scrambler ============================ #")
        print("            ---------------------------------------------             ")
        print("# =========================== Scrambler ============================ #")
        print("# ------------------------------------------------------------------ #")
        print(" ")

        print("self.CONFIG['message'] =>", self.CONFIG["message"])
        result = []

        print(" ")
        for x in self.CONFIG["message"]:
            print("-------------------------------")
            print(x)
            print("-------------------------------")
            print(Rotor(x.upper()).init_rotor())
            result.append(x)
        print(" ")

        return "".join(result)
