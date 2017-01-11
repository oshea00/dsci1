import ctypes

# gcc -shared -o flipfunc.so flipfunc.c

flipslib = ctypes.cdll.LoadLibrary('/Users/moshea/repos/flips/flipfunc.so')
flipslib.f.restype = ctypes.c_double

hist = (ctypes.c_int*1000)()
headsInARow = ctypes.c_int32(0)
flips = ctypes.c_int32(100000)
odds = flipslib.f(flips, ctypes.byref(headsInARow), ctypes.byref(hist))

print("Probability of heads: {}".format(odds))
print("Longest run of heads: {}".format(headsInARow.value))
h = [(i,c) for i,c in enumerate(hist) if c > 0]
print(sorted(h, key=lambda(r, c): r, reverse=True))


