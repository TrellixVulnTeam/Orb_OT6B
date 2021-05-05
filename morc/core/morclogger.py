'''
日志记录模块
'''
__author__ = 'Zhuchen Zhong'
__version__ = '1.0.0'
'''
Version
    1.0.0
        First Commit
'''
__all__ = ["morclogger", "MORCLOGGER_LEVEL_DEBUG", "MORCLOGGER_LEVEL_INFO"]

import time

class vfilestream():
    def __init__(self, vfilename: str = None, encoding:str = 'utf-8', buffering:int = -1, savemode:str = 'a'):
        self.vfilename = vfilename
        self.encoding = encoding
        self.buffering = buffering if buffering > 0 else 16
        self.savemode = savemode

        self.flagClosed = False
        self.buffer = ''
        self.data = ''

    def bwrite(self, rdata: str) -> int:
        count = 0
        while rdata:
            while len(self.buffer) >= self.buffering:
                self.data += self.buffer[0]
                self.buffer = self.buffer[1:]
            self.buffer += rdata[0]
            rdata = rdata[1:]
            count += 1
        return count
    
    def write(self, rdata) -> int:
        if self.flagClosed:
            return
        return self.bwrite(rdata)
    
    def writelines(self, rdata) -> int:
        if self.flagClosed:
            return
        return self.bwrite(''.join([r for r in rdata]))
    
    def close(self):
        self.flush()
        self.flagClosed = True

    def flush(self):
        while self.buffer:
            self.data += self.buffer[0]
            self.buffer = self.buffer[1:]
    
    def closed(self) -> bool:
        return self.flagClosed

    def save(self) -> bool:
        self.flush()
        try:
            fp = open(self.vfilename, mode=self.savemode, encoding=self.encoding)
            fp.write(self.data)
        except (IOError, PermissionError):
            return False
        else:
            return True

MORCLOGGER_LEVEL_INFO = 'INFO'
MORCLOGGER_LEVEL_DEBUG = 'DEBUG'
class morclogger():
    def __init__(self, filename:str, mode:str = 'a', virtual:bool = False, encoding:str = 'utf-8', buffering:int = -1, level:int = MORCLOGGER_LEVEL_INFO):
        if virtual:
            self.stream = vfilestream(filename, encoding, buffering, mode)
        else:
            self.stream = open(filename, mode, encoding=encoding, buffering=buffering)
        self.virtual = virtual

        self.level = level
        self.encoding = encoding
    
    def log(self, msg:str) -> int:
        return self.stream.write(
            '\n{}:{}:{}'.format(time.asctime(), self.level, msg)
        )
    
    def save(self):
        self.stream.flush()
    
    def close(self):
        self.stream.close()
    
    def savelocal(self) -> bool:
        if not self.virtual:
            return
        return self.stream.save()

    
    def closed(self) -> bool:
        return self.stream.close()

