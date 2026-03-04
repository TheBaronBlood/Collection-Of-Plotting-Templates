from pathlib import Path
from matplotlib import style

_styles_dir = Path(__file__).parent

# dark = str(_styles_dir / "mydark.mplstyle")
# light = str(_styles_dir / "mylight.mplstyle")

# Styles in matplotlib's Library registrieren
style.core.USER_LIBRARY_PATHS.append(str(_styles_dir))
style.core.reload_library()