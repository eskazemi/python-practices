import random
n , trials  = map(int, input().split())

dead_ends = 0 # The number of dead ends

for t in range(trials):
    a = [[False]* n for i in range(n)] # Create a grid page

    x , y = n//2, n//2 # Start from the center

    while 0 < x < n-1 and 0< y< n-1:
        if a[x-1][y] and a[x+1][y] and a[x][y+1] and a[x][y-1]:
            dead_ends +=1
            break
        a[x][y] = True
        r=random.random()
        if r < 0.25:
            if not a[x+1][y]:
                x +=1
        elif r < 0.5:
            if not a[x-1][y]:
                x -= 1
        elif r < 0.75:
            if not a[x][y+1]:
                y += 1
        else:
            if not a[x][y-1]:
                y -= 1

print(100*dead_ends/trials)
