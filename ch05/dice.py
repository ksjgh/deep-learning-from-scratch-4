import numpy as np

def sample(dices=2):
    sum = 0
    for _ in range(dices):
        x = np.random.choice([1,2,3,4,5,6])
        sum += x

    return sum

trial = 1000
running_ave = 0

for n in range(trial):
    x = sample(dices=2)
    running_ave += (x-running_ave)/(n+1)
    print(running_ave)




# def sample(dices=2):
#     x = 0
#     for _ in range(dices):
#         x += np.random.choice([1, 2, 3, 4, 5, 6])
#     return x


# trial = 1000
# V, n = 0, 0

# for _ in range(trial):
#     s = sample()
#     n += 1
#     V += (s - V) / n
#     print(V)
