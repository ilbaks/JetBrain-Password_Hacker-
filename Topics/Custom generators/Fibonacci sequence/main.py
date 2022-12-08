def fibonacci(n):
    a = 0
    yield a
    b = 1
    yield b
    i = 2
    while i < n:
        save = b
        b = a + b
        a = save
        yield b
        i += 1

        #yield b
