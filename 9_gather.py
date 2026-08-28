import time
import asyncio

async def rat():
    await asyncio.sleep(3)
    return "🐀"

async def ssss():
    await asyncio.sleep(1)
    return "🐍🐍🐍"

async def main():
    result = await asyncio.gather(rat(), ssss())
    print(result)

if __name__ == '__main__':
    tiempo = time.perf_counter()
    asyncio.run(main())
    tiempo2 = time.perf_counter() - tiempo
    print(f'Tiempo total: {tiempo2:0.2f} segundos')
