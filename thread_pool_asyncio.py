from threading import Thread , Condition
import time , asyncio

def thread_speed_test():

    def add1():
        nonlocal count
        nonlocal thread_count
        for i in range(single_test_num):
            with mutex:
                mutex.notify()
                count += 1
                if thread_count > 1:
                    mutex.wait()
        thread_count -= 1
        with mutex:
            mutex.notify()

    mutex = Condition()
    count = 0
    thread_count = thread_num
    thread_list = list()
    for i in range(thread_num):
        thread_list.append(Thread(target = add1))

    st_time = time.time()
    for thr in thread_list:
        thr.start()

    for thr in thread_list:
        thr.join()

    ed_time = time.time()
    print("runtime" , count)
    print(f'threading finished in {round(ed_time - st_time,4)}s ,speed {round(single_test_num * thread_num / (ed_time - st_time),4)}q/s' ,end='\n\n')

def asyncio_speed_test():

    count = 0

    async def switch():
        await asyncio.sleep(0)

    async def add1():
        nonlocal count
        for i in range(single_test_num):
            count += 1
            await switch()

    async def main():

        tasks = asyncio.gather(*(add1() for i in range(thread_num))                        )
        st_time = time.time()
        await tasks
        ed_time = time.time()
        print("runtime" , count)
        print(f'asyncio   finished in {round(ed_time - st_time,4)}s ,speed {round(single_test_num * thread_num / (ed_time - st_time),4)}q/s')

    asyncio.run(main())

if __name__ == "__main__":
    single_test_num = 100000
    thread_num = 2
    thread_speed_test()
    asyncio_speed_test()