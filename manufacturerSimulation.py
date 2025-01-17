
class Station:
    def __init__(self, name, processingSpeed):
        self.name = name
        self.processingSpeed = processingSpeed
        self.nextStation = None
        self.backLog = 0
        self.maxBackLog = 0
        self.clocktick = 0

    def receive(self):
        self.backLog += 1
        if self.backLog > self.maxBackLog:
            self.maxBackLog = self.backLog
        # print(f'{self.name} received.  Back Log: {self.backLog}    maxBackLog: {self.maxBackLog}')

    def process(self):
        if self.backLog > 0:
            if self.clocktick == self.processingSpeed:
                self.send()
            self.clocktick += 1
        if self.nextStation is not None:
            self.nextStation.process()

    def hasBacklog(self):
        if self.backLog > 0:
            return True
        elif self.nextStation is not None:
            return self.nextStation.hasBacklog()
        else:
            return False

    def send(self):
        self.backLog -= 1
        self.clocktick = 0
        if self.nextStation is not None:
            self.nextStation.receive()
        # print(f'{self.name} sent.  Back Log: {self.backLog}    maxBackLog: {self.maxBackLog}')


def startSimulation(numItems: int):
    station1 = Station("station 1", 1)
    station2 = Station("station 2", 2)
    station3 = Station("station 3", 3)
    station4 = Station("station 4", 2)
    station5 = Station("station 5", 1)

    station1.nextStation = station2
    station2.nextStation = station3
    station3.nextStation = station4
    station4.nextStation = station5

    totalItemsToProcess = numItems
    condition = True
    totalClockticks = 0
    while condition:
        totalClockticks += 1
        if totalItemsToProcess > 0:
            station1.receive()
            totalItemsToProcess -= 1

        station1.process()
        condition = totalItemsToProcess > 0 or station1.hasBacklog()

    print("Number of items to process: " + str(numItems))
    print("Total Clockticks: " + str(totalClockticks))
    print("station 1 max backlog: " + str(station1.maxBackLog))
    print("station 2 max backlog: " + str(station2.maxBackLog))
    print("station 3 max backlog: " + str(station3.maxBackLog))
    print("station 4 max backlog: " + str(station4.maxBackLog))
    print("station 5 max backlog: " + str(station5.maxBackLog))



if __name__ == '__main__':
    startSimulation(100)