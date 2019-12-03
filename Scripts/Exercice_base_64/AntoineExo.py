import base64

encoded = base64.b64encode(b'oui')
data = base64.b64decode(encoded)

print(" ")
print(" == Result == ")
print(data)
print(encoded)
print(" ")

print(" ===== Exo === ")

toto = "ABCD"


def convert_str_to_list(list_to_convert):
    """
    convert string to list
    """
    return [i for i in list_to_convert]


def convert_str_to_ascii(list_to_convert):
    """
    convert string to list
    """
    return [ord(i) for i in list_to_convert]


def convert_ascii_to_binary(list_to_convert):
    """
    convert ascii to binary
    """
    return [bin(i).replace("0b", "") for i in list_to_convert]


def convert_binary_on_eight_bit(list_to_convert):
    """
    convert binary on eight bit
    """
    return ["0" * (8 - len(i)) + i for i in list_to_convert if len(i) < 8]


def convert_eight_bit_to_string(list_to_convert):
    """
    convert eight bit to string
    """
    return "".join(list_to_convert)


def convert_string_to_six_bit(list_to_convert):
    """
    convert string to six bit
    """
    return [list_to_convert[i:i + 6] for i in range(0, len(list_to_convert), 6)]


def convert_binary_to_decimal(list_to_convert):
    """
    convert binary to decimal
    """
    return [int(i, 2) for i in list_to_convert]


def convert_decimal_to_ascii_character(list_to_convert):
    """
    convert decimal to ascii character
    """
    l = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    return [l[i] for i in list_to_convert]


def convert_list_to_str(list_to_convert):
    """
    convert list to str
    """
    return "".join(list_to_convert)


def rezise_str_to_multiple_of_eight(list_to_convert):
    """
    rezise str to multiple of eight
    """
    while len(list_to_convert) % 8 != 0:
        list_to_convert += "="
    return list_to_convert


l_1 = convert_str_to_list(toto)
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

# =====================================================================
# =====================================================================
# =====================================================================
