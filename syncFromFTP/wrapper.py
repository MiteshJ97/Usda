import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        # print("Finished {} in {} secs".format(repr(func.__name__), round(run_time, 3)))
        print("This process took {} secs to finish".format(round(run_time, 3)))
        return value

    return wrapper


# @timer
# def doubled_and_add(num):
#     res = sum([i*2 for i in range(num)])
#     print("Result : {}".format(res))
