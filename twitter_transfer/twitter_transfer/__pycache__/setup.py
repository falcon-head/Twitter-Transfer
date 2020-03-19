"""
__foldername__ = twitter-transfer
__filename__ = setup.py
__author__ = Shrikrishna Joisa
__date_created__ = 19/03/2020
__date_last_modified__ =  20/03/2020
__python_version__ = 3.7.4 64-bit
__credits__ = []

"""

import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if __name__ == "__main__":
    package_list = ['scrapy', 'selenium', 'pandas']
    for i in package_list:
        install(i)