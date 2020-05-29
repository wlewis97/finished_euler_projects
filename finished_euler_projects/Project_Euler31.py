# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?
import math as m

#as there is only 1 way to make £2 using a £2 coint, we'll add that way to our calculation at the end
total = 0 #initialise counter
for one_pound in range(0,3): # as possible number of pound coins are 0,1 or 2:
    for fifty_p in range(0,m.floor(((200 - one_pound*100)/50))+1): #calculates maximum number of 50ps we could use by subtracting the value of already used coins from the aim of 200p, that number divided of the value of the coin, rounded down, gives the total number of coing that could be used in that instance
        for twenty_p in range(0,m.floor(((200 - one_pound*100 - fifty_p*50)/20))+1): #same as for fifty pence but accounts for number of 50 ps
            for ten_p in range(0,m.floor(((200 - one_pound*100 - fifty_p*50 - twenty_p*20)/10))+1):
                for five_p in range(0, m.floor(((200 - one_pound*100 - fifty_p*50 - twenty_p*20 - ten_p*10) / 5)) + 1):
                    for two_p in range(0,
                                        m.floor(((200 - one_pound*100 - fifty_p*50 - twenty_p*20 - ten_p*10 - fifty_p*5) / 2)) + 1):
                        total += 1 #1p coins will fill whatever defecit of money there is and as that is the only way to make 2 pounds using only 1ps we can add this possible way to the total
total += 1 #accounting for 2 pound coin possibility
print(total)