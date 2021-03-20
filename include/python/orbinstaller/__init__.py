'''
Orb 安装程序的综合文件库
'''
__version__ = '1.0'
'''
Version Notes
    1.0
        First Commit
'''
__all__ = [
    'PATH',
    'raiseError',
    'init'
]

import os
import shelve
import time
from copy import deepcopy as copy
from sys import argv, exit
argv = argv[:]

import colorama

from .errtype import *

__DEBUG = False

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
configure = {}
TMP = {}


# tools
def mkdir(name: str) -> bool:
    if os.path.isdir(name):
        return True
    try:
        os.mkdir(name)
    except:
        return False
    else:
        return True

def raiseError(err: object, msg: str) -> None:
    '''输出异常
    :param err(str): 异常类
    :param msg(str): 异常消息

    :return(None)
    '''
    try:
        colorama.init()
    except NameError:  # rich version
        pass
    else:  # colorama version
        raise err(
            colorama.Fore.RED + colorama.Back.YELLOW +\
                msg,
            colorama.Fore.RESET + colorama.Back.RESET
        )


# function
def set_mConfigure(key: str, fields: str = None, /, updateOnceWrite = True):
    '''对主配置文件进行读写
    :param key(str): 键
    :param fields(str): 字段
    :param updateOnceWrite: 写入后立即更新
    '''
    pass

def get_mConfigure(key: str = '', /,useCache: bool = False, updateCache: bool = False):
    '''获取主配置文件信息
    :param key(str): 键
    :param useCache(bool): 使用缓存
    :param updateCache(bool): 若为真，其他动作自动失效，只更新缓存

    :return(anyType)
    '''
    pass


def init() -> bool:
    '''执行初始化操作
    :return(bool)
    '''
    if not mkdir(PATH['etc']):
        raiseError(InitError, 'Fail to creat folder `%s`' % PATH['etc'])
        return False
    TMP['mConfigure_filename'] = os.path.join(PATH['etc'], 'configure')
    
    return True


# test
if __DEBUG:
    from pprint import pprint
    print("PATH:")
    pprint(PATH)
