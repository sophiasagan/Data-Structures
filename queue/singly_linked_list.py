class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None # stores a node, that corresponds to our first node in the list
        self.tail = None # stores a node that is the end of the list

    def add_to_head(self, value):
        # create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # new_node should point to current head
            new_node.next_node = self.head
            # move head to new node
            self.head = new_node

    def add_to_tail(self, value):
        # create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # point the node at current tail , to the new node
            self.tail.next_node = new_node
            self.tail = new_node

    def remove_head(self):
        # if list is empty do nothing
        if not self.head:
            return None
        # if list only has one element, set head and tail to None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        # othersie we have more elements in the list
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value
    
    def contains(self, value):
        if self.head is None:
            return False

        #loop through each node, untile we see the value, or we cannot go further
        current_node = self.head

        while current_node is not None:
            # check if this is the node we are looking for
            if current_node.value == value:
                return True

            # otherwise, go to the next node
            current_node = current_node.next_node
        return False

    def get_max(self):
        if not self.head:
            return None
        # largest value so far
        max_value = self.head.get_value()
        # current node in list
        current = self.head.get_next()
        # check to see if we're still at a valid list node
        while current:
            # check if current value is greater than the max_value
            if current.get_value() > max_value:
                # if so, update our max_value variable
                max_value = current.get_value()
            # update the current node to the next node in the list
            current = current.get_next()
        return max_value

    def remove_tail(self):
        if not self.head:
            return None

        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value

        current = self.head

        while current.get_next() is not self.tail:
            current = current.get_next()

        value = self.tail.get_value()
        self.tail = current
        return value

# example
# linked_list = LinkedList()
# linked_list.add_to_head(0)
# linked_list.add_to_tail(1)
# print(f'does our LL contain 0? {linked_list.contains(0)}')
# print(f'does our LL contain 1? {linked_list.contains(1)}')
# print(f'does our LL contain 2? {linked_list.contains(2)}')

# linked_list.add_to_head(2)
# print(f'the start of the list is {linked_list.head.value}')
# linked_list.add_to_head(5)
# print(f'the start of the list is {linked_list.head.value}')
# linked_list.remove_head()
# print(f'the start of the list is {linked_list.head.value}')

