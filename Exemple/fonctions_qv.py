class Age_Person:

    #
    # convert_str_to_list
    #
    def split(word):
        return [char for char in word]

    word = 'ABC'
    print(split(word))


#
# convert_list_to_str
#
liste = ["A", "B", "C"]
chaine = "".join(liste)

print(chaine)

#
# convert_binary_on_eight_bit
#

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