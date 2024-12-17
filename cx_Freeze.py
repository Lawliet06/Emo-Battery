import sys
from cx_Freeze import setup, Executable

# Replace "your_script.py" with the actual filename of your script
script = "BatterySaver.py"

# Replace "images" with the path to your images folder
images_folder = "img"

options = {
    'build_exe': {
        'includes': [],
        'include_files': [(images_folder, images_folder)],
        'excludes': [],
    },
}

executables = [Executable(script)]

setup(name='EmoBattery',
      version='1.0',
      description='Battery life notifier for battery saving',
      options=options,
      executables=executables)

