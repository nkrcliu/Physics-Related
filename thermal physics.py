import math
import numpy as np
import matplotlib.pyplot as plt

def g(N, q):
    N_fac = math.factorial(N)
    q_fac = math.factorial(q)
    Nq_fac = math.factorial(N-q)
    result = N_fac/(q_fac*Nq_fac)
    return result

N = 100
result = []
num = range(0, 81)
gt = []

for i in num:
    subresult=[]
    qa = i
    qb = 80-i
    ga = g(N, qa)
    gb = g(N, qb)
    gtotal = ga * gb
    subresult.append(qa)
    subresult.append(ga)
    subresult.append(qb)
    subresult.append(gb)
    subresult.append(gtotal)
    gt.append(gtotal)
    result.append(subresult)

np.savetxt('result.csv', result, delimiter=',')
plt.plot(num, gt)
plt.title('Distribution of States')
plt.xlabel('qa')
plt.ylabel('quantity')
plt.show()