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

def simulate13(game, sim_num = MAX_SIM, max_time = MAX_TIME):
    game_ = copy.deepcopy(game)
    times = [0] * (max_time+1)
    
    for i in range(0, sim_num):
        step_num = 0;
        
        for j in range(1, max_time+1):
            step_num += 1
            result = game_.step()
            if result != Going: break
            
        times[step_num] += 1;
        game_ = copy.deepcopy(game);
    
    plt.bar( np.array(range(0, max_time+1)), np.array(times) )
    plt.xlabel("step") ; plt.ylabel("frequency") ; plt.title("number of steps to bankrupt")
    plt.show()

# ().py simulation_type player_money master_money probability
if __name__ == "__main__":
    game = Game(player=20, master=INF, p=0.50)
    simulate13(game)
