import matplotlib.pyplot as plt
import numpy as np
import random
import copy
from math import *
from statistics import mean, median,variance,stdev
from time import sleep

INF = -1
Going = 0
PlayerLose = 1
MasterLose = 2
MAX_TIME = 580
MAX_SIM  = 15000

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

def simulate13(game, sim_num = MAX_SIM, max_time = MAX_TIME):
    times = [0] * (max_time+1)
    
    for i in range(0, sim_num):
        game_ = copy.deepcopy(game)
        cnt = 0;
        for j in range(1, max_time+1):
            cnt += 1
            result = game_.step()
            if result != Going: times[cnt] += 1; break;
    
    solution = [0] * (max_time+1)
    sol = sim_num / 2**20
    
    for t in range(20, max_time+1, 2):
        solution[t] = sol
        a = (t-20)/2
        sol *= (2*a*a + 41*a + 210)/(2*a*a + 44*a + 42)
    
    plt.plot( np.array(range(0, max_time+1)), np.array(solution), marker='o', color='b', markerfacecolor="w", markersize=5, linestyle='None' )
    plt.bar( np.array(range(0, max_time+1)), np.array(times) )
    plt.show()

# ().py simulation_type player_money master_money probability
if __name__ == "__main__":
    game = Game(player=20, master=INF, p=0.50)
    simulate13(game)
