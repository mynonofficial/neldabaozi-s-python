import time, functools

def metric(fn):
    @functools.wraps(fn)
    def executime(*args):
        time_start = time.time()
        fn(*args)
        time_end = time.time()
        n = time_end - time_start
        print('%s executed in %s ms' % (fn.__name__, n))
        print(fn(*args))

    return executime

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)

if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
