import matplotlib.pyplot as plt
import numpy as np
import random
import copy
from math import *
from statistics import mean, median,variance,stdev

INF = -1
Going = 0
PlayerLose = 1
MasterLose = 2
MAX_TIME = 2 * 10**3
MAX_SIM  = 2 * 10**3
BET_TIME = 100

class Game:
    # money, money, probability of player winning
    def __init__(self, player = 20, master = INF, p = 0.50):
        self.player = player; self.master = master; self.p = p
    
    # return Going | PlayerLose | MasterLose
    def step(self):
        diff = 0
        if random.random() < self.p: diff = 1
        else: diff = -1
        
        # master has infinite money
        if self.master == INF:
            self.player += diff
            if self.player == 0: return PlayerLose
            else: return Going
        
        # master can bankrupt
        else:
            self.player += diff ; self.master -= diff
            if self.player == 0: return PlayerLose
            elif self.master == 0: return MasterLose
            else: return Going

def simulate(game, trial_num = 500):
    results = [0] * (BET_TIME + 21);
    
    for n in range(0, trial_num):
        game_ = copy.deepcopy(game)
        for i in range(0, BET_TIME):
            result = game_.step()
            if result != Going: break
        results[game_.player] += 1
    
    return results

def simulate12(game, trial_num = 500):
    t_n = 100
    results = [[0 for i in range(t_n)] for j in range(BET_TIME + 21)]

    #combs = calc(80)
    
    for n in range(0, t_n):
        result = simulate(game, trial_num)
        #print(result)
        #print('########')
        for i in range(0, BET_TIME + 21):
            results[i][n] = result[i]
            #print(results[i][n])
    
    #print(results)
    
    mean_result = [0] * (BET_TIME + 21)
    stdev_result = [0] * (BET_TIME + 21)
    for i in range(0, BET_TIME + 21):
        mean_result[i] = mean(results[i])
        stdev_result[i] = stdev(results[i])

    print(mean_result)
    print(stdev_result)

    plt.bar( np.array(range(0, BET_TIME + 21)), np.array(mean_result), yerr = np.array(stdev_result) )
    plt.show()


# ().py simulation_type player_money master_money probability
if __name__ == "__main__":
    game = Game(player=20, master=INF, p=0.44)
    simulate12(game)
