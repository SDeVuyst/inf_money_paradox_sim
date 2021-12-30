from random import choice
import matplotlib.pyplot as plt
from collections import Counter

list_of_values = []
list_of_flips = []  

def main():
    amount = int(input('How many simulations?\n'))
    simulate(amount)

    # count how many of each instance
    amount_of_flips = Counter(list_of_flips)

    # put the values back into a list
    keys_flips, values_flips = zip(*amount_of_flips.items())

    # calculate average winning
    average_winning = sum(list_of_values) / len(list_of_values)

    # plot the results
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle(f'{amount} simulations')
    ax1.bar(keys_flips, values_flips)
    ax1.set_title('amount of consecutive flips')
    ax2.plot(list_of_flips, list_of_values, 'o')
    ax2.set_title('winnings per amount of flips')
    plt.figtext(0.275, 0.02, f' average winning is {average_winning}', fontsize=10)
    plt.show()

    
def coinflip(current_value=2, amount_of_flips=0):
    # flip coin
    current_coin = choice([True, False])
    amount_of_flips += 1
        
    # flipped on good side, double value and continue playing
    if current_coin == True:
        current_value *= 2
        return(coinflip(current_value, amount_of_flips))

    #flipped on bad side, game ends, return value of your coin
    elif current_coin == False:
        return(current_value, amount_of_flips)


def simulate(amount):
    for i in range(amount):
        flip = coinflip()
        list_of_values.append(flip[0])
        list_of_flips.append(flip[1])


if __name__ == '__main__':
    main()
