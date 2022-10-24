import string
import argparse
import random

def create_password(length , upper = False, lower = False, digits = False, pun = False):
    """
        Args:
            length(int)
            upper (bool)
            lower (bool)
            digits (bool)
            pun (bool)
        Raises:
            TypeError
        Returns:
            password
    """
    
    pool = ''
    if upper:
        pool += string.ascii_uppercase

    if lower:
        pool += string.ascii_lowercase

    if digits:
        pool += string.digits

    if pun:
        pool = string.punctuation

    if pool == '':
        pool = string.ascii_letters
         
    return (''.join(random.choices(pool, k=length)))




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="password creator")
    parser.add_argument('length', type=int, help="Length of password")
    parser.add_argument('-u', '--upper',  help="Use upper case in password", action="store_true")
    parser.add_argument('-l', '--lower',  help="Use lower case in password", action="store_true")
    parser.add_argument('-d', '--digits', help="Use digits in password", action="store_true")
    parser.add_argument('-p', '--pun',  help="Use punctuation in password", action="store_true")



    args = parser.parse_args()
    print(create_password(args.length, args.upper, args.lower, args.digits, args.pun))