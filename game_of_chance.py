import random

money = 100

#Write your game of chance functions here

def heads_tails(h_or_t, bet):
    num = random.randint(1, 2)
    earnings = 0
    if num == 1:
        winning = 'heads'
        print('heads!')
    else:
        winning = 'tails'
        print('tails!')
    if winning == h_or_t:
        print ('You win')
        earnings += bet
    else:
        print('You loose')
        earnings -= bet
    return earnings
    
    




#Call your game of chance functions here
#heads_tails('tails', 50)
money += heads_tails('tails', 50)
print('You now have %s money' %(money))

