'''
ORB CORE 处理系统

Author: Zhuchen Zhong
'''
__version__ = '1.0.0'
'''
Version
    1.0.0
        First Commit
'''
__date__ = ''

from core import MORC
from sys import exit

morc = MORC()
morc.loop()
