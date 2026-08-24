from asyncio import Future
from Fetcher import fetcher

def fetch(self, url):
    #ej del fetch que podria implementar Fetcher
    response = yield from self.session.get(url)
    body = yield from response.read()

class Task:
    def __init__(self, coro):
        self.coro = coro
        f = Future()
        f.set_result(None)
        self.step(f)

    def step(self, future):
        try:
            next_future = self.coro.send(future.result)
        except StopIteration:
            return

        next_future.add_done_callback(self.step)

if __name__ == '__main__':
  fetcher = Fetcher('/333/')
  Task(fetcher.fetch())
