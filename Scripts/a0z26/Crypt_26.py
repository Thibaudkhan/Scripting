alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U','V', 'W', 'X', 'Y', 'Z']
alphabetCode = ['NC', 'OD', 'PD', 'QD', 'RD', 'SD', 'TD', 'UD', 'VD', 'WD', 'XD', 'YD', 'ZD', 'AD', 'BD', 'CD', 'DD','ED', 'FD', 'GD', 'HD', 'ID', 'JD', 'KD', 'LD', 'MD']

class Base:

    def __init__(self):
        pass

    #
    ##Convert text from test.txt to code code ascii
    #
    def convert_str_to_ascii(self,my_list):
        """
        convert my_list to new aschii array
        :param my_list: string array from test.txt
        :return: int array
        """
        listing = []
        list = my_list[0]
        for x in list:
            listing.append(ord(x))

        print(listing)
        return listing


    def crypt(self,list_ascii):
        """
        convert code ascii to code a0z25
        :param list_ascii : int array
        :return string array  :
        """
        quotient = 0
        result = ""
        for i in list_ascii:
            quotient += i

            if(i == 0):
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

    def decrypt(self,to_decrypt):

        """
        decrypt a0z25 message
        :param to_decrypt: int array
        :return: string message
        """
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

    def call_crypt(self):
        """
        call cryptage method and write in crypted_file.txt the crypted message
        :return: void
        """
        with open("To_crypt.txt", "r") as myfile:
            data = myfile.readlines()
            list_ascii = self.convert_str_to_ascii(data)
            list_crypted = self.crypt(list_ascii)
            crpt = open("crypted_file.txt", "w")
            crpt.write(list_crypted)
            crpt.close()

    def call_decrypt(self):
        """
        call decrypatge method and write in decrypted_file.txt the decrypted message
        :return: void
        """
        with open("To_decrypt.txt", "r") as mf:
            text_crypted = mf.readlines()
            list_decrypted = self.decrypt(text_crypted)
            dcrpt = open("decrypted_file.txt", "w")
            dcrpt.write(list_decrypted)
            dcrpt.close()


b = Base()
b.call_crypt()
b.call_decrypt()
