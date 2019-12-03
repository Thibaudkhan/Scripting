my_list = ["A","B"]
my_char = "eurhgiebgierngieubrgioehngienfginegda"
my_list_b = ["Aaaaa","Bddddddd","fzfzfzf"]
#
## convert string to list
#


def convert_str_to_ascii(my_list):
    listing = []
    for x in my_list:
        listing.append(ord(x))

    return listing


def convert_string_to_six_bit(my_list_bit):
    #print(my_char.split(0::6))
    list_six_bit = [my_list_bit[i:i + 6] for i in range(0, len(my_list_bit), 6)]
    return list_six_bit


def rezise_str_to_multiple_of_eight(list_to_convert):
    while len(list_to_convert) % 8 != 0: # ou 4 (info tibo)
        list_to_convert += "="
    return list_to_convert

def convert_str_to_list(word):
    '''Spliter une chaîne de caractère en liste'''
    return [char for char in word]


def convert_list_to_str(liste):
    ''' Convertir une liste de caractère en une chaîne'''
    chaine = "".join(liste)
    return chaine


def convert_binary_on_eight_bit(binary):
    '''Ajouter des zéro devant les chaînes de caractères pour obtenir huit bit'''

    listing = []

    nb_tab = len(binary)
    x = 0

    while x < nb_tab:

        longueur = len(binary[x])
        #    print(longueur)

        while longueur < 8:
            binary[x] = "0" + binary[x]
            longueur += 1
        listing.append(binary[x])

        x += 1

    return listing



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


def convert_ascii_to_binary(list_to_convert):
    return [bin(i).replace("0b", "") for i in list_to_convert]



def convert_binary_to_decimal(list_to_convert):
    return [int(i, 2) for i in list_to_convert]




l_1 = convert_str_to_list("ABCD")
print("l_1 => ", l_1)
l_2 = convert_str_to_ascii(l_1)
print("l_2 => ", l_2)
l_3 = convert_ascii_to_binary(l_2)  # ===
print("l_3 => ", l_3)
l_4 = convert_binary_on_eight_bit(l_3)
print("l_4 => ", l_4)
l_5 = convert_eight_bit_to_string(l_4)
print("l_5 => ", l_5)
l_6 = convert_string_to_six_bit(l_5)
print("l_6 => ", l_6)
l_7 = convert_binary_to_decimal(l_6)  # ===
print("l_7 => ", l_7)
l_8 = convert_decimal_to_ascii_character(l_7)
print("l_8 => ", l_8)
l_9 = convert_list_to_str(l_8)
print("l_9 => ", l_9)
l_10 = rezise_str_to_multiple_of_eight(l_9)
print("l_10 => ", l_10)
