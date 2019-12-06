"""Try to resolve the following challenges
​
Let's see what the most concise solutions can be...
​
"""


def replace_zeros_by_ones_in_a_string(string_to_transform):
    """
​
    Args:
        string_to_transform: The string to transform
​
    Returns:
        The transformed string where zeros are replaced by ones and ones are replaced by zeros
​
        As an example:
            string_to_transform = '00100010001011101' should be transformed to '11011101110100010'
​
    """
    transformed_string = ''
    for i in string_to_transform:
        if i == "0":
            transformed_string += "1"
        elif i == "1":
            transformed_string += "0"
    return transformed_string


def main():
    """Main function
​
    Returns:
​
    """
    orginal_string = '000111'
    resulting_string = replace_zeros_by_ones_in_a_string(orginal_string)
    print(f"Orginal string  : {orginal_string}")
    print(f"Resulting string: {resulting_string}")


if __name__ == '__main__':
    main()