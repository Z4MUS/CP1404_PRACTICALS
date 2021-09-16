"""
CP1404/CP5632 Practical
Hex colours in a dictionary
"""

HEX_COLOUR_CODES = {"gray9": "171717", "firebrick": "b22222", "cyan1": "00ffff", "blue1": "0000ff", "black": "000000", "azure1": "f0ffff", "brown": "a52a2a", "beige": "f5f5dc", "burlywood": "deb887", "cadetblue": "5f9ea0"}

raw_colour = input("what colour would you like the hexadecimal code for: ").lower()
while raw_colour != "":
    if raw_colour in HEX_COLOUR_CODES:
        print(f"the code for {raw_colour} is #{HEX_COLOUR_CODES[raw_colour]}")
    else:
        print("invalid code")
    raw_colour = input("what colour would you like the hexadecimal code for: ").lower()