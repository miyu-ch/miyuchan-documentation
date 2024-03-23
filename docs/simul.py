import numpy as np

def v(n):
    return (3 * ((np.arange(1, n+1) * 10).sum() + n))

def w(n, p):
    return v(n)/p

n = 1 # Level to reach
p = 10 # XP for a message

print("Total XP Required to reach this level:",v(n))
print("Total messages to send to reach this level:",int(w(n, p))+1)
