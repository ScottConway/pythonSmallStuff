import random
import time

LOOPSIZE = 1000000

def simpleMontyHall():
    staywins = 0
    changewins = 0
    for i in range(LOOPSIZE):
        chosen_door = random.randint(0, 2)
        winning_door = random.randint(0, 2)
        if chosen_door == winning_door:
            staywins += 1
        else:
            changewins += 1

    print(f"number of staywins: {staywins}   number of changewins: {changewins}\n")

def timeFunction(functionName, func):
    print(f"{functionName}")
    tic = time.perf_counter()
    func()
    toc = time.perf_counter()
    print(f"Executed in {toc - tic:0.4f} seconds\n")

if __name__ == '__main__':
    timeFunction("simpleMontyHall", simpleMontyHall)