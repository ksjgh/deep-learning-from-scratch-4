import numpy as np
import matplotlib.pyplot as plt
from bandit import Agent

N_ARMS = 10
class NonStatBandit: # non-stationary
    def __init__(self, arms=N_ARMS):
        self.arms = N_ARMS
        self.rates = np.random.rand(arms)

    def play(self, arm):
        rate = self.rates[arm]

        ## add noise to all arms , non-stationary effect
        self.rates += 0.1 * np.random.randn(self.arms)
        if rate > np.random.rand():
            return 1
        else:
            return 0
        

class AlphaAgent:
    def __init__(self, epsilon, alpha, actions=N_ARMS):
        self.epsilon = epsilon
        self.Qs = np.zeros(actions)
        self.alpha = alpha # fixed alpha

    def update(self, action ,reward):
        # update with alpha
        self.Qs[action] += self.alpha * ( reward - self.Qs[action] ) # [eq 1.6]

    def get_action(self):
        if np.random.rand() < self.epsilon:
            return np.random.randint(0, len(self.Qs))
        return np.argmax(self.Qs)
    

runs = 200
steps = 1000
epsilon = 0.1
alpha = 0.8
agent_types = ['sample average','alpha const update']
results = {}

for agent_type in agent_types:
    all_rates = np.zeros((runs, steps)) # (200, 1000)

    for run in range(runs):
        if agent_type == 'sample average':
            agent = Agent(epsilon)
        else:
            agent = AlphaAgent(epsilon, alpha)

        bandit = NonStatBandit()
        total_reward = 0
        rates = []

        for step in range(steps):
            action = agent.get_action()
            reward = bandit.play(action)
            agent.update(action, reward)
            total_reward += reward
            rates.append(total_reward/(step + 1))

        all_rates[run] = rates
        
    avg_rates = np.average(all_rates, axis=0)
    results[agent_type] = avg_rates

# [그림 1-20] 표본 평균과 고정값 α에 의한 갱신 비교
plt.figure()
plt.ylabel('Average Rates')
plt.xlabel('Steps')
for key, avg_rates in results.items():
    plt.plot(avg_rates, label=key)
plt.legend()
plt.show()
