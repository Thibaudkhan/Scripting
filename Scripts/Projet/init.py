alphabetList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z', ' ', "'"]
alphabetDict = {'G': 7, 'U': 21, 'T': 20, 'L': 12, 'Y': 25, 'Q': 17, 'V': 22, 'J': 10, 'O': 15, 'W': 23, 'N': 14,
                'R': 18, 'Z': 26, 'S': 19, 'X': 24, 'A': 1, 'M': 13, 'E': 5, 'D': 4, 'I': 9, 'F': 6, 'P': 16, 'B': 2,
                'H': 8, 'K': 11, 'C': 3}

rotor1 = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I',
          'B', 'R', 'C', 'J']
rotor2 = ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y',
          'F', 'V', 'O', 'E']
rotor3 = ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M',
          'U', 'S', 'Q', 'O']
reflector = ['E', 'N', 'K', 'Q', 'A', 'U', 'Y', 'W', 'J', 'I', 'C', 'O', 'P', 'B', 'L', 'M', 'D', 'X', 'Z', 'V', 'F',
             'T', 'H', 'R', 'G', 'S']


def rotation_Rotor(result):
    result.append(result[0])
    del result[0]
    return result


def Validate(result):
    for x in result:
        if alphabetList.count(x.upper()) < 1:
            return False
    return True


print("Welcome to the enigma machine")
message_List = []
while Validate(message_List) == False or len(message_List) <= 0:
    try:
        message = str(input("Write the message do you want to crypt/decrypt: \n"))
        message_List = list(message)
    except:
        print("You must only enter letter without special characters!")
s = []
for i in range(0, len(message_List), 1):
    if message_List[i] == ' ':
        s.append(' ')
    elif message_List[i] == "'":
        s.append("'")
    else:
        print("rotor1 => ", rotor1)
        print("rotor2 => ", rotor2)
        print("rotor3 => ", rotor3)
        a = alphabetDict[message_List[i].upper()]
        # print(a)
        b = rotor1[a - 1]
        print(b)
        c = alphabetDict[b]
        # print(c)
        d = rotor2[c - 1]
        print(d)
        e = alphabetDict[d]
        # print(e)
        f = rotor3[e - 1]
        print(f)
        g = alphabetDict[f]
        # print(g)
        h = reflector[g - 1]
        print(h)
        j = rotor3.index(h)
        # print(j)
        k = alphabetList[j]
        print(k)
        l = rotor2.index(k)
        # print(l)
        m = alphabetList[l]
        print(m)
        n = rotor1.index(m)
        # print(n)
        o = alphabetList[n]
        print(o)
        s.append(o)
    if (i + 1) % 1 == 0:
        rotation_Rotor(rotor1)
    if (i + 1) % 26 == 0:
        rotation_Rotor(rotor2)
    if (i + 1) % 676 == 0:
        rotation_Rotor(rotor3)

print("crypted/decrypted message: ", ''.join(s))
