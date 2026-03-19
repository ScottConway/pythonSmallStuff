class MyRandom:
    v = 3

    def __init__(self):
        pass

    def random(self):
        self.v = self.v ** 3 % (2 ** 32 - 5)
        return self.v

    def random1(self):
        num = self.random() / (2 ** 32 - 5)
        return num

    def randomint(self, max: int) -> int:
        num = int(self.random1() * max)
        return num

    def setSeed(self, newSeed):
        self.v = newSeed


def runTest():
    myRandom = MyRandom()
    for i in range(100):
        # print(myRandom.random1())
        print(myRandom.randomint(100))


if __name__ == '__main__':
    runTest()
