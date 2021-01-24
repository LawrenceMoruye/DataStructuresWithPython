"""
LinkedList Implementation from the Udacity Course:
Introduction to Data Structures And Algorithms.
It contains 3 functions:
get_position:returns the element at a certsin position
insert:Add an element to a particular spot in ghe list
delete:deletes the first element with that particular value

"""
class Element(object):
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self,head=None):
        self.head = head
    
    def append(self,new_element):
        """
        If the LinkedList already has a head, 
        iterate through the next reference in every 
        Element until you reach the end of the list. 
        Set next for the end of the list to be the 
        new_element. Alternatively, if there is no head 
        already, you should just assign new_element to 
        it and do nothing else.
        """
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self,position):
        """
        Get an element in a particular position.
        Assume the 1st position is 1,return 
        None if position not in list
        """
        counter = 1
        current = self.head
        if position < 1:
            return None

        while current and counter <= position:
            if counter ==position:
                return current

            current = current.next
            counter +=1
        return None

    def insert(self,new_element,position):
        """
        insert a new node at a given position.
        Assuming the first position is 1,
        inserting at position 3 means
        btn 2nd and 3rd elements
        """
        counter = 1
        current = self.head
        if position >1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete(self,value):
        """
        delete the first node with a given value
        """

        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next

        if current.value == value:
            if previous:
                previous.next = current.next

            else:
                self.head = current.next  

if __name__ =="__main__":

    #Test cases
    #setting up some elements
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)    

    #setting up the Linkedlist
    ll = LinkedList(e1)
    ll.append(e2)
    ll.append(e3)

    #testing get position
    print(ll.head.next.next.value)
    print(ll.get_position(3).value)

    #Testing insert
    ll.insert(e4,3)
    print(ll.get_position(3).value)


    #Testing delete
    ll.delete(1)
    print(ll.get_position(1).value)
    print(ll.get_position(2).value)
    print(ll.get_position(3).value)









