import time
import threading

#Making the class for Queue
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
laneA_lights = "RED"
laneB_lights = "RED"
laneC_lights = "RED"
laneD_lights = "RED"
def Lights_Changer():
    global LaneA_lights, LaneB_Lights, LaneD_lights, LaneC_lights
    Flag = True
    while True :
        if Flag == True :
            LaneA_lights = "GREEN"
            LaneB_Lights = "RED"
            LaneD_lights = "RED"
            LaneC_lights = "GREEN"
            print("A:",LaneA_lights,"B:",LaneB_Lights,"D:",LaneD_lights,"C:",LaneC_lights,"\n")

            Flag = False
            time.sleep(9)
        else :
            LaneA_lights = "RED"
            LaneB_Lights = "GREEN"
            LaneD_lights = "GREEN"
            LaneC_lights = "RED"
            print("A:",LaneA_lights,"B:",LaneB_Lights,"D:",LaneD_lights,"C:",LaneC_lights,"\n")
            Flag = True
            time.sleep(9)


def generator():
    global i
    i =0
    while True :
        #for the non priority lanes (cars are generated every 10 seconds)
        lanes["AL3"].enqueue(f"car_AL3_{i}")
        lanes["BL3"].enqueue(f"car_BL3_{i}")
        lanes["CL3"].enqueue(f"car_CL3_{i}")
        lanes["DL3"].enqueue(f"car_DL3_{i}")
        print(f"Generated cars {i} in AL3, BL3, CL3, DL3\n")

        time.sleep(10)

        #for the priority lanes (cars are generated every 5 seconds)

        lanes["AL2"].enqueue(f"car_AL2_{i}")
        lanes["BL2"].enqueue(f"car_BL2_{i}")
        lanes["CL2"].enqueue(f"car_CL2_{i}")
        lanes["DL2"].enqueue(f"car_DL2_{i}")
        print(f"Generated cars {i} in AL2, BL2, CL2, DL2\n")
        i += 1

        time.sleep(5)
def traversal():
    global LaneA_lights,LaneB_Lights,LaneD_lights,LaneC_lights

    while True :
        if LaneA_lights == "GREEN" :

            if not lanes["AL2"].isEmpty() :
                car = lanes["AL2"].dequeue()
                lanes["BL1"].enqueue(car)
                print(f"AL2 car moved to BL1\n")

            elif not lanes["AL3"].isEmpty():
                car = lanes["AL3"].dequeue()
                lanes["CL1"].enqueue(car)
                print(f"AL3 moved to CL1\n")

        if LaneB_Lights == "GREEN" :

            if not lanes["BL2"].isEmpty() :
                car = lanes["BL2"].dequeue()
                lanes["AL1"].enqueue(car)
                print(f"BL2 car moved to AL1\n")

            elif not lanes["BL3"].isEmpty():
                car = lanes["BL3"].dequeue()
                lanes["DL1"].enqueue(car)
                print(f"BL3 car moved to DL1\n")

        if LaneD_lights == "GREEN" :

            if not lanes["DL2"].isEmpty() :
                car = lanes["DL2"].dequeue()
                lanes["CL1"].enqueue(car)
                print(f"DL2 car moved to CL1\n")

            elif not lanes["DL3"].isEmpty():
                car = lanes["DL3"].dequeue()
                lanes["AL1"].enqueue(car)
                print(f"DL3 car moved to AL1\n")

        if LaneC_lights == "GREEN" :

            if not lanes["CL2"].isEmpty() :
                car = lanes["CL2"].dequeue()
                lanes["DL1"].enqueue(car)
                print(f"CL2 car moved to DL1\n")

            elif not lanes["CL3"].isEmpty():
                car = lanes["CL3"].dequeue()
                lanes["BL1"].enqueue(car)
                print(f"CL3 car moved to BL1\n")

threading.Thread(target=Lights_Changer,daemon= True).start()
threading.Thread(target=generator,daemon= True).start()
threading.Thread(target=traversal,daemon= True).start()

while True :
    time.sleep(1)
