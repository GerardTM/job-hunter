class ThemeColors:
    def __init__(
        self,
        background: str,
        surface: str,
        border: str,
        border_strong: str,
        text_primary: str,
        text_secondary: str,
        text_muted: str,
        text_subtle: str,
        brand_surface: str,
        brand_surface_hover: str,
    ):
        self.BACKGROUND = background
        self.SURFACE = surface
        self.BORDER = border
        self.BORDER_STRONG = border_strong
        self.TEXT_PRIMARY = text_primary
        self.TEXT_SECONDARY = text_secondary
        self.TEXT_MUTED = text_muted
        self.TEXT_SUBTLE = text_subtle
        self.BRAND_SURFACE = brand_surface
        self.BRAND_SURFACE_HOVER = brand_surface_hover

    BRAND_500 = "#f43f5e"
    BRAND_600 = "#e11d48"
    BRAND_700 = "#be123c"


LIGHT = ThemeColors(
    background="#f8fafc",
    surface="#ffffff",
    border="#e2e8f0",
    border_strong="#cbd5e1",
    text_primary="#0f172a",
    text_secondary="#475569",
    text_muted="#64748b",
    text_subtle="#94a3b8",
    brand_surface="#ffe4e6",
    brand_surface_hover="#fff1f2",
)


DARK = ThemeColors(
    background="#0f172a",
    surface="#1e293b",
    border="#334155",
    border_strong="#475569",
    text_primary="#f8fafc",
    text_secondary="#cbd5e1",
    text_muted="#94a3b8",
    text_subtle="#64748b",
    brand_surface="#4c0519",
    brand_surface_hover="#881337",
)

_current_theme = LIGHT


def set_theme(dark: bool) -> None:
    global _current_theme
    _current_theme = DARK if dark else LIGHT


def get_colors() -> ThemeColors:
    return _current_theme