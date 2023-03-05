from matplotlib import pyplot as plt

with open('pi.txt') as f:
    pi_num = str(f.read())[:1000]
y = list(map(int, list(pi_num)))

x = []
for k in range(1000):
    x.append(k)

plt.scatter(x, y, s=5, alpha=0.8)
plt.plot(x, y, alpha=0.4, c='red', linewidth=0.5)
plt.show()
