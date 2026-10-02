from pathlib import Path

from PyInstaller.utils.hooks import collect_data_files


project_root = Path.cwd()
app_path = project_root / "app"


datas = [
    (
        str(app_path / "assets"),
        "assets",
    ),
]

datas += collect_data_files("PySide6")


a = Analysis(
    ["app/__main__.py"],
    pathex=[str(project_root)],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="JobHunter",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon=str(app_path / "assets" / "icon.ico"),
)