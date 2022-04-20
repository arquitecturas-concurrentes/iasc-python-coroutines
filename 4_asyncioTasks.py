import asyncio
import time

async def say_after(delay, what):
  await asyncio.sleep(delay)
  print(what)

async def main():
  task1 = asyncio.create_task(say_after(1, 'hello'))
  task2 = asyncio.create_task(say_after(2, 'world'))

  await task1
  await task2

if __name__ == '__main__':
  tiempo = time.perf_counter()
  asyncio.run(main())
  tiempo2 = time.perf_counter() - tiempo
  print(f'Tiempo total: {tiempo2:0.2f} segundos')