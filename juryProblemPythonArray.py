import time
import array

from rich import print

JURYSIZE = 64
ARRAYSIZE = JURYSIZE + 2
MINDELTA = 0.0000000001

"""
This module contains functions for solving problems related to 1D arrays in a jury context.
"""
class JuryPool:
    """
    Represents a pool of jurors for jury selection.
    """
    arraySize = 0
    jurors = array.array('d')

    def __init__(self, jurySize: int):
        self.jurySize = jurySize
        self.arraySize = jurySize+2
        for i in range(self.arraySize):
            self.jurors.append(1.0)
        for i in range(self.arraySize, (self.arraySize*self.arraySize)):
            self.jurors.append(0.0)

    def position(self, x: int, y: int)->int:
        return (x*self.arraySize)+y

    def iterate(self):
        delta = 0.0
        for i in range(1, self.arraySize-1):
            for j in range(1, self.arraySize-1):
                p = self.position(i, j)
                pUp = p - self.arraySize
                pDown = p + self.arraySize
                pLeft = p - 1
                pRight = p + 1
                # print(f"i: {i} j:{j} p: {p} pUp: {pUp}, pDown: {pDown}")
                oldValue = self.jurors[p]
                self.jurors[p] = (self.jurors[pUp] + self.jurors[pDown] + self.jurors[pRight] + self.jurors[pLeft]) / 4.0
                delta += (self.jurors[p] - oldValue)
        return delta

    def iterateUntilConvergence(self):
        delta = 1.0
        iteration = 0
        while delta > MINDELTA:
            delta = self.iterate()
            iteration += 1
            if iteration%1000 == 0:
                print(f"iteration: {iteration}  \tDelta: {delta:.10f}")

        print(f"Converged!  iteration: {iteration}  \tDelta: {delta:.10f}")

def jurysimulation():
    jp = JuryPool(JURYSIZE)
    jp.iterateUntilConvergence()


def timeFunction(functionName, func):
    print(f"{functionName}")
    tic = time.perf_counter()
    func()
    toc = time.perf_counter()
    print(f"Executed in {toc - tic:0.4f} seconds\n")

if __name__ == '__main__':
    timeFunction("Jury Simulation", jurysimulation)

