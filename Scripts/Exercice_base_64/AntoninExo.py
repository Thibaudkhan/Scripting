chaine_eight_bit = ["01011000", "00011101", "01110001", "00100111", "00111010"]
decimals = [16, 20, 9, 3, 17, 0]


def convert_eight_bit_to_string(list_to_convert):
    """Permet la conversion d'une liste contenant des chaînes de caractères en chaine de caractères contenant toutes les
     données de la liste en entrée.

        :type list_to_convert: list
    """
    return "".join(list_to_convert)


def convert_decimal_to_ascii_character(list_to_convert):
    """Permet la conversion d'une liste contenant des entiers en liste contenant les caractères équivalents de ces
    entiers en ASCII.

        :type list_to_convert: list
    """
    for i in range(len(list_to_convert)):
        # On remplace l'entier présent dans la liste par le caractère en ascii (chr) + 65 car les
        # caractères alphanumériques en ASCII commencent à 65
        list_to_convert[i] = chr(list_to_convert[i] + 65)

    return list_to_convert


print(convert_eight_bit_to_string(chaine_eight_bit))
print(convert_decimal_to_ascii_character(decimals))