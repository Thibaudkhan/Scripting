# from Scripts.Projet.COIL.Coil import *


class Rotor:

    def __init__(self, letter):
        self.letter = "H"

    def init_rotor(self):

        temp = {}

        ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ROTOR_1  = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
        ROTOR_2  = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
        ROTOR_3  = "BDFHJLCPRTXVZNYEIWGAKMUSQO"

        REFLECTEUR = "ENKQAUYWJICOPBLMDXZVFTHRGS"

        def rotor(first, second, letter, x):
            init = first.index(letter) + x
            return second[init]

        # ┌- v < -- e < -- p < -- v < -- h < -- h < -- h(IN)
        # └ > t --> q --> y --> v --> m --> m -->      m(OUT)

        print(self.letter)
        l = rotor(ALPHABET, ROTOR_1, self.letter, 1)
        print(l)
        print(" ")
        l = rotor(ROTOR_1, ROTOR_2, l, 0)
        print(l)

        l = rotor(ROTOR_2, ROTOR_3, l, 0)
        print(l)

        # rotor 2 => p

        l = rotor(ALPHABET, ROTOR_1, self.letter, 1)

        rotor_2 = ROTOR_1.index(l) + 1
        print(rotor_2)
        rotor_2_1 = ROTOR_2[rotor_2]
        print(rotor_2_1)
        print(" ")

        # rotor 2 => e

        rotor_3 = ROTOR_3.index(rotor_2_1)
        print(rotor_3)
        rotor_3_1 = ROTOR_3[rotor_3]
        print(rotor_3_1)

        print(" ")
        
        reflecteur = REFLECTEUR.index(rotor_3_1) + 1
        print(reflecteur)

        rotor_3_r = ROTOR_3[reflecteur]
        print(rotor_3_r)
        rotor_2_r = ROTOR_2.index(rotor_3_r) + 1
        print(rotor_2_r)

        rotor_1_r = ROTOR_1[rotor_2_r]
        print(rotor_1_r)










        '''
        for i, j in ROTOR_1.items():
            temp[j] = i
        for i, j in temp.items():
            print('"' + i + '": ' + str(j) + ",")
        
        print(self.letter)
        base = ALPHABET_2[(self.letter)]
        print("base +> ", base)
        rotor_1 = ROTOR_1[base]
        print("rotor_1 +> ", rotor_1)
        rotor_2 = ALPHABET_2[rotor_1]
        print("rotor_2 +> ", rotor_2)
        '''