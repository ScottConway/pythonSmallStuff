#!/usr/bin/env python3
import math
import time


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def bigloop():
    # Use a breakpoint in the code line below to debug your script.
    for a in range(0, 2023):
        for b in range(0, 2023):
            for c in range(0, 2023):
                if ((a * b + c == 2020) and (a + b * c == 2021)):
                    print(f"a = {a}  b = {b}  c = {c}")


def smartloop1():
    for a in range(0, 2022):
        for b in range(0, 2023):
            c = 2020 - (a * b)
            if ((a * b + c == 2020) and (a + b * c == 2021)):
                print(f"a = {a}  b = {b}  c = {c}")


def smartloop2():
    for a in range(1, 2022):
        maxb = math.ceil(2021 / a) + 1
        for b in range(0, maxb):
            c = 2020 - (a * b)
            if (a * b + c == 2020) and (a + b * c == 2021):
                print(f"a = {a}  b = {b}  c = {c}")


def smartloop3():
    mina = math.trunc(math.sqrt(2021))
    for a in range(mina, 2022):
        maxb = math.ceil(2021 / a) + 1
        for b in range(0, maxb):
            c = 2020 - (a * b)
            if (a * b + c == 2020) and (a + b * c == 2021):
                print(f"a = {a}  b = {b}  c = {c}")


def singleLoop():
    b = 0

    for a in range(0, 2022):
        inner = (a * a) - (2021 * a) + 1020100
        if inner < 0:
            continue

        c = 1010 - math.sqrt(inner)
        if a == 0 and c == 0:
            continue

        if c != math.trunc(c):
            continue

        if c == 0:
            b = 0
            c = 2020 - (a * b)
        else:
            b = (2021 - a) / c

        if b != math.trunc(b):
            continue

        if (a * b + c == 2020) and (a + b * c == 2021):
            print(f"a = {a}  b = {b}  c = {c}")


def timeFunction(functionName, func):
    print(f"{functionName}")
    tic = time.perf_counter()
    func()
    toc = time.perf_counter()
    print(f"Executed in {toc - tic:0.4f} seconds\n")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    timeFunction("bigloop", bigloop)
    timeFunction("smartloop1", smartloop1)
    timeFunction("smartloop2", smartloop2)
    timeFunction("smartloop3", smartloop3)
    timeFunction("singleLoop", singleLoop)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
