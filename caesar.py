
def encrypt(text, rot):
    """ receives a string, rotates the characters by the the integer rot and
        returns the new string
    """
    if type(rot) != int:
        rot = int(rot)
    # if text is not a string, return text
    if type(text) is not str:
        return text
    # encrypt and return the new string
    new_string = ""
    for i in range(len(text)):
        new_string += rotate_character(text[i], rot)
    return new_string

def alphabet_position(letter):
    """ receives a single character string and
        returns the 0-based index alphabet position
    """
    # calculate position based on lowercase characters
    letter = letter.lower()
    position = ord(letter) - 97
    return position

def rotate_character(char, rot):
    """ receives a single character string and an integer to rotate by
        returns the new char based on rotating to the right by rot
    """
    # return char if it is not a letter
    if not char.isalpha():
        return char
    # rotate position
    old_pos = alphabet_position(char)
    new_pos = (old_pos + rot) % 26
    # preserve original case
    if char.islower():
        new_pos += 97
    else:
        new_pos += 65
    # calculate and return new character
    char = chr(new_pos)
    return char
