import time
import numpy as np

from rich import print

JURYSIZE = 64
ARRAYSIZE = JURYSIZE + 2
MINDELTA = 0.0000000001

def jurysimulation():
    array = np.zeros((ARRAYSIZE, ARRAYSIZE), dtype=float)

    for i in range(ARRAYSIZE):
        array[0, i] = 1.0

    iterations = 0

    while True:
        delta = 0.0

        for i in range(1, ARRAYSIZE - 1):
            for j in range(1, ARRAYSIZE - 1):
                originalValue = array[i, j]
                array[i, j] = (array[i - 1, j] + array[i + 1, j] + array[i, j - 1] + array[i, j + 1]) / 4.0
                delta += abs(originalValue - array[i, j])

        iterations += 1

        if delta < MINDELTA:
            break

        if iterations % 1000 == 0:
            print(f"Iteration: {iterations}   Delta: {delta}   Min: {MINDELTA}")

    print(f"Number of iterations: {iterations}")

def timeFunction(functionName, func):
    print(f"{functionName}")
    tic = time.perf_counter()
    func()
    toc = time.perf_counter()
    print(f"Executed in {toc - tic:0.4f} seconds\n")

if __name__ == '__main__':
    timeFunction("Jury Simulation", jurysimulation)