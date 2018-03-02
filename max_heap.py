class MaxHeap:
    def __init__(self, heap=[]):
        if heap == []:
            # storing the heap size here
            self.heap = [0]
        else:
            self.heap = [0] + heap
            i = len(self.heap) - 1
            self.heap[0] = i # get the size of the heap
            i = i // 2 # start at parent of last node
            while i > 0:
                self.heapify(i)
                i -= 1

    def __str__(self):
        return str(self.heap[1:]) + " Heap size: {}".format(self.heap[0])
        
    def insert(self, val):
        self.heap.append(val)
        self.heap[0] += 1
        index = self.heap[0] # since we are storing the length
        while (val > self.heap[index//2] and index != 1):
            # store as a temp value
            temp = self.heap[index//2]
            self.heap[index//2] = val
            self.heap[index] = temp
            index = index // 2
            
    def extract_max(self):
        max_value = self.heap[1]
        if self.heap[0] > 1:
            self.heap[1] = self.heap.pop() # get the value from the right-most leaf
            self.heapify(1) # heapify at index 1
        else:
            max_value = self.heap.pop()
        # decrease heap size
        self.heap[0] -= 1             
        return max_value
   
    def sort(self):
        # want to store the original heap we have stored
        temp_heap = self.heap
        sorted_heap = []
        while self.heap[0] > 0:
            sorted_heap.insert(0, self.extract_max())
        self.heap = temp_heap
        return sorted_heap
        
    def heapify(self, i):
        heap_size = self.heap[0]
        left = 2*i
        right = 2*i + 1
        max_value = i
        # make sure that left and right are in the limits of the heap array
        if (left <= heap_size-1 and self.heap[left] > self.heap[i]):
            max_value = left
        if (right <= heap_size-1 and self.heap[right] > self.heap[max_value]):
            max_value = right
        if (max_value != i):
            temp = self.heap[max_value]
            self.heap[max_value] = self.heap[i]
            self.heap[i] = temp
            self.heapify(max_value)
            

if __name__ == "__main__":    
    a = MaxHeap()
    a.insert(8)
    print(a)
    a.insert(1)
    print(a)
    a.insert(3)
    print(a)
    a.insert(4)
    print(a)
    print(a.extract_max())
    print(a)
    b = MaxHeap([4,3,5,8])
    a = MaxHeap([16,17,25,37,48,49,34,46,23,50,10,27])
    print(b)
    print(a)