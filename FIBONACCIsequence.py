import numpy as np
def Fibonacci(N):
    if N == 0: return np.array(1)
    fib = np.zeros(N+1, dtype=int)  
    fib[0], fib[1] = 1, 1
    for k in range(2,N+1):
        fib[k] = fib[k-1] + fib[k-2]
    return fib
print(Fibonacci(10))
