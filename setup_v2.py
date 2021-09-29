from setuptools import setup

DATA_FILES = []
APP = ['app_v2.py']
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'CFBundleShortVersionString': '1.0.0',
        'LSUIElement': True,
    },
    'packages': ['rumps','os','threading']
}

setup(
    app=APP,
    name='netStatus',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'], install_requires=['rumps','requests']
)