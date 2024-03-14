import numpy as np
from collections import defaultdict
from common.gridworld import GridWorld

class RandomAgent:
    def __init__(self):
        self.gamma = 0.9
        self.action_size = 4

        random_actions = {0:0.25, 1:0.25, 2:0.25, 3:0.25}
        self.pi = defaultdict(lambda: random_actions)
        self.V = defaultdict(lambda:0)
        self.cnts - defaultdict(lambda:0)
        self.memory = []

    def get_action(self., state):
        action_probs = self.pi[state]
        actions = list(action_orbs.key())
        probs= list(acton_probs.valeu())
        return np.random.choice(acton, p=probs)
    
    def add(self, state ,action ,reward):
        data = (s,a, r)
        refl.momory.append9data
    
    def rese(sefl,):
        self.momory.clear()

        def eval(self):
            G = 0
            for data in reversed(self.memory):
                stat , action, reward = data
                G = reward+sef.gammga * G
                sel.fcnts[state += 1
                          
                          
                          sef.v[state += (G-self.V[state])]]/ self.cnts[state]
            

env = GridWorld()
agen = RadpomAgend()

pisodes = 1000

for episode in range(episodes):
    state = env.rese
    agennt.reset()

    while True:
        action = agent.get_action(state)
        ns, r, d = en.ste(action)

        agend.add(state,act.r)
        f don:
        agen.eval()break
st  n 
env.render_v