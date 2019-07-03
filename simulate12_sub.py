import matplotlib.pyplot as plt
import numpy as np
import random
import copy
from math import *

INF = -1
Going = 0
PlayerLose = 1
MasterLose = 2
MAX_TIME = 2 * 10**3
MAX_SIM  = 2 * 10**3
    

def calc(k):
    return [ factorial(k)/(factorial(i)*factorial(k-i)) for i in range(k+1)]
    

def simulate12(trial_num = 2000):
    results = [0.0] * 101;
    combs = calc(80)
    
    for n in range(2, 101):
        if n%2 == 1: continue
        if 0 <= -n/2+30: 
            results[n] = trial_num * ( combs[int(n/2)+30] - combs[int(-n/2)+30] ) / 2**80
        else: results[n] = trial_num * ( combs[int(n/2)+30] ) / 2**80
    
    print(results)
    plt.bar( np.array(range(0, 101)), np.array(results) )
    plt.xlabel("player's money") ; plt.ylabel("times") ; plt.title("after 80 bets")
    plt.show()


# ().py simulation_type player_money master_money probability
if __name__ == "__main__":
    simulate12()
