"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # create a new_node
        new_node = ListNode(value)
        self.length += 1 # update length
        if not self.head and not self.tail: # if there is no head or tail node
            self.head = new_node # new node will be head
            self.tail = new_node # and tail
        else: # if node already exists
            new_node.next = self.head # new node's next is current head
            self.head.prev = new_node # previous pointer to the new node from current head
            self.head = new_node # new node is the head

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value  # value of node to remove
        self.delete(self.head) # ListNode delete method
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None) # create new node
        self.length += 1 # length update
        if not self.head and not self.tail: # if there's no head or tail
            self.head = new_node # new node will be head
            self.tail = new_node # and tail
        else:
            new_node.prev = self.tail # new node previous pointer becomes current tail
            self.tail.next = new_node # next point to new node
            self.tail = new_node # new node is the tail


    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value # value of node to remove
        self.delete(self.tail) # ListNode delete method
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node is self.head: # if node is the head already
            return
        self.delete(node) # ListNode delete method
        self.add_to_head(node.value) # ListNode add to head method

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail: # if node is the tail already
            return
        self.delete(node) # ListNode delete method
        self.add_to_tail(node.value) # ListNode add to tail method

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        self.length -= 1 
        if self.head is self.tail: # if only node
            self.head = None # remove pointer to head
            self.tail = None # remove pointer to tail
        elif node is self.head: # if node is head
            self.head = node.next # assign the head to current head next pointer
            node.delete() # delete method from ListNode
        elif node is self.tail: # if node is tail
            self.tail = node.prev # assign the tail to current tail next pointer
            node.delete() # delete method from ListNode
        else: # if neither head or tail
            node.delete() # delete method from ListNode
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if self.length > 0:
            max_value = self.head.value # max variable
            current = self.head
            while current.next != None: # loop through nodes
                if current.value > max_value: # compare values until max node value found
                    max_value = current.value
                current = current.next
            if max_value > current.value:
                return max_value # return max value
            else:
                return current.value
        else:
            return None
