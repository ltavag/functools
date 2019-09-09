import time
import random
import functools


def time_it(sample_size):
    def return_fn(fn):
        @functools.wraps(fn)
        def og_fn(args):
            start = time.time()

            for x in range(sample_size):
                fn(args)

            end = time.time()
            print('The function took {} on average'.format(str((end-start)/sample_size)))

        return og_fn
    return return_fn


@time_it(sample_size=100)
def sleep_avg(avg_ms):
    """This function sleeps for an amount of time.

    * Over time it tends to have an average of
    avg_ms.
    """
    x = random.choice(range(2*avg_ms))
    time.sleep(float(x)/1000)


print(sleep_avg.__name__)
print(sleep_avg.__doc__)
