import time
import random

def sleep_avg(avg_ms):
    """This function sleeps for an amount of time.

    * Over time it tends to have an average of
    avg_ms.
    """
    x = random.choice(range(2*avg_ms))
    time.sleep(float(x)/1000)

sleep_avg(100)
print(sleep_avg.__doc__)
