class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.max_n = k
        self.queue = []

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if len(self.queue) < self.max_n:
            self.queue = self.queue[::-1]
            self.queue.append(value)
            self.queue = self.queue[::-1]
            return True
        return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if len(self.queue) < self.max_n:
            self.queue.append(value)
            return True
        return False
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if len(self.queue):
            del self.queue[0]
            return True
        return False
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if len(self.queue):
            del self.queue[-1]
            return True
        return False
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if len(self.queue):
            return self.queue[0]
        return -1
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if len(self.queue):
            return self.queue[-1]
        return -1
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return not len(self.queue)
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return len(self.queue) == self.max_n