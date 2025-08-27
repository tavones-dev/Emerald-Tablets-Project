# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['modern_emerald_tablets.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('throne_thoth.png', '.'),
        ('thoth.png', '.'),
        ('wallpaper_of_thoth.png', '.'),
        ('tablet_content.py', '.')
    ],
    hiddenimports=['PySide6.QtXml'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Emerald_Tablets_of_Thoth',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='throne_thoth.ico'
) 