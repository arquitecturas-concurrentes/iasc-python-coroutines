import time
import asyncio

async def rat():
    await asyncio.sleep(3)
    return "🐀"

async def ssss():
    await asyncio.sleep(1)
    return "🐍🐍🐍"

async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(rat())
        task2 = tg.create_task(ssss())
    print(f"Result: {task1.result()}, {task2.result()}")

if __name__ == '__main__':
    tiempo = time.perf_counter()
    asyncio.run(main())
    tiempo2 = time.perf_counter() - tiempo
    print(f'Tiempo total: {tiempo2:0.2f} segundos')
