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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tic = time.perf_counter()
    smartloop3()
    toc = time.perf_counter()
    print(f"Executed in {toc - tic:0.4f} seconds")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
