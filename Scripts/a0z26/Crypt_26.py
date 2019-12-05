
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
to_decrypt = int(input())

def decrypt(number):
    result = ''
    quotient = number

    if(number == 0):
        result = alphabet[0] + result
        print("0 ::"+result)

    while quotient != 0:
        dividende = quotient
        quotient = round(dividende/26)
        division_euclidienne = dividende % 26
        result = alphabet[division_euclidienne] + result
        print(result)
    return result

decrypt(to_decrypt)