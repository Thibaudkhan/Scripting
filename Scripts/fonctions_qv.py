def convert_str_to_list(word):
    '''Spliter une chaîne de caractère en liste'''
    return [char for char in word]


word = 'ABC'
print(convert_str_to_list(word))


def convert_list_to_str(liste):
    ''' Convertir une liste de caractère en une chaîne'''
    chaine = "".join(liste)
    return chaine


liste = ["A", "B", "C"]
print(convert_list_to_str(liste))


def convert_binary_on_eight_bit(binary):
    '''Ajouter des zéro devant les chaînes de caractères pour obtenir huit bit'''

    nb_tab = len(binary)
    x = 0

    while x < nb_tab:

        longueur = len(binary[x])
        #    print(longueur)

        while longueur < 8:
            binary[x] = "0" + binary[x]
            longueur += 1
        print(binary[x])

        x += 1


binary = ["1000001", "1000010", "1000011", "01"]
print(convert_binary_on_eight_bit(binary))
