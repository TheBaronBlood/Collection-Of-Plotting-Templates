import numpy as np
import matplotlib.pyplot as plt
import os
import Styles

# ── Theme ────────────────────────────────────────────────────────────────────
# Lädt das Style-File aus dem Styles-Package
# Verfügbare Styles: "mylight", "mydark"
plt.style.use("mylight")

# Zugriff auf die Farben des aktuellen Color-Cycles
# Verwendung: colors[0], colors[1], colors[2], ...
colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]

# ── Figure & Axes ─────────────────────────────────────────────────────────────
# figsize=(Breite, Höhe) in Zoll
# Ein Subplot:      fig, ax = plt.subplots()
# Mehrere Subplots: fig, (ax1, ax2) = plt.subplots(1, 2)  ← nebeneinander
#                   fig, (ax1, ax2) = plt.subplots(2, 1)  ← übereinander
fig, ax = plt.subplots(figsize=(10, 6))

# ── Daten ────────────────────────────────────────────────────────────────────
# np.linspace(start, stop, anzahl_punkte) → gleichmäßig verteilte Werte
# np.array([1, 2, 3, ...])               → eigene Werte als Array
x = np.linspace(-5, 5, 100)
y = x**2

# ── Plot ─────────────────────────────────────────────────────────────────────
# marker:    "o" Kreis | "s" Quadrat | "^" Dreieck | "" kein Marker
# linestyle: "-" Linie | "--" gestrichelt | ":" gepunktet | "" keine Linie
# zorder:    höhere Zahl = weiter vorne (Überlappungsreihenfolge)
# label:     Text für die Legende, LaTeX mit r"$...$" möglich
ax.plot(x, y,
        linestyle="-",
        marker="",
        color=colors[0],
        zorder=1,
        label=r"$f(x) = x^2$")

# ── Scatter / Einzelpunkte ───────────────────────────────────────────────────
# Für einzelne Punkte oder Messwerte ohne Linie
# ax.scatter(x_werte, y_werte,
#            color=colors[1],
#            zorder=2,          # über dem Plot zeichnen
#            label="Messpunkte")

# ── Annotation / Beschriftung mit Pfeil ──────────────────────────────────────
# xy:        Koordinate der Pfeilspitze
# xytext:    Koordinate des Textes
# ha:        horizontale Ausrichtung ("center", "left", "right")
# arrowprops: Aussehen des Pfeils
ax.annotate("Label",
            xy=(0, 0),
            xytext=(0, 3),
            ha="center",
            fontsize=12,
            color=colors[1],
            arrowprops=dict(
                color=colors[1],
                arrowstyle="->",   # "->" | "-|>" | "fancy"
                linewidth=1.5
            ))

# ── Achsenbeschriftung & Titel ───────────────────────────────────────────────
# LaTeX-Symbole mit r"$...$" möglich, z.B. r"$\Omega$", r"$\mu$"
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Titel")

# ── Ticks (optional) ─────────────────────────────────────────────────────────
# Feste Tick-Werte setzen
# ax.set_xticks([...])
# ax.set_yticks([...])

# Automatischer Tick-Abstand, z.B. alle 1 Einheit
# from matplotlib import ticker
# ax.xaxis.set_major_locator(ticker.MultipleLocator(1))

# ── Achsenlimits (optional) ──────────────────────────────────────────────────
# ax.set_xlim(0, 10)
# ax.set_ylim(0, 100)

# ── Legende & Layout ─────────────────────────────────────────────────────────
# loc: "best" | "upper right" | "lower left" | "center" | ...
ax.legend(loc="best")

# tight_layout() passt Abstände automatisch an → verhindert abgeschnittene Labels
fig.tight_layout()

# ── Speichern (optional) ─────────────────────────────────────────────────────
# Dateiname wird automatisch vom Script-Namen abgeleitet
# from pathlib import Path
# name = os.path.basename(__file__).split(".")[0]
# preview_dir = Path(__file__).parents[2] / "Styles" / "preview"
# preview_dir.mkdir(parents=True, exist_ok=True)
# fig.savefig(f"Output/{name}.pdf")   # PDF
# fig.savefig(f"Output/{name}.png")   # PNG


from pathlib import Path
name = os.path.basename(__file__).split(".")[0]
preview_dir = Path(__file__).parents[1] / "Styles" / "preview"
preview_dir.mkdir(parents=True, exist_ok=True)
fig.savefig(preview_dir / f"{name}_dark.png")
