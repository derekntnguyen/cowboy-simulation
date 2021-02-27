#  -*- coding: utf-8 -*-
'''
P6
Derek Nguyen
Created: 2019-03-06
Modified: 2019-03-06
Due: 2019-03-06
'''

# %% codecell

import numpy as np
import matplotlib # used to create interactive plots in the Hydrogen package of the Atom IDE
matplotlib.use('Qt5Agg') # used to create interactive plots in the Hydrogen package of the Atom IDE
import matplotlib.pyplot as plt

# Smithers = 0 90%
# Johson = 1 80%
# Flynn = 2 50%


def shoots(who):
    '''
    Function to determine probability of a shot landing for Smithers, Johnson, and Flynn
    Parameters:
    who, 'Smithers', 'Johnson', 'Flynn' as inputs to determine accuracy of each shot
    '''
    if who == 'Smithers': # Smithers shoots with an accuracy of 90%
        if np.random.uniform() < 0.9:
            shot = 1
        else:
            shot = 0
    elif who == 'Johnson': # Johnson Shoots with an accuracy of 90%
        if np.random.uniform() < 0.8:
            shot = 1
        else:
            shot = 0
    elif who == 'Flynn': # Flynn Shoots shoots with an accuracy of 50%
        if np.random.uniform() < 0.5:
            shot = 1
        else:
            shot = 0

    return shot

def Cowboy_Sim(numTrials = 1000):
    '''
    Simulates the probability of the result of a three way duel with n number of trials. Utilizes function shoots and best strategy of shooting at the best shot.
    Parameters:
    numTrials, a number of trials to be performed
    '''
    Smithers_wins = 0 # Establish intial stats
    Johnson_wins = 0
    Flynn_wins = 0

    for trial in np.arange(numTrials): # Initiate ForLoop for numTrials to be performed
        Smithers_Alive = 1 # set alive status to each cowboy
        Johnson_Alive = 1
        Flynn_Alive = 1

        shootsfirst = np.random.randint(3) # Determines who shoots first

        if shootsfirst == 0:
            if shoots('Smithers') == 1:
                Johnson_Alive = 0 # sets status of Johnson to shot after being hit
            else:
                Johnson_Alive = 1 # sets status of Johnson to not shot after being not hit

        elif shootsfirst == 1:
            if shoots('Johnson') == 1:
                Smithers_Alive = 0 # sets status of Smithers to shot after being hit
            else:
                Smithers_Alive = 1 # sets status of Smithers to not shot after being not hit
        elif shootsfirst == 2:
            Johnson_Alive = 1 # Flynn shoots in the air
            Smithers_Alive = 1

        if Johnson_Alive ==0 & Flynn_Alive == 0:
            Smithers_wins += 1 # establish stats for Smithers

        if Smithers_Alive == 0 & Flynn_Alive == 0:
            Johnson_wins += 1 # establish stats for Johnson

        if Smithers_Alive == 0 & Johnson_Alive == 0:
            Flynn_wins += 1 # establish stats for Flynn

    objects = ('Smithers', 'Johnson', 'Flynn',)
    y_pos = np.arange(len(objects))
    stats = [Smithers_wins, Johnson_wins, Flynn_wins]

    probability = stats / np.sum(stats) # Calculates the probability of each cowboy winning the duel
    print('Probability of Smithers, Johnson, and Flynn Winning is:')
    print(probability)

    plt.bar(y_pos, stats, align='center', alpha=0.5) # Creates Barchart as a visual
    plt.xticks(y_pos, objects)
    plt.ylabel('Number of Wins')
    plt.title('Three Way Duel Results')

Cowboy_Sim()
