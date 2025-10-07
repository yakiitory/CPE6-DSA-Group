class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        current_node = self.head
        new_node = Node(value)
        while (current_node.next):
            current_node = current_node.next
        current_node.next = new_node
    
    def to_list(self) -> list:
        l = []
        current_node = self.head
        while current_node:    
            l.append(str(current_node.value))
            current_node = current_node.next
        return l
    
    def search(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False
    
    def delete(self, value) -> bool:
        temp_node = self.head

        # if head node is to be deleted
        if temp_node is not None:
            if temp_node.value == value:
                self.head = temp_node.next
                temp_node = None
                return True
        
        # search for value to delete
        # keep track of previous node
        while temp_node is not None:
            if temp_node.value == value:
                break
            previous_node = temp_node
            temp_node = temp_node.next

        # return false if node is not found
        if temp_node == None:
            return False
        
        # switch up pointers
        previous_node.next = temp_node.next

        # free the temp node
        temp_node = None