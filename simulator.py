class Queue:
    def __init__(self):
        self.queue = []
        self.head = self.tail = -1

    def enqueue (self,element):
        self.queue.append(element)
    def dequeue(self):
        if self.isEmpty():
            return "queue is empty"
        return self.queue.pop(0)
    def isEmpty(self):
        if self.head == -1:
            return "the queue is empty"

#creating a queue for the lanes
VQueueA_AL1_outgoing = Queue()
VQueueA_AL2_outgoing = Queue()
VQueueA_AL3_outgoing = Queue()

VQueueA_AL1_incoming = Queue()
VQueueA_AL2_incoming = Queue()
VQueueA_AL3_incoming = Queue()

VQueueB_BL1_outgoing = Queue()
VQueueB_BL2_outgoing = Queue()
VQueueB_BL3_outgoing = Queue()

VQueueB_BL1_incoming = Queue()
VQueueB_BL2_incoming = Queue()
VQueueB_BL3_incoming = Queue()

VQueueC_CL1_outgoing = Queue()
VQueueC_CL2_outgoing = Queue()
VQueueC_CL3_outgoing = Queue()

VQueueC_CL1_incoming = Queue()
VQueueC_CL2_incoming = Queue()
VQueueC_CL3_incoming = Queue()

VQueueD_BL1_outgoing = Queue()
VQueueD_BL2_outgoing = Queue()
VQueueD_BL3_outgoing = Queue()

VQueueD_BL1_incoming = Queue()
VQueueD_BL2_incoming = Queue()
VQueueD_BL3_incoming = Queue()

#Traffic Lights
Traffic_Light = ["RED","GREEN"]
