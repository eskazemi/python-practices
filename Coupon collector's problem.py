#Coupon collector problem
#Having several types of cards, how many cards should be selected in order to have at least one of each type of card? 
#(We assume that in each choice, the probability of choosing the cards is equal to each other).

import random

n = int(input())

count = 0 # number of selected cards
collected_count = 0 # several types of cards are selected
is_collected = [False]*n # array boolean
while collected_count < n:
    count += 1
    value = random.randrange(0,n)
    if not is_collected[value]:
        collected_count += 1
        is_collected[value] = True

print(count)