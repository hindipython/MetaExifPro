import subprocess
import sys
import os

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Ensure PyInstaller is installed
try:
    import PyInstaller
except ImportError:
    print("Installing PyInstaller...")
    install("pyinstaller")

import PyInstaller.__main__

print("Starting Build Process with PyInstaller...")

# Define PyInstaller arguments
args = [
    'main.py',                       # Script to bundle
    '--name=MetaExifPro',            # Name of the executable
    '--icon=icon.ico',               # Application Icon
    '--onefile',                     # Create a single executable file
    '--noconsole',                   # No console window (GUI only)
    '--clean',                       # Clean cache before building
    
    # Collect all data/dependencies for critical libraries
    '--collect-all=customtkinter',   # Essential for CTk themes/fonts
    '--collect-all=mutagen',         # Essential for audio metadata
    '--collect-all=piexif',          # Essential for Exif handling
    '--collect-all=PIL',             # Pillow
    '--collect-all=pypdf',
    '--collect-all=docx',
    '--collect-all=openpyxl',
    
    '--distpath=dist',               # Output directory
    '--workpath=build',              # Temporary work directory
    '--noconfirm',                   # Do not ask for confirmation to overwrite
    
    # EXCLUDE HEAVY UNNEEDED LIBRARIES
    # This acts as a safety net if building from a "dirty" environment
    '--exclude-module=torch', 
    '--exclude-module=scipy', 
    '--exclude-module=pandas', 
    '--exclude-module=numpy', 
    '--exclude-module=matplotlib', 
    '--exclude-module=cv2',
    '--exclude-module=tensorflow',
    '--exclude-module=tkinter.test',
    '--exclude-module=unittest'
]

# Run PyInstaller
PyInstaller.__main__.run(args)

print("\n" + "="*50)
print(f"Build Success! File located at: {os.path.abspath('dist/MetaExifPro.exe')}")
print("="*50)
