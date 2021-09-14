#! /usr/bin/python3
import string,random
def main():
    while True:
        length=int(input('please inter your perferred password length:'))
        chars=string.ascii_letters+string.digits+'!@#$%%^'
        password=''.join([random.choice(chars) for i in range(length)])
        print('your password :{}'.format(password))
        while True:
            answer=input('do you want another password(y/n):').lower()
            if answer == 'n' or answer == 'y':
                break
        if answer =='n':
            break
 
        
if __name__=="__main__":
    main()    
    
    
