import multiprocessing
import time

def cpu_load():
    while True:
        pass

if __name__ == "__main__":
    processes = []
    for _ in range(4):  # Change 4 to the number of CPU cores you want to stress
        p = multiprocessing.Process(target=cpu_load)
        p.start()
        processes.append(p)
    time.sleep(60)  # Run for 60 seconds
    for p in processes:
        p.terminate()