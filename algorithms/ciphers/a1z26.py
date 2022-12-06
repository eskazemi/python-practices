


def encode(plain: str) -> list:
    """
        Args:
            plain(str)
        Raise:
            TypeError
        Return:
            return a list of the numbers representing the Unicode code of a specified character.

    """
    return [ord(elm) - 92 for elm in plain]


def decode(encode: list)-> str:
    
    """
    This function Decodes.

        Args:
            encode(list)
        Raise:
            TypeError
        Return:
            The decoded phrase
            
    """
    return "".join(chr(elm + 92) for elm in encode)
    

print(encode("amir"))
print(decode([5, 17, 13, 22]))