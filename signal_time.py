from signal_generator import *
import time

timer=[]
moments = []



for j in range(1, 100, 1):
    n = 12 * j
    w = 2700
    N = 640
    moments.append(n)
    start_time = time.time()
    calculate(n, w, N)
    timer.append(time.time() - start_time)



plt.plot(moments, timer)
plt.show()

