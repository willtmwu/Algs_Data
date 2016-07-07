class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""

        posIndex = 1;
        currentNode = self.head
        if position < 1:
            return None
        while currentNode!=None and posIndex <= position:
            if posIndex == position:
                return currentNode  
            currentNode = currentNode.next
            posIndex+=1

        return None
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""

        posIndex = 1;
        currentNode = self.head

        if position>1:
            while currentNode!=None and posIndex < position:
                if posIndex == position-1:
                    new_element.next = currentNode.next
                    currentNode.next = new_element
                posIndex+=1
                currentNode = currentNode.next
        elif position==1:
            new_element.next = self.head
            self.head = new_element
    
    def delete(self, value):
        """Delete the first node with a given value."""
        prevNode = None
        currentNode = self.head

        while currentNode != None:
            if currentNode.value == value:
                if prevNode != None:
                    prevNode.next = currentNode.next
                else:
                    self.head = currentNode.next

            prevNode = currentNode    
            currentNode = currentNode.next
        

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

# Test insert
ll.insert(e4,3)
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value
