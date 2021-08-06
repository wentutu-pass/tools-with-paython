from xeger import Xeger

_x = Xeger()
for i in range(20):
    testStr = _x.xeger(r'^[a-z_]+(\.[a-z_][a-z0-9_]*)*$')
    print(testStr)
    i += 1
