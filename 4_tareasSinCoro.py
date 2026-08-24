import time

def io():
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('3')

def main(tareas):
    for tarea in tareas:
        io()

if __name__ == '__main__':
    tiempo = time.perf_counter()
    main(range(3))
    tiempo2 = time.perf_counter() - tiempo
    print(f'Tiempo total: {tiempo2:0.2f} segundos')