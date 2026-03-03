import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig
import os
import Styles

plt.style.use("mydark")
color_cycle = plt.rcParams["axes.prop_cycle"].by_key()["color"]

fig, axs = plt.subplots(2, 1)


x = np.linspace(0,10,100)
y = np.sin(x)


axs[0].plot(x,y)
axs[1].plot(x,y)

axs[0].grid(True)
axs[1].grid(True)

plt.show()









