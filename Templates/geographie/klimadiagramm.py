import matplotlib.pyplot as plt 
import matplotlib.ticker as ticker
import numpy as np
import Styles


plt.style.use("mylight")
color_cycle = plt.rcParams["axes.prop_cycle"].by_key()["color"]


months = ["Jan","Feb","Mar","Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dez"]

temp_mid = np.array([2.2,7.5,8.2,11.6,17.1,17.9,20,21.4,17.4,11.9,6.1,4.2])
nn = np.array([41.4,56.9,22.3,23.1,68.5,50.4,71.6,15,16,23,32.9,36.8])




fig, ax1 = plt.subplots()

color = color_cycle[0]
ax1.set_xlabel("Monate")
ax1.set_ylabel('Temp in °C', color=color)
ax1.plot(months, temp_mid, color=color, zorder=3)
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylim(round(np.min(temp_mid)-10), round(np.max(temp_mid)+10*2))
ax1.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax1.set_title(r"$$\textbf{Deutschland }\text{(München)}$$", loc="left", pad=10)

ax2 = ax1.twinx()
color = color_cycle[5]
ax2.set_ylabel('Niederschlag in NN', color=color)
y1_min, y1_max = ax1.get_ylim()
ax2.set_ylim(y1_min*2, y1_max*2)
ax2.plot(months, nn, color=color, zorder=0)
ax2.tick_params(axis='y', labelcolor=color)


ax2.fill_between(months, nn, temp_mid*2, where=nn<temp_mid*2, interpolate=True, facecolor='none', edgecolor=color_cycle[2], alpha=0.7, hatch='//',zorder=-2)


fig.tight_layout()
plt.show()
