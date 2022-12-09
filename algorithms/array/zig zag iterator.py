input_user_1 = list(map(int, input("array 1: ").split())) 
input_user_2 = list(map(int, input("array 2: ").split())) 

class ZigZag:

    def __init__(self,l1,l2):
        self.que=[l1,l2]

    def next(self):
        v=self.que.pop(0)
        r=v.pop(0)
        if v:
            self.que.append(v)
        return r

    def has_next(self):
        if self.que:
            return True
        return False

z=ZigZag(input_user_1,input_user_2)

while z.has_next():
    print(z.next(),end=" ")