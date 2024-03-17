import numpy as np

x = np.array([1, 2, 3])         # 확률 변수
pi = np.array([0.1, 0.1, 0.8])  # 확률 분포

# =========== 기댓값의 참값 계산 ==================
e = np.sum(x * pi)
print('참값(E_pi[x]):', e)

# =========== 몬테카를로법으로 계산 ==================
n = 100  # 샘플 개수
samples = []
for _ in range(n):
    # pi를 이용한 샘플링, !!! 실험을 통해서 얻기 때문에 여기서 pi 은 알지 못하는 상태임
    s = np.random.choice(x, p=pi)  
    samples.append(s)

mean = np.mean(samples)  # 샘플들의 평균
var = np.var(samples)    # 샘플들의 분산
print('몬테카를로법: {:.2f} (분산: {:.2f})'.format(np.mean(samples), np.var(samples)))

# =========== 중요도 샘플링으로 계산 ===========
b = np.array([1/3, 1/3, 1/3])  # 첫 번째 실험 : 확률 분포가 서로 매우 다를 때 분산 커짐
# b = np.array([0.2, 0.2, 0.6]) # 두 번째 개선 : 확률 분포가 유사해지면 분산 줄어듬 (P.167)

samples = []
for _ in range(n):
    idx = np.arange(len(b))         # b의 인덱스([0, 1, 2])
    i = np.random.choice(idx, p=b)  # b를 사용하여 샘플링
    s = x[i]
    rho = pi[i] / b[i]              # 가중치
    samples.append(rho * s)         # 샘플 데이터에 가중치를 곱해 저장
    
mean = np.mean(samples)
var = np.var(samples)
print('중요도 샘플링: {:.2f} (분산: {:.2f})'.format(np.mean(samples), np.var(samples)))
