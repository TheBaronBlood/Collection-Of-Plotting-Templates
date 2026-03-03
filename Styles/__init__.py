from pathlib import Path
import matplotlib as mpl

_styles_dir = Path(__file__).parent

# dark = str(_styles_dir / "mydark.mplstyle")
# light = str(_styles_dir / "mylight.mplstyle")

# Styles in matplotlib's Library registrieren
mpl.style.core.USER_LIBRARY_PATHS.append(str(_styles_dir))
mpl.style.core.reload_library()