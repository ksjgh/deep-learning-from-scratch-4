## P.165 무작위 정책에 따라 행동하는 에이전트
## RandomAgent class

import os, sys

# To check working directory check before path add
print()

# for importing the parent dirs
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from collections import defaultdict
import numpy as np
from common.gridworld import GridWorld

class RandomAgent:
    def __init__(self):
        self.gamma = 0.9
        self.action_size = 4

        ## !!! Random Policy
        random_actions = {0: 0.25, 1: 0.25, 2: 0.25, 3: 0.25}     
        self.pi = defaultdict(lambda: random_actions)
        self.V = defaultdict(lambda: 0)
        self.cnts = defaultdict(lambda: 0)
        self.memory = []

    def get_action(self, state):
        action_probs = self.pi[state]
        actions = list(action_probs.keys())
        probs = list(action_probs.values())
        return np.random.choice(actions, p=probs)

    ## save data to replay buffer
    def add(self, state, action, reward):
        data = (state, action, reward)
        self.memory.append(data)

    def reset(self):
        self.memory.clear()

    def eval(self):
        ## 이 예제는 에피소딕 시나리오 , 목표 상태의 가치는 0
        ## 거꾸로 Return 계산하기
        ## P.162 : G_C = R2 , G_B = R1 + gamma * G_C , G_A = R0 + gamma * G_B
        G = 0
        for data in reversed(self.memory):  # 역방향으로(reserved) 따라가기
            state, action, reward = data
            G = reward + self.gamma * G

            ## 몬테카를로 방식 , 증분 방식으로 Return G 갱신
            self.cnts[state] += 1
            self.V[state] += (G - self.V[state]) / self.cnts[state]

env = GridWorld()
agent = RandomAgent()

episodes = 1000
for episode in range(episodes):  # 에피소드 1000번 수행
    state = env.reset()
    agent.reset()

    while True:
        action = agent.get_action(state)             # 행동 선택
        next_state, reward, done = env.step(action)  # 행동 수행

        agent.add(state, action, reward)  # (상태, 행동, 보상) 저장
        if done:   # 목표에 도달 시
            agent.eval()  # 몬테카를로법으로 가치 함수 갱신
            break         # 다음 에피소드 시작

        state = next_state

# [그림 5-12] 몬테카를로법으로 얻은 가치 함수
env.render_v(agent.V)
