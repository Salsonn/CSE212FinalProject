class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, addition):
    # This function adds the contents of 'addition' to the class
        self.queue.append(addition)
        return True

    def dequeue(self):
        # This function removes and returns the next item in the queue.
        return self.queue.pop(self.queue[0])

grapes_of_wrath = Queue()

grapes_of_wrath.enqueue("James")
grapes_of_wrath.enqueue("Lilly")
grapes_of_wrath.enqueue("Mitchell")
grapes_of_wrath.enqueue("Mary")


print(len(grapes_of_wrath.queue))

grapes_of_wrath.dequeue()
grapes_of_wrath.dequeue()

print(len(grapes_of_wrath.queue))