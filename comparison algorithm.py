a = input()[::-1]
b = input()[::-1]

if int(a) == int(b):
    a,b = a[::-1], b[::-1]
    print(a+"="+b)
elif int(a) > int(b):
    a,b = a[::-1], b[::-1]
    print(a+">"+b)
else:
    a, b = a[::-1], b[::-1]
    print(a+"<"+b)