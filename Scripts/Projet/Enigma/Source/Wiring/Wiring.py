"""
Wiring
"""

WIRING = {
    "TURNOVER": ["Q","E","V","J","Z"],
    "ETW": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z', ' ', "'"],
    "alphabetDict": {'G': 7, 'U': 21, 'T': 20, 'L': 12, 'Y': 25, 'Q': 17, 'V': 22, 'J': 10, 'O': 15, 'W': 23, 'N': 14,
                     'R': 18, 'Z': 26, 'S': 19, 'X': 24, 'A': 1, 'M': 13, 'E': 5, 'D': 4, 'I': 9, 'F': 6, 'P': 16,
                     'B': 2, 'H': 8, 'K': 11, 'C': 3},
    "I": ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A',
               'I', 'B', 'R', 'C', 'J'],
    "II": ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P',
               'Y', 'F', 'V', 'O', 'E'],
    "III": ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K',
                'M', 'U', 'S', 'Q', 'O'],
    "VI": ['E', 'S', 'O', 'V', 'P', 'Z', 'J', 'A', 'Y', 'Q', 'U', 'I', 'R', 'H', 'X', 'L', 'N', 'F', 'T', 'G', 'K',
           'D', 'C', 'M', 'W', 'B'],
    "V": ['V', 'Z', 'B', 'R', 'G', 'I', 'T', 'Y', 'U', 'P', 'S', 'D', 'N', 'H', 'L', 'X', 'A', 'W', 'M', 'J', 'Q', 'O',
          'F', 'E', 'C', 'K'],



    "UKW-b": ['E', 'N', 'K', 'Q', 'A', 'U', 'Y', 'W', 'J', 'I', 'C', 'O', 'P', 'B', 'L', 'M', 'D', 'X', 'Z', 'V',
                  'F', 'T', 'H', 'R', 'G', 'S']
}


"""
"ETW"	ABCDEFGHIJKLMNOPQRSTUVWXYZ	 	 	 
"I"	EKMFLGDQVZNTOWYHXUSPAIBRCJ	Y	    Q	1
"II"	AJDKSIRUXBLHWTMCQGZNPYFVOE	M	E	1
"III"	BDFHJLCPRTXVZNYEIWGAKMUSQO	D	V	1
"IV"	ESOVPZJAYQUIRHXLNFTGKDCMWB	R	J	1
"V"	VZBRGITYUPSDNHLXAWMJQOFECK	H	    Z	1
"VI"	JPGVOUMFYQBENHZRDKASXLICTW	HU	ZM	2
"VII"	NZJHGRCXMYSWBOUFAIVLPEKQDT	HU	ZM	2
"VIII"	FKQHTLXOCBJSPDZRAMEWNIUYGV	HU	ZM	2
"Beta"	LEYJVCNIXWPBQMDRTAKZGFUHOS	 	 	 
"Gamma"	FSOKANUERHMBTIYCWLQPZXVGJD	 	 	 
"UKW-b"	ENKQAUYWJICOPBLMDXZVFTHRGS	 	 	 
"UKW-c"	RDOBJNTKVEHMLFCWZAXGYIPSUQ
"""

# (" ".join("ESOVPZJAYQUIRHXLNFTGKDCMWB")).split(" ")