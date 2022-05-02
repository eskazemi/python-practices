import random
#May generate similar numbers
def make_random_ints(num,ib,ub):
    rng = random.Random()
    result=[]
    for i in range(num):
        result.append(rng.randrange(ib,ub))

    return result


a = make_random_ints(5,1,13)


def make_random_ints_no_seem(num,x,y):
    
    result = []
    rng = random.Random()
    for i in range(num):
        while True:
            condidate = rng.randrange(x,y)
            if condidate not in result:
                break
            result.append(condidate)
    return result