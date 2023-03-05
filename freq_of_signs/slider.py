import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import matplotlib.ticker as ticker

with open('pi.txt') as file:
    pi_num = file.read()[:5000]


def num_of(num):
    global pi_num
    a = []
    for k in range(10):
        a.append(pi_num[:num].count(str(k)))
    return a


init_num = 100
y = num_of(init_num)

fig, ax = plt.subplots()
line = ax.bar([i for i in range(10)], num_of(init_num))

fig.subplots_adjust(left=0.25, bottom=0.25)

axfreq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
num_slider = Slider(
    ax=axfreq,
    label='Символы после запятой',
    valmin=1,
    valmax=5000,
    valinit=init_num,
    valstep=1
)

def update(val):
    global line
    line.remove()
    line = ax.bar([i for i in range(10)], num_of(num_slider.val))


num_slider.on_changed(update)
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
plt.show()
