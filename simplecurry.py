from functools import partial
def curried(fn):
    """Decorator that makes a function curried: f(a, b, c) == f(a)(b)(c) == f(a, b)(c) == f(a)(b, c)
    """
    def wrapped(*args, **kwargs):
        if fn.__code__.co_argcount > len(args) + len(kwargs):
            return partial(curried(fn), *args, **kwargs)
        else:
            return fn(*args, **kwargs)
    return wrapped
