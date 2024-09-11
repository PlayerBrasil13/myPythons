class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, elem):
        self.__queue.append(elem)

    def get(self):
        if len(self.__queue) > 0:
            self.__first = self.__queue[0]
            del self.__queue[0]
            return self.__first
        else:
            raise QueueError


class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
        self.__counter = 0

    def isempty(self):
        return self.__counter == 0

    def put(self, elem):
        self.__counter += 1
        Queue.put(self, elem)
    
    def get(self):
        self.__counter -= 1
        return Queue.get(self)





que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
