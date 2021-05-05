import socket
import time
from threading import Thread

from .scode import *
from .morclogger import *


class clientSocketConnectionPool():
    '''
    管理对客户端套接字的连接
    '''
    def __init__(self, timeout: int = 5, checkInterval: int = 60):
        self.timeout = timeout
        self.checkInterval = checkInterval

        self.connection = {}
    
    def push(self, target:str, conn) -> bool:
        if target in self.connection.keys():
            return False
        self.connection[target] = conn
        return True
    
    def pop(self, target:str):
        if self.testConnecting(target):
            self.connection[target].close()
        return self.connection.pop(target) if self.connection.get(target, None) else None
    
    def testConnecting(self, target:str) -> bool:
        try:
            self.connection[target].send(TEST_CONNECTION.encode("ascii"))
        except (TimeoutError, ConnectionAbortedError):
            return False
        else:
            return True
    
    def start(self):
        while True:
            for item in self.connection.items():
                pass
