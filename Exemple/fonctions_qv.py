class Conversion:

    #
    # convert_str_to_list
    #
    '''Spliter une chaîne de caractère en liste'''
    def split(word):
        return [char for char in word]

    word = 'ABC'
    print(split(word))
    '''Resort une chaîne de caractère'''

#
# convert_list_to_str
#
''' Convertir une liste de caractère en une chaîne'''
liste = ["A", "B", "C"]
chaine = "".join(liste)

print(chaine)
'''Ressort une chaîne de caractère'''

#
# convert_binary_on_eight_bit
#
'''Ajouter des zéro devant les chaînes de caractères pour obtenir huit bit'''

binary = ["1000001", "1000010", "1000011", "01"]

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
'''resort les chaînes en huit bit'''