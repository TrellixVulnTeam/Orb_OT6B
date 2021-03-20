"""
From CPython StdLib 2.7.15 user.py -> copy to Python 3.x

Version Notes
    2.1
        line:49: IOError -> FileNotFoundError
    2.0
        run `~/.pythonrc.py` as user.py runs
    1.1
        add warnings
    1.0
        Copy from python
"""
__version__ = "2.1"
__all__ = ["home", "pythonrc"]

import os
import runpy

try:
    import colorama
except ModuleNotFoundError:
    import sys
    print("Error:Import: run `pip3 install colorama` to get it", file=sys.stderr)

errorMsgForPythonrcFile = \
"""
Error:
    File:.pythonrc.py (from user.py)
    Warnings:
        Please make sure that your pythonrc.py is already always being right
"""

home = os.curdir
if "HOME" in os.environ:
    home = os.environ["HOME"]
elif os.name == "posix":
    home = os.path.expanduser("~/")
elif os.name == "nt":
    if "HOMEPATH" in os.environ:
        if "HOMEDRIVE" in os.environ:
            home = os.environ["HOMEDRIVE"] + os.environ["HOMEPATH"]
        else:
            home = os.environ["HOMEPATH"]

pythonrc = os.path.join(home, ".pythonrc.py")
try:
    fp = open(pythonrc, "rb")
except FileNotFoundError:
    pythonrc = None
else:
    try:
        runpy.read_code(fp)
    except BaseException:
        fp.close()
        print(
            colorama.Fore.RED
            + colorama.Back.BLUE
            + errorMsgForPythonrcFile
            + colorama.Fore.RESET
            + colorama.Back.RESET,
            end="\n\n\a",
        )
        raise
    else:
        fp.close()
        del fp
