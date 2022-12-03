from string import ascii_letters

def encrypt(input_string,key):
    """
    enctypt
    =======
    Args:
        input_string (str): the plain_text that needs to be encoded 
        key(int): the number of letters to shift the message by
    Raises:
        TypeError
    Returns:
        Encodes a given string with the caesar cipher and returns the encoded message
    """
    alpha=ascii_letters
    encrypted = ''
    for ch in input_string:
        if ch not in alpha:
            encrypted += ch
        else:
            new_key=(alpha.index(ch)+key) % len(alpha)
            encrypted +=alpha[new_key]
    return encrypted


def decrypt(string,key):
    """
    decrypt
    =======
    """
    key *= -1
    return encrypt(string,key)

def brute_force(string):
    """
    A brute force algorithm solves a problem through exhaustion: 
    it goes through all possible choices until a solution is found. 
    The time complexity of a brute force algorithm is often proportional to the input size.
    Brute force algorithms are simple and consistent, but very slow.
    ========
    
    Args:
        string (str)
    Raises:
        TypeError
    Returns:
        A dictionary that contains all possible choices 
    """
    alpha=ascii_letters
    key=1
    result=""
    brute_force_data={}

    while key <= len(alpha):
        result=decrypt(string,key)
        brute_force_data[key]=result
        result=""
        key +=1
    return brute_force_data


def main():
    while True:
        print('-' * 10 + "\n**Menu**\n" + '-' * 10)
        print("1.Encrpyt")
        print("2.Decrypt")
        print("3.BruteForce")
        print("4.Quit")
        choice = input("What would you like to do?: ")
        if choice not in ['1', '2', '3', '4']:
            print ("Invalid choice, please enter a valid choice")
        elif choice == '1':
            strng = input("Please enter the string to be encrypted: ")
            key = int(input("Please enter off-set between 1-94: "))
            if key in range(1, 95):
                print (encrypt(strng.lower(), key))
        elif choice == '2':
            strng = input("Please enter the string to be decrypted: ")
            key = int(input("Please enter off-set between 1-94: "))
            print(decrypt(strng, key))
        elif choice == '3':
            strng = input("Please enter the string to be decrypted: ")
            print(brute_force(strng))
            main()
        elif choice == '4':
            print ("Goodbye.")
            break
main()