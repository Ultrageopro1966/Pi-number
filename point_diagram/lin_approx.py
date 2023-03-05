import numpy as np
from matplotlib import pyplot as plt\


with open('pi.txt') as f:
    pi_num = f.read()[:500]

pi_num = list(map(int, list(pi_num)))

approx = np.polyfit(np.array([i for i in range(500)]), np.array(pi_num), 1)
f = np.poly1d(approx)
y = []
for k in [i for i in range(500)]:
    y.append(f(k))


plt.plot(np.array([i for i in range(500)]), np.array(pi_num), alpha=0.5)
plt.plot(np.array([i for i in range(500)]), y)


plt.show()
