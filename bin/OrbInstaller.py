'''
Orb Installer

安装Orb Studio及其组件
'''
__version__ = '1.0.0r1'
'''
Version Notes
    1.0
        First Commit
'''
from include.python.orbinstaller import init
from include.python.orbinstaller.errtype import InitError
import shelve
from sys import platform as sysPlatform
from sys import argv, exit
from cmd import Cmd
import platform
import os

import colorama
#import rich

from orbinstaller import *
from orbinstaller.errtype import *
if not init():
    '''
    目前不会触发，现行错误直接抛出
    这里留用
    '''
    exit(1) # 初始化失败

# const
argv = argv[:]


class OrbInstaller(Cmd):
    prompt = '$'

    def do_help(self, line: str):
        if line:
            self.default(line)

    def default(self, line):
        self.stdout.write("Unknown Command: %s\n" % line)

    def preloop(self):
        print(
            "Orb Installer @"
            + "Microsoft Windows [Version "
            + ".".join(list(platform.win32_ver()[:-2]))
            + "]"
            + os.linesep
            + "Base on Python "
            + platform.python_version()
            + " ("
            + ", ".join(list(platform.python_build()))
            + ") ["
            + platform.python_compiler()
            + "] on "
            + sysPlatform
        )

    # built-in command
    def do_exit(self, line: str):
        try:
            line += 0
        except TypeError:
            exit()
        else:
            exit(line)

    def do_clear(self, line: str):
        os.system("clear")


OrbInstaller().cmdloop()
