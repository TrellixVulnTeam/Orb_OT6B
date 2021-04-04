'''
Orb 安装程序的综合文件库
'''
__version__ = '1.0'
'''
Version Notes
    1.0
        First Commit
'''
__DEBUG = False
__all__ = [
    'PATH'
]

import os
from sys import argv, exit
argv = argv[:]


from .errtype import *

ROOT_PATH = os.sep.join(__file__.split(os.sep)[:-4])
PATH = {
    'bin': os.path.join(ROOT_PATH, 'bin'),
    'include': os.path.join(ROOT_PATH, 'include'),
    'include/python': os.path.join(ROOT_PATH, os.path.join('include', 'python')),
    'opslib': os.path.join(ROOT_PATH, 'opslib'),
    'support':os.path.join(ROOT_PATH, 'support'),
    'etc': os.path.join(ROOT_PATH, 'etc')
}
PATH['root'] = ROOT_PATH
del ROOT_PATH
