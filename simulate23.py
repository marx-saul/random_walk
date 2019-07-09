import matplotlib.pyplot as plt
import numpy as np
import random
import copy
import sys

INF = -1
Going = 0
PlayerLose = 1
MasterLose = 2
MAX_TIME = 10000
MAX_SIM  = 1000

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
    

def simulate23(game, trial_num = MAX_SIM):
    player_lose = [0] * (MAX_TIME+1);
    master_lose = [0] * (MAX_TIME+1);
    player_time = 0
    master_time = 0
    draw = 0
    
    for n in range(0, trial_num):
        draw_flag = True
        game_ = copy.deepcopy(game)
        
        for i in range(0, MAX_TIME+1):
            result = game_.step()
            if result == PlayerLose:
                player_lose[i] += 1
                player_time += 1
                draw_flag = False
                break
            elif result == MasterLose:
                master_lose[i] += 1
                master_time += 1
                draw_flag = False
                break
        
        if draw_flag: draw += 1
        
    
    print("player bunkrupt: ", player_time, ", master bunkrupt: ", master_time, ', draw: ', draw)
    
    """plt.bar( np.array(range(0, MAX_TIME+1)), np.array(player_lose) )
    plt.xlabel('steps before player bankrupt'); plt.ylabel('times')
    plt.show()
    
    plt.bar( np.array(range(0, MAX_TIME+1)), np.array(master_lose) )
    plt.xlabel('steps before master bankrupt'); plt.ylabel('times')
    plt.show()"""
    
    
# ().py simulation_type player_money master_money probability
if __name__ == "__main__":
    game = Game(player=20, master=80, p=0.49)
    simulate23(game)
