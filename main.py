import matplotlib.pyplot as plt
import numpy as np
import random

INF = -1
Going = 0;
PlayerLose = 1
MasterLose = 2

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
    

def simulate(game, max_time = 100000):
    trans = [game.player] ; step_num = max_time
    
    for i in range(0, max_time):
       result = game.step()
       
       # process
       #print(game.player)
       trans.append(game.player)
       #print(game.player)
       
       if (result != Going): step_num = i+1; break
       
    plt.plot(np.array(range(0, step_num+1)), np.array(trans))
    plt.xlabel("step") ; plt.ylabel("player's money") ; plt.title("random walk")
    plt.show()
    
    return trans
    

if __name__ == "__main__":
    game = Game(player=20, master=80, p=0.50)
    trans = simulate(game)
    print("time = ", len(trans))
