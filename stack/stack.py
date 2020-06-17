from singly_linked_list import LinkedList

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?

# LinkedList
  # Memory storage for LL is more dynamic than arrays.
  # insertion and deletion are easier and faster
  # require more net memory for functionality
  # memory utilization is more efficient
  # dynamic and flexible

# Array
  # arrays are quicker as have set size
  # accessing an element is faster
  # data is contiguous
  # elements belong to an index
  # insertion and deletion are more intensive
  # memory utilization inefficient
"""


# --- array --
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         if len(self.storage) > 0:
#             return self.storage.pop()


# --- linkedlist ---

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_tail()
        else:
            return None