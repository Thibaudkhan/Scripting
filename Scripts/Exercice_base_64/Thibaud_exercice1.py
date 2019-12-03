my_list = ["A", "B"]
my_char = "eurhgiebgierngieubrgioehngienfginegda"
my_list_b = ["Aaaaa", "Bddddddd", "fzfzfzf"]


#
## convert string to list
#
def convert_str_to_ascii(my_list):
    for x in my_list:
        print(ord(x))

    return ord(x)


def convert_string_to_six_bit(my_list_bit):
    # print(my_char.split(0::6))
    list_six_bit = [my_char[i:i + 6] for i in range(0, len(my_char), 6)]
    print(list_six_bit)
    return list_six_bit


def rezise_str_to_multiple_of_eight(my_list):
    for i in range(0, len(my_list)):
        while len(my_list[i]) < 7:
            my_list_b[i] += "="
            print(my_list_b)
    return my_list_b


convert_str_to_ascii(my_list)
convert_string_to_six_bit(my_char)
rezise_str_to_multiple_of_eight(my_list_b)
