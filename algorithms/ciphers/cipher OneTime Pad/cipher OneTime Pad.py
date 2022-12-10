import random
user_input = input("phrase: ")

class OneTime():
    def encrypt(self,text):
        plain=[ord(i) for i in text]
        cipher=[]
        key=[]
        for i in plain:
            k=random.randint(1,300)
            c=(i+k)
            cipher.append(c)
            key.append(k)
        return cipher,key
    def decrypt(self,key,cipher):
        plain=[]
        for i in range(len(key)):
            p=int((cipher[i] - key[i]))
            plain.append(chr(p))
        result=''.join([i for i in plain])
        return result

c,k=OneTime().encrypt(user_input)
print(c)
print(k)
print(OneTime().decrypt(k,c))