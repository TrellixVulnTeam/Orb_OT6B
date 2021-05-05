'''
C -> . : command
Q -> ? : question
'''
__all__ = [
    'translateCode',
    'TEST_CONNECTION'
]


TEST_CONNECTION = b'#T:0001.#'


__scodeDict = {}
for item in __all__[1:]:
    __scodeDict[item] = eval(item)
def translateCode(code: str) -> str:
    for item in __scodeDict.keys():
        if __scodeDict[item] == code:
            return item

if __name__ == '__main__':
    for item in __scodeDict.items():
        print("%s | %s" % item)
