import matplotlib.pyplot as plt
from datetime import datetime, timezone
import random

def simulate():
    a = []
    for i in range(1, 15):
        j = datetime.utcnow().replace(day=i)
        a += [j]

    b = []
    for i in range(1, 15):
        j = random.randrange(20, 120)
        b += [j]

    plt.plot(a,b)
    plt.xlabel('date')
    plt.ylabel('time in production')
    plt.show()
