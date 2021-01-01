'''
Orb Installer

Version Notes
    1.0
        First Commit
'''
from cmd import Cmd
import platform
import os
from sys import platform as sysPlatform

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
            + sysPlatform)

OrbInstaller().cmdloop()
