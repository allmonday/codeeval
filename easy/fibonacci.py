args = [
"5",
"32"
]

def memo(fn):
    cache = {}
    def wrap(n):    
        if n in cache:
            return cache[n]
        else:
            cache[n] = fn(n)
            return cache[n]
    return wrap

@memo
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for arg in args:
    print fibonacci(int(arg))
