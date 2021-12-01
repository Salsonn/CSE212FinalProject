# Queue

Queues can be found all around our lives. From the line in the grocery store, to a list of homework assignments, even music playlists. All of these are queues, and without them, the would just wouldn't be the same.

## Queue Structure

Queues are a data structure that holds data in a one-dimensional format (that being a line). The most important, and identifiable, characteristic of a queue is it's **first in, first out** ordering system. This means that in a queue, data is added by appending it to the end of the data set, and data is removed or read starting at the first index in the structure.

## Enqueuing Data

In the case of Python, queues can be easily made using a simple list. Data can be added with the built-in ``append()`` function.

Example:
```python
def enqueue(target, addition)
# This function adds the contents of 'addition'
# to the end of the queue specified by 'target'
    target.append(addition)
    return True

queue = [] # Create an empty queue

enqueue(queue, 'first in line')
enqueue(queue, 'second in line')
enqueue(queue, 'third in line')
enqueue(queue, 'fourth in line')

```

## Dequeueing Data

When removing data from a queue, you'll want to have a place to store it. Fortunately, if we use the ``pop()`` function in Python, the value we remove is returned by the function!

Example:
```python
def dequeue(target)
# This function removes and returns the
# item in the front of the queue in 'target'.
    return target.pop(target[0]) # Remove and return the
                                 # first value in the queue.

queue = ['1', '2', '3', '4'] # Create an empty queue

print(dequeue(queue)) # Removes '1' from queue and prints the value.
```

## Example

The following example code shows a simple queue structure within a Python class, which includes enqueueing and dequeuing function.

```python
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, addition)
    # This function adds the contents of 'addition' to the class
        self.queue.append(addition)
        return True

    def dequeue(self):
        # This function removes and returns the next item in the queue.
        return self.queue.pop(self.queue[0])
```

## Problem to Solve

Create a class called Holds. This class holds a queue of library patrons that have placed a hold on any given piece of media. Implement functions for enqueueing, dequeueing, as well as for returning number of patrons in the queue and if the media is available (i.e. the queue is empty).

Create an instance of this class called ``grapes_of_wrath`` and add holds for James, Lilly, Mitchell, and Mary in that order. Print how many holds are on ``grapes_of_wrath``. Then remove the first two from the queue and reprint the number of holds, then check if the media is available. After that, remove the next two from the queue and check if the media is available again.

## Queue Performance

When it comes to queues in Python, the data structure is fairly well-optimized. In other languages, removing an item from the first index of an array would then require iterating through said array to move the rest of the items to their new place in the queue. Python's lists are more versatile in that they don't requre the iteration after removing the first index, which gives them a performance of O(1) to enqueue and dequeue a value from the list, wheras other languages would require 0(n) to dequeue a value (though still only 0(1) to enqueue).

### [<-- Back](../README.md)