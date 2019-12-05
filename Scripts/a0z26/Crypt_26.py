alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U','V', 'W', 'X', 'Y', 'Z']
alphabetCode = ['NC', 'OD', 'PD', 'QD', 'RD', 'SD', 'TD', 'UD', 'VD', 'WD', 'XD', 'YD', 'ZD', 'AD', 'BD', 'CD', 'DD','ED', 'FD', 'GD', 'HD', 'ID', 'JD', 'KD', 'LD', 'MD']

def convert_str_to_ascii(my_list):
    listing = []
    list = my_list[0]
    for x in list:
        listing.append(ord(x))

    print(listing)
    return listing


def crypt(number):

    quotient = 0
    result = ""
    for i in number:
        quotient += i

        if(number == 0):
            result = alphabet[0] + result
            print("0 ::"+result)

        while quotient != 0:
            dividende = quotient
            quotient = round(dividende/26)
            division_euclidienne = dividende % 26
            result +=  alphabet[division_euclidienne]
        result += " "
    print(result)
    return result

def decrypt(to_decrypt):

    tab = to_decrypt[0].split()
    decoded = ''
    for y in tab:
        i = 0
        for x in alphabetCode:
            if y == x:
                decoded += alphabet[i]
            i += 1
    print(decoded)
    return decoded

def call_crypt():
    with open("test.txt", "r") as myfile:
        data = myfile.readlines()
        list_ascii = convert_str_to_ascii(data)
        list_crypted = crypt(list_ascii)
        crpt = open("crypted_file.txt", "w")
        crpt.write(list_crypted)
        crpt.close()

def call_decrypt():
    with open("crypted_file.txt", "r") as mf:
        d = mf.readlines()
        list_decrypted = decrypt(d)
        dcrpt = open("decrypted_file.txt", "w")
        dcrpt.write(list_decrypted)
        dcrpt.close()



call_crypt()
call_decrypt()
