"""Try to resolve the following challenges
​
Let's see what the most concise solutions can be...
​
"""


def replace_zeros_by_ones_in_a_string(s):
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
    # return s.replace('0', 'a').replace('1', '0').replace('a', '1')
    return s.translate(s.maketrans('01', '10'))


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
