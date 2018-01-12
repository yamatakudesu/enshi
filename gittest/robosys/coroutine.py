def coroutine():
    hello = yield "Hello"
    yield hello


coro = coroutine()
print(next(coro))
print(coro.send("World"))
