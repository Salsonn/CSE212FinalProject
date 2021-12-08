# Set

Set data structures are a type of unordered data structure. These are used in instances where, unlike in queues, stacks, or lists, the order of the items in the structure does not matter. Sets also have one very important qualifying feature: each data point must have a unique value.

## Set Structure

Because each value in a data set is unordered, this means we would theoretically need to iterate through the entire set of data each time we need to find a data point within the structure. However, this is extremely slow, so we instead we can take advantage of the data's uniqueness attribute to design alternate searching algorithms.

Because there are no duplicate values in the data, this means we can only have so many possible values, and that allows us to store a data point at an index that mirrors its contents. While this is effective on the small scale, it quickly generates massive amounts of overhead as the size of the data set increases.

To mitigate this issue, we generate a hash for each value, and use the hash for storage address assignment. This solution is extremely fast, performing at O(1), but comes with the drawback of the hashes potentially appearing more than one time, as the number of unique hashes can be smaller than the number of unique values. To address this issue, there are two different techniques that can be used.

## Open Addressing

When using open addressing, duplicate hashes are stored in any adjacent available address. There are multiple ways this can be implemented, and it is important to remember that this method can quickly grow out of control if conflicts generate any overlap. This is also slower, as multiple addresses need to be checked for a given value.

## Chaining

Another technique to handle duplicate hashes is chaining. In this technique, whenever a conflict occures, the data at that given address is moved into a new, chained list along with its conflict, and that list is then linked to in the original set structure. This is also slower, as the second list must be iterated through per item, but it is less likely to have serious issues when handling conflicts.

## Common Set Methods

* ``add()`` Adds the specified value to the set.
* ``remove()`` Removes the specified value from the set.
* ``member()`` Returns True if the specified value is found within a set.
* ``size()`` Returns an integer reflecting the number of data points in the set.

## Example

In Python, we can easily create set structures using the dict data type, which are indicated by ``{}`` brackets. Data within dicts can be manipulated in simple ways with the ``add()`` and ``remove()`` functions. Sets can hold a variety of data types, and we are using numbers here simply for readability.

```python
exampleSet = {1, 2, 3, 4, 5, 6}
print(exampleSet)

exampleSet.add(8)
print(exampleSet)

exampleSet.remove(2)
print(exampleSet)
```

## Problem to Solve

Python comes equipped with the ``hash()`` function for quickly generating a has based on whatever input it is given, though not every data type is hashable by this function. Since the hash is numeric, you can compress the size of your set by using ``index(number) = hash(n) % 10`` to generate a smaller set of data to work with.

Using this information, create a set data structure that can store up to 16 random values between 1 and 128.

The solution to this challenge is available [here](/res/hasher.py).

### [<-- Back](../README.md)