import asyncio
import time

def print_loco(algo):
  return print(algo,'loco')

async def print_re_loco(algo):
  return print(algo,'loco')

def main():
  print_loco('algo')
  coro = print_re_loco('algo')
  asyncio.run(coro)

if __name__ == '__main__':
  tiempo = time.perf_counter()
  main()
  tiempo2 = time.perf_counter() - tiempo
  print(f'Tiempo total: {tiempo2:0.2f} segundos')