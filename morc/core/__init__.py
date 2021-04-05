'''
ORB CORE 处理系统核心实现

Author: Zhuchen Zhong
'''
__version__ = '1.0.0'
'''
Version
    1.0.0
        First Commit
'''
__date__ = ''

# 服务端特殊码
# C=. 无需答复
# Q=? 需要答复
MORC_SCODE = {
    # 测试
    'TEST:IS_CONNECTED:Q' : "#T:ICD.#", # 是否连接
    'TEST:JUST_PASS:C' : "#T:JP.#", # 空信息

    # 请求
    'REQUEST:REQ_CONNECT:C' : "#R:RQT.#", # 请求连接
    'REQUEST:FLAG_USER:Q' : "#R:FGU?#", # 标记为一般用户

    # 命令
    'COMMAND:SEND_FLAGUSR:Q' : "#C:SFU.#", # 返回请求标记用户等级

    # 应答
    'REPLY:ACC_CONNECTION:C' : "#R:ACC.#", # 允许连接
    'REPLY:ALL_FGUSER' : "#R:AFU.#" # 允许标记为一般用户
}
def get_MORC_SCODE(item : str):
    return MORC_SCODE.get(item, MORC_SCODE.get('TEST:JUST_PASS:C'))

import socket
import time
from sys import exit
from threading import Thread


class ClientSocConn():
    def __init__(self) -> None:
        self.__pool = {}
    
    def push(self, item:str, nick:str, conn) -> bool:
        if not self.__pool.get(item, None):
            self.__pool[item] = []
            self.__pool[item][nick] = conn
            return True
        elif not self.__pool[item].get(nick, None):
            return False
        else:
            self.__pool[item][nick] = conn
            return True

    def get(self, item:str, nick:str):
        return self.__pool.get(item, {}).get(nick, None)
    
    def pop(self, item:str, nick:str) -> False:
        conn = self.get(item, nick)
        if not conn:
            return False
        del self.__pool[item][nick]
        return True

    def get_tmp(self):
        return self.__pool.get('TMP', None)

class MORC():
    '''
    核心服务器
    '''
    def __init__(self, hostname:str = '127.0.0.1', port:int = 52004, MAX_BYTES:int = 65535, MAX_LISTEN:int = 100) -> None:
        su = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        su.bind((hostname, port))
        self.coreUDPConnection = su
        self.MAX_BYTES = MAX_BYTES

        sc = socket.socket()
        sc.bind((hostname, 52005))
        sc.listen(100)
        self.coreSocketConnection = sc

        # 客户端连接池
        self.cliSocConn = ClientSocConn()
    
    def loop(self):
        print("Listening at {}".format(self.coreUDPConnection.getsockname()))
        self.tmpSock = {}

        TR_ACCEPT_SCOK_CONN = Thread(target=self.accepSocketConn, daemon=True)
        TR_ACCEPT_SCOK_CONN.start()
        TR_CONFIRM_SOCK_CONN = Thread(target=self.confirmSockConn, daemon=True)
        TR_CONFIRM_SOCK_CONN.start()

        while True:
            data, addr = self.coreUDPConnection.recvfrom(self.MAX_BYTES)
            if data.decode('ascii') == get_MORC_SCODE('REQUEST:REQ_CONNECT:C'):
                if addr in self.tmpSock.items():
                    self.cliSocConn.push('TMP','addr', self.tmpSock[addr])
                    self.coreUDPConnection.sendto(get_MORC_SCODE('REPLY:ACC_CONNECTION:C'.encode('ascii'), addr))

    def confirmSockConn(self):
        def waitReply(conn, addr):
            conn.sendall(get_MORC_SCODE('COMMAND:SEND_FLAGUSR:Q').encode('ascii'))
            if conn.recv(1024).decode('ascii') == get_MORC_SCODE('REQUEST:FLAG_USER:Q'):
                conn.sendall(get_MORC_SCODE('REPLY:ALL_FGUSER').encode('ascii'))
                self.cliSocConn.pop('TMP', addr)
                self.cliSocConn.push('USER', conn)

        while True:
            for conn in [(self.cliSocConn.get('TMP', addr), addr) for addr in (self.cliSocConn.get_tmp() or [])]:
                t = Thread(target=waitReply, args=conn, daemon=True)
                t.start()
                t.join(3)
    
    def accepSocketConn(self):
        while True:
            c, addr = self.coreSocketConnection.accept()
            if not self.isConnected(c):
                continue
            
            if not self.tmpSock.get(addr, None):
                self.tmpSock[addr] = c
    
    def isConnected(self, conn) -> bool:
        try:
            conn.sendall(get_MORC_SCODE('TEST:IS_CONNECTED:Q').encode('ascii'))
        except ConnectionAbortedError:
            return False
        else:
            return True

