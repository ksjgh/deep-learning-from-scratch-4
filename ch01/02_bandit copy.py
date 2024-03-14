import numpy as np
import matplotlib.pyplot as plt

N_ARMS = 10

class Bandit:
    def __init__(self,arms=N_ARMS):
        self.win_rates = np.random.rand(arms)
        
    def play(self, arm):
        win_rate = self.win_rates[arm]

        if win_rate > np.random.rand():
            return 1
        else:
            return 0
        
class Agent:
    def __init__(self, epsilon, action_size=N_ARMS):
        self.epsilon = epsilon # epsilon-greedy
        self.Qs = np.zeros(action_size) # value of each arm
        self.ns = np.zeros(action_size) # play number of each arm

    def update(self, action, reward):
        self.ns[action] += 1
        self.Qs[action] += (reward - self.Qs[action]) / self.ns[action]

    def get_action(self):
        if np.random.rand() < self.epsilon:
            return np.random.randint(0, len(self.Qs)) # random action
        else:
            return np.argmax(self.Qs) # greedy action
        
if __name__ == '__main__':
    steps = 1000
    epsilon = 0.1

    bandit = Bandit()
    agent = Agent(epsilon)
    total_reward = 0
    total_rewards = []
    win_rates = []

    for step in range(steps):
        action = agent.get_action()
        reward = bandit.play(action)
        agent.update(action, reward)
        total_reward += reward

        total_rewards.append(total_reward)
        win_rates.append(total_reward / (step + 1))

    print(total_reward)

    # [그림 1-12] 단계별 보상 총합
    plt.ylabel("Total reward")
    plt.xlabel("step")
    plt.plot(total_rewards)
    plt.show()

    # [그림 1-13] 단계별 승률
    plt.ylabel("Rates")
    plt.xlabel("steps")
    plt.plot(win_rates)
    plt.show()


     