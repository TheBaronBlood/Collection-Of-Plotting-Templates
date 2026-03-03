import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.pyplot import savefig
import os
import Styles

plt.style.use("mydark")


F = np.array([0, 0.5, 1, 2, 3, 4])
s1 = np.array([0, 0.8, 1.5, 2.9, 4.4, 5.8])
s2 = np.array([0, 0.4, 0.8, 1.6, 2.8, 3.6])

I = np.array([0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1,0.06,0.02])
I_smooth = np.linspace(I.min(), I.max(), 300)
t = np.array([1.8,3.4,5.0,7.2,9.9,13.2,18.1,26.5,32.5,45.5])

s1_fit = np.polyfit(F,s1, 1)
s2_fit = np.polyfit(F,s2, 1)
t_fit = np.polyfit(I,t,2)


p1 = np.poly1d(s1_fit)
p2 = np.poly1d(s2_fit)

p3 = np.poly1d(t_fit)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,4))

# Plot Daten
ax1.plot(F, p1(F), "-")
ax1.plot(F, s1, "o", label="Messwerte", color="#e6414a")

ax1.plot(F, p2(F), "-")
ax1.plot(F, s2, "o", label="Messwerte", color="#f18927")

ax2.plot(I, t, "o-", label="Messwerte", color="#ffc12d")
#ax2.plot(I, p3(I), "-", label="Messwerte", color="#ffc12d")
#ax2.plot(I_smooth, p3(I_smooth), "-", color="#ffc12d")

# x-Ticks auf beiden Achsen bei jedem 1er Schritt
ax1.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))


ax2.xaxis.set_major_locator(ticker.MultipleLocator(0.1))

# Optional: Achsentitel und Legende
ax1.set_xlabel("Kraft (N)")
ax1.set_ylabel("Strecke (cm)")
ax1.legend()

ax2.set_xlabel("Unsicherheit")
ax2.set_ylabel("t-Wert")
ax2.legend()

plt.tight_layout()


plt.show()

# from pathlib import Path
# name = os.path.basename(__file__).split(".")[0]
# preview_dir = Path(__file__).parents[2] / "Styles" / "preview"
# preview_dir.mkdir(parents=True, exist_ok=True)
# fig.savefig(preview_dir / f"{name}_dark.png")