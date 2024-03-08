from functools import wraps
from threading import Thread
from queue import Queue


def do_stuff(q1, a, k, method):
    try:
        q1.put(method(*a, **k))
    except Exception as e:
        q1.put(e)


def timeout(sec=3):
    def timeout_dec(func):
        @wraps(func)
        def test(*args, **kwargs):
            q = Queue()
            p = Thread(target=do_stuff, args=[q, args, kwargs, func], kwargs={}, daemon=True)
            p.start()
            p.join(sec)

            if p.is_alive():
                # I can't kill the thread, but just keep the tests running.
                raise TimeoutError(f"Timed out after {sec} seconds")
            else:
                x = q.get()
                if isinstance(x, Exception):
                    raise x
                return x
        return test
    return timeout_dec
