import string
import random

def password_info():
    """
    Args:
         No argumnet
    Raises:
        KeyError : Invalid input please enter True or False!
    Returns:
        dict container length, upper, lower, digits, pun
    """
    length = int(input("length password: "))
    while True:
        try:
            upper =  {"true":True,"false":False}[input("Do you want to include uppercase letters? True or False? ").lower()]
            lower =  {"true":True,"false":False}[input("Do you want to include lowercase letters? True or False? ").lower()]
            digits =  {"true":True,"false":False}[input("Do you want to include digits letters? True or False? ").lower()]
            pun =  {"true":True,"false":False}[input("Do you want to include punctuation letters? True or False? ").lower()]
            return {"length": length, "upper": upper, "lower": lower, "digits": digits, "pun":pun}
        except KeyError:
            print("Invalid input please enter True or False!")
   
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




args = password_info()
print(create_password(args.get("length"), args.get("upper"), args.get("lower"), args.get("digits"), args.get("pun")))