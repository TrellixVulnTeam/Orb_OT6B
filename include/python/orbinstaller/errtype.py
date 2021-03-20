'''
Orb 安装程序的错误类型
'''
__version__ = '1.0'
'''
Version Notes
    1.0
        First Commit
'''


class OrbInstallerBaseError(Exception):
    '''
    异常基类
    '''
    def __init__(self, msg='', /, repr='', code=''):
        self.msg = msg
        self.repr = repr
        self.code = code
        
class InitError(OrbInstallerBaseError):
    '''
    初始化失败
    '''
    def __init__(self):
        super(InitError, self).__init__()
    def __repr__(self):
        return repr

