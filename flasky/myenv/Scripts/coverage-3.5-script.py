#!e:\python\web\myenv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'coverage==3.7.1','console_scripts','coverage-3.5'
__requires__ = 'coverage==3.7.1'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('coverage==3.7.1', 'console_scripts', 'coverage-3.5')()
    )
