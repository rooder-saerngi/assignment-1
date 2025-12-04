import time

class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, element):
        self.queue.append(element)
    def dequeue(self):
        if self.isEmpty():
            return None
        return self.queue.pop(0)
    def isEmpty(self):
        return len(self.queue) == 0
    def size(self):
        return len(self.queue)
    def __str__(self):
        return str(self.queue)
#creating a queue for the lanes
lanes = {
    "AL1": Queue(), "AL2": Queue(), "AL3": Queue(),
    "BL1": Queue(), "BL2": Queue(), "BL3": Queue(),
    "CL1": Queue(), "CL2": Queue(), "CL3": Queue(),
    "DL1": Queue(), "DL2": Queue(), "DL3": Queue(),
}
#Traffic Lights (every ten seconds the lights change )
def Lights_Changer():
    Flag = True
    while True :
        if Flag == True :
            LaneA_lights = "GREEN"
            LaneB_Lights = "RED"
            LaneD_lights = "RED"
            LaneC_lights = "GREEN"

            Flag = False
            time.sleep(10)
        else :
            LaneA_lights = "RED"
            LaneB_Lights = "GREEN"
            LaneD_lights = "GREEN"
            LaneC_lights = "RED"
            Flag = True
            time.sleep(10)


def generator():
    global i
    i =0
    while True :
        #for the non priority lanes (cars are generated every 10 seconds)
        lanes["Al3"].enqueue(f"car_AL3_{i}")
        lanes["BL3"].enqueue(f"car_BL3_{i}")
        lanes["CL3"].enqueue(f"car_CL3_{i}")
        lanes["DL3"].enqueue(f"car_DL3_{i}")

        time.sleep(10)

        #for the priority lanes (cars are generated every 5 seconds)

        lanes["AL2"].enqueue(f"car_AL2_{i}")
        lanes["BL2"].enqueue(f"car_BL2_{i}")
        lanes["CL2"].enqueue(f"car_CL2_{i}")
        lanes["DL2"].enqueue(f"car_DL2_{i}")

        i += 1
