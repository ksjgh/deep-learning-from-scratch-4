## P.346
## off-policy , importance sampling , target policy(pi), behavior policy(b)

## def update(self): 살펴보기

import os, sys; sys.path.append(os.path.join(os.path.dirname(__file__), '..'))  # for importing the parent dirs
from collections import defaultdict
import numpy as np
from common.gridworld import GridWorld
from common.utils import greedy_probs


class McOffPolicyAgent:
    def __init__(self):
        self.gamma = 0.9
        self.epsilon = 0.1
        self.alpha = 0.2
        self.action_size = 4

        random_actions = {0: 0.25, 1: 0.25, 2: 0.25, 3: 0.25}
        self.pi = defaultdict(lambda: random_actions) ## 대상 정책 초기화
        self.b = defaultdict(lambda: random_actions) ## 행동 정책 초기화
        self.Q = defaultdict(lambda: 0)
        self.memory = []

    def get_action(self, state):
        action_probs = self.b[state] ### 행동 정책을 사용한다!!!
        actions = list(action_probs.keys())
        probs = list(action_probs.values())
        return np.random.choice(actions, p=probs)

    def add(self, state, action, reward):
        data = (state, action, reward)
        self.memory.append(data)

    def reset(self):
        self.memory.clear()

    def update(self):
        ## method = 1 : 책에서 나온 방법
        ## method = 2 : 내가 맞다고 생각하는 방법 , ## !!!! P.346 에 개념을 메모해놓았음
        method = 2

        if method == 1:
            G = 0
            rho = 1 ## 거꾸로 계산하기 , P.345

            for data in reversed(self.memory):
                state, action, reward = data
                key = (state, action)

                ## rho 사용
                ## P.342  식A.1, q_pi(s,a) = E_b[rho * G | s , a]
                G = self.gamma * rho * G + reward
                self.Q[key] += (G - self.Q[key]) * self.alpha
                rho *= self.pi[state][action] / self.b[state][action]

                ## epsilon=0 : 탐욕 정책
                self.pi[state] = greedy_probs(self.Q, state, epsilon=0)

                ## epsilon > 0 : epsilon-greedy
                self.b[state] = greedy_probs(self.Q, state, self.epsilon)

        ## !!!! P.346 에 개념을 메모해놓았음
        if method == 2:
            G_b = 0
            rho = 1 ## 거꾸로 계산하기 , P.345

            for data in reversed(self.memory):
                state, action, reward = data
                key = (state, action)
                
                G_b = reward + self.gamma * G_b
                rho *= self.pi[state][action] / self.b[state][action]
                G_pi = rho * G_b
                # G = self.gamma * rho * G + reward
                self.Q[key] += (G_pi - self.Q[key]) * self.alpha

                self.pi[state] = greedy_probs(self.Q, state, epsilon=0)
                self.b[state] = greedy_probs(self.Q, state, self.epsilon)


        if method == 3:
            ## method = 2 에서 pi 업데이트할 때 살짝 탐험적이게해보자

            G_b = 0
            rho = 1 ## 거꾸로 계산하기 , P.345

            for data in reversed(self.memory):
                state, action, reward = data
                key = (state, action)
                
                G_b = reward + self.gamma * G_b
                rho *= self.pi[state][action] / self.b[state][action]
                G_pi = rho * G_b
                # G = self.gamma * rho * G + reward
                self.Q[key] += (G_pi - self.Q[key]) * self.alpha

                ### !!!!!!!!!!!!!!!!!!!!!!!!!
                # self.pi[state] = greedy_probs(self.Q, state, epsilon=0)
                self.pi[state] = greedy_probs(self.Q, state, epsilon=self.epsilon * 0.2)

                self.b[state] = greedy_probs(self.Q, state, self.epsilon)



env = GridWorld()
agent = McOffPolicyAgent()

# episodes = 10000
episodes = 20000
for episode in range(episodes):
    state = env.reset()
    agent.reset()

    while True:
        action = agent.get_action(state)
        next_state, reward, done = env.step(action)

        agent.add(state, action, reward)
        if done:
            agent.update()
            break

        state = next_state

env.render_q(agent.Q)