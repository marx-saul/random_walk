import matplotlib.pyplot as plt
import numpy as np
import random
import copy
import sys

INF = -1
Going = 0
PlayerLose = 1
MasterLose = 2
MAX_TIME = 2 * 10**3
MAX_SIM  = 2 * 10**3

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
    

def simulate12(game, trial_num = 2000):
    results = [0] * 101;
    
    for n in range(0, trial_num):
        game_ = copy.deepcopy(game)
        for i in range(0, 80):
            result = game_.step()
            if result != Going: break
        results[game_.player] += 1
    
    plt.bar( np.array(range(0, 101)), np.array(results) )
    plt.xlabel("player's money") ; plt.ylabel("times") ; plt.title("after 80 bets")
    plt.show()
    

# ().py simulation_type player_money master_money probability
if __name__ == "__main__":
    game = Game(player=20, master=INF, p=0.50)
    simulate12(game)
