from Source.Wiring.Wiring import *


class Rotor:

    def __init__(self, ROTOR):
        self.ROTOR = ROTOR

    def letter_rotor(self, method, letter, dictionnary, rotor, indice_rotor):
        '''
        :return: return the letter according to the parameters
        '''

        if method == 1:
            a = dictionnary[letter]
            b = rotor[a + indice_rotor]
            """
            if letter in WIRING["TURNOVER"]:
                WIRING["TURNOVER"].index(letter)
            """
        else:
            a = rotor.index(dictionnary)
            b = WIRING["ETW"][a]
        return b

    def rotation_Rotor(self, result):
        '''
        :param result:
        :return: rotate a rotor in params
        '''

        result.append(result[0])
        del result[0]
        return result

    def move_rotor(self, nb_exec):
        '''
        :param nb_exec:
        :return: if condition for move rotor is True
        '''

        """
        def turnover(rotor):
            Rotor(self.ROTOR).rotation_Rotor(WIRING[self.ROTOR[rotor]])
        """

        if (nb_exec + 1) % 1 == 0:
            Rotor(self.ROTOR).rotation_Rotor(WIRING[self.ROTOR["rotor1"]])
            # if turn is True:
                # turnover("rotor2")
        if (nb_exec + 1) % 26 == 0:
            Rotor(self.ROTOR).rotation_Rotor(WIRING[self.ROTOR["rotor2"]])
            # if turn is True:
                # turnover("rotor3")
        if (nb_exec + 1) % 676 == 0:
            Rotor(self.ROTOR).rotation_Rotor(WIRING[self.ROTOR["rotor3"]])
            # if turn is True:
                # turnover("rotor4")