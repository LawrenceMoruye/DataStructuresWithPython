"""
Make a Queue class using a list.
from Udacity's Introduction to Data Structures
 and Algorithm
 """
 
class Queue(object):
    def __init__(self,head = None):
        self.storage = [head]

    def enqueue(self,new_element):
        self.storage.append(new_element)

    def peek(self):
        '''
        have a look at the first element
        but dont do anything
        '''
        return self.storage[0]

    def dequeue(self):
        return self.storage.pop(0)

if __name__ =="__main__":
    #setup
    q = Queue(1)
    q.enqueue(2)
    q.enqueue(3)

    #test peek
    print(q.peek())

    #testing dequeue
    print(q.dequeue())

    #test enqueue
    q.enqueue(4)

    #dequeue
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

    q.enqueue(5)
    print(q.peek())
