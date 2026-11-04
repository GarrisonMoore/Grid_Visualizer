from typing import Any

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self) -> str:
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def __repr__(self):
        # If the list is empty, return "None"
        if not self.head_node:
            return "None"

        result = ""
        current_node = self.head_node

        # Iterate through the list and concatenate each node's data
        while current_node is not None:
            result += f"{current_node.data} <-> "
            current_node = current_node.next

        result += "None"
        return result

    def append_left(self, data:Any):
        """
        Append to the head of the list
        """
        # Create a new node with specified data
        new_node = Node(data)

        # If the list is empty
        if not self.head_node:
            # assign new node to the head and tail
            self.head_node = new_node
            self.tail_node = new_node
            return "List is empty. Appending your node to the empty list."

        else:
            # Point the new node to the head node
            new_node.next = self.head_node
            # Point the previous head node backward to the new node
            self.head_node.prev = new_node

            # Reassign the head node to the new node
            self.head_node = new_node

            return f"Appending: {new_node} to the head."

    def append_right(self, data:Any):
        """
        Append to the tail of the list
        """
        # Create a new node with specified data
        new_node = Node(data)

        # If the list is empty
        if not self.head_node:
            # assign new node to the head and tail and raise an error
            self.head_node = new_node
            self.tail_node = new_node

            return TypeError("List is empty. Appending your node to the empty list.")
        else:
            # Point the new node backward to the tail node
            new_node.prev = self.tail_node

            # Point the old tail node forward to the new node
            self.tail_node.next = new_node

            # Reassign the main tail pointer to the new node
            self.tail_node = new_node

            return f"Appending: {new_node} to the tail."

    def pop_left(self):
        """
        Removes the head element from the list
        """
        # If the list is empty
        if not self.head_node:
            raise TypeError("List is empty, nothing to remove.")
            return "List is empty, nothing to remove."

        # if there is only 1 element in the list
        elif self.head_node == self.tail_node:
            # mark the head node for removal
            node_to_remove = self.head_node

            # set head and tail node to None
            self.head_node = None
            self.tail_node = None

            return node_to_remove
        else:
            # mark the head node for removal
            node_to_remove = self.head_node

            # point the head node to the next node from the head
            self.head_node = self.head_node.next

            # return the node we removed
            return f"Removing: {node_to_remove}"

    def pop_right(self):
        """
        Removes the tail element from the list
        """
        # if the list is empty
        if not self.head_node:
            raise TypeError("List is empty, nothing to remove.")
            return "List is empty, nothing to remove."

        # if there is only 1 element in the list
        elif self.head_node == self.tail_node:
            # mark the head node for removal
            node_to_remove = self.head_node

            # set head and tail node to None
            self.head_node = None
            self.tail_node = None

            return node_to_remove
        else:
            # Mark the tail node for removal
            node_to_remove = self.tail_node

            # Assign the tail node to the node before it
            self.tail_node = self.tail_node.prev

            # Assign the new tails .next pointer to None
            self.tail_node.next = None

            return f"Removing: {node_to_remove}"

    def contains(self, target_data):
        """
        Searches the list for specified data
        """
        # Assign current node to th head
        current_node = self.head_node

        while current_node is not None:
            # If the data in the current node matches the target data
            if current_node.data == target_data:
                return True
            # Keep iterating
            current_node = current_node.next
        return False


# ===== Testing =====

llist = LinkedList()
print(f"Empty List:\n({llist})\n")

print(f"Calling 'contains()' method on the list:")
print(f"List: {llist}\n")
print(f"{llist.contains(3)}\n")

print(f"Calling 'pop_right()' method on the list:")
llist.pop_right()
print(f"List: {llist}\n")

print(f"Calling 'pop_left()' method on the list:")
llist.pop_left()
print(f"List: {llist}\n")

# printing my Error handling
print(f"Calling 'append_right()' method on the empty list:")
print(llist.append_right("y"))
print(f"List: {llist}\n")

print(f"Calling 'pop_right()' method on the list:")
llist.pop_right()
print(f"List: {llist}\n")

print(f"Calling 'append_left()' method on the empty list:")
llist.append_left("x")
print(f"{llist})\n")

print(f"Calling 'pop_left()' method on the list:")
llist.pop_left()
print(f"{llist})\n")

# Append a letter to the head
llist.append_left("x")
print(f"Appending 'x' to the head:\n({llist})\n")

# Pop the tail element from the list
llist.pop_right()
print(f"Removing the tail element:\n({llist})\n")

# append an element to the tail
llist.append_right("y")
print(f"Appending 'y' to the tail:\n({llist})\n")

# Append 5 nodes to the tail
for i in range(5):
    llist.append_right(i)
print(f"Appending 5 nodes to the tail:\n({llist})\n")

# Remove the head element
llist.pop_left()
print(f"Removing the head element:\n({llist})\n")

# remove the tail element
llist.pop_right()
print(f"Removing the tail element:\n({llist})\n")

print(llist.contains(3))


# BRUH why does this work
print(llist.head_node.next.next.prev.prev.next.prev.next.next.next)