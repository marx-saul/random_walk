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
    

# plot the transition of the money player has
def simulate1(game, max_time = MAX_SIM, flag = False):
    trans = [game.player] ; step_num = max_time
    
    for i in range(0, max_time):
       result = game.step()
       
       # process
       #print(game.player)
       trans.append(game.player)
       #print(game.player)
       
       if (result != Going): step_num = i+1; break
    
    if flag:
        plt.plot( np.array(range(0, step_num+1)), np.array(trans) )
        plt.xlabel("step") ; plt.ylabel("player's money") ; plt.title("random walk")
        plt.show()
    
    return len(trans)-1
    

def simulate2(game, sim_num = MAX_SIM, max_time = MAX_TIME):
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
    args = sys.argv
    sim_type = 1; pm = 20; mm = INF; pr = 0.50
    
    if len(args) >= 5:
        sim_type = int(args[1])
        pm = int(args[2])
        if args[3] == 'INF' or args[3] == 'inf':
            mm = INF
        else:
            mm = int(args[3])
        pr = float(args[4])
    
    if len(args) == 4:
        sim_type = int(args[1])
        pm = int(args[2])
        if args[3] == 'INF' or args[3] == 'inf':
            mm = INF
        else:
            mm = int(args[3])
            
    if len(args) == 3:
        sim_type = int(args[1])
        pm = int(args[2])
    
    if len(args) == 2:
        sim_type = int(args[1])
    
    game = Game(player=pm, master=mm, p=pr)
    #time = simulate1(game, flag=True)
    #print("time = ", time)
    if sim_type == 1: simulate1(game, flag=True)
    else: simulate2(game)
