class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def removeDuplicates(self, head):
    '''takes the head of a linked list as an argument
    and removes any duplicates in that list
    list has to be in ascending order '''
    #Write your code here
    prev_data = 0
    curr = head
    while curr.next:
        if curr.data == curr.next.data:
            # point to next
            cnext = curr.next
            curr.next = cnext.next
            # unlink node
            cnext.next = None
            # check to make sure next node does not have same data
        else:
            curr = curr.next
    return head
