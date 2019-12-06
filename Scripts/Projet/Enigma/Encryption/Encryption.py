from Encryption.Rotor.Rotor import Rotor
from Source.Wiring.Wiring import *


class Encryption:

    def __init__(self, value, ROTOR):
        self.value = value
        self.ROTOR = ROTOR

    def encryption(self):
        """
        :return: encryption value according to the parameters
        """

        def isValidate(result):
            for x in result:
                if WIRING["ETW"].count(x.upper()) < 1:
                    return False
            return True

        # ====
        message_List = []
        list_result = []
        # ====

        while isValidate(message_List) == False or len(message_List) <= 0:
            try:
                message_List = list(self.value)
            except:
                print("You must only enter letter without special characters!")

        for i in range(0, len(message_List), 1):
            if message_List[i] == ' ':
                list_result.append(' ')
            elif message_List[i] == "'":
                list_result.append("'")
            else:
                int_rotor_1 = Rotor(self.ROTOR).letter_rotor(1, message_List[i].upper(), WIRING["alphabetDict"], WIRING[self.ROTOR["rotor1"]], -1)
                int_rotor_2 = Rotor(self.ROTOR).letter_rotor(1, int_rotor_1, WIRING["alphabetDict"], WIRING[self.ROTOR["rotor2"]], -1)
                int_rotor_3 = Rotor(self.ROTOR).letter_rotor(1, int_rotor_2, WIRING["alphabetDict"], WIRING[self.ROTOR["rotor3"]], -1)
                if self.ROTOR["len_rotors"] > 3:
                    int_rotor_4 = Rotor(self.ROTOR).letter_rotor(1, int_rotor_3, WIRING["alphabetDict"], WIRING[self.ROTOR["rotor4"]], -1)
                    if self.ROTOR["len_rotors"] == 5:
                        int_rotor_5 = Rotor(self.ROTOR).letter_rotor(1, int_rotor_4, WIRING["alphabetDict"], WIRING[self.ROTOR["rotor5"]], -1)
                        center_reflector = Rotor(self.ROTOR).letter_rotor(1, int_rotor_5, WIRING["alphabetDict"], WIRING[self.ROTOR["reflector"]], -1)
                        out_rotor_5 = Rotor(self.ROTOR).letter_rotor(0, WIRING["alphabetDict"], center_reflector, WIRING[self.ROTOR["rotor5"]], "")
                        out_rotor_4 = Rotor(self.ROTOR).letter_rotor(0, WIRING["alphabetDict"], out_rotor_5, WIRING[self.ROTOR["rotor4"]], "")
                    else:
                        center_reflector = Rotor(self.ROTOR).letter_rotor(1, int_rotor_4, WIRING["alphabetDict"], WIRING[self.ROTOR["reflector"]], -1)
                        out_rotor_4 = Rotor(self.ROTOR).letter_rotor(0, WIRING["alphabetDict"], center_reflector, WIRING[self.ROTOR["rotor4"]], "")
                    out_rotor_3 = Rotor(self.ROTOR).letter_rotor(0, WIRING["alphabetDict"], out_rotor_4, WIRING[self.ROTOR["rotor3"]], "")
                else:
                    center_reflector = Rotor(self.ROTOR).letter_rotor(1, int_rotor_3, WIRING["alphabetDict"], WIRING[self.ROTOR["reflector"]], -1)
                    out_rotor_3 = Rotor(self.ROTOR).letter_rotor(0, WIRING["alphabetDict"], center_reflector, WIRING[self.ROTOR["rotor3"]], "")
                out_rotor_2 = Rotor(self.ROTOR).letter_rotor(0, WIRING["alphabetDict"], out_rotor_3, WIRING[self.ROTOR["rotor2"]], "")
                out_rotor_1 = Rotor(self.ROTOR).letter_rotor(0, WIRING["alphabetDict"], out_rotor_2, WIRING[self.ROTOR["rotor1"]], "")

                list_result.append(out_rotor_1)

        return ''.join(list_result)
