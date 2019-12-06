import argparse

from Encryption.Encryption import Encryption
from Params.Params import Params


def main():
    """
    :return: init to import params and encryption value
    """

    print(" ")
    print("=================================================")
    print("           ---------------------------           ")
    print("                      Enigma                     ")
    print("           ---------------------------           ")
    print("=================================================")
    print(" ")
    print("Press CTRL + C to quit")
    print(" ")

    POS_ROTOR = {"len_rotors": 3, "rotor1": "I", "rotor2": "II", "rotor3": "III", "rotor4": "VI", "rotor5": "V", "reflector": "UKW-b"}
    CONFIG = Params().detection_file()
    print("In     => ", CONFIG["value"])
    print("Params => ", CONFIG["method"])

    result = Encryption(CONFIG["value"], POS_ROTOR).encryption()
    print("OUT    => ", result)


if __name__ == '__main__':
    #
    # Call the main() function
    #
    main()