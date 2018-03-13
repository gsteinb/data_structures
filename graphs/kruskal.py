import sys

class MinHeap:
    ''' MinHeap implementation that uses graph edges.
    Each graph edge is in the format [current vertex, destination vertex, weight]
    e.g. [1,2,3] is the edge from vertex 1 to vertex 2 with weight 3'''
    def __init__(self, heap=[]):
        if heap == []:
            # storing the heap size here
            self.heap = [0]
        else:
            self.heap = [0] + heap
            i = len(self.heap) - 1
            self.heap[0] = i # get the size of the heap
            i = i // 2 # start of parent of last node
            while i > 0:
                self.heapify(i)
                i -= 1
                
    def is_empty(self):
        '''returns a boolean that indicates if the heap is empty
        >>>heap = MinHeap([1,2,3])
        >>>heap.is_empty
        False
        >>>heap = MinHeap()
        >>>heap.is_empty
        True
        '''
        return self.heap[0] == 0

    def __str__(self):
        return str(self.heap[1:]) + " Heap size: {}".format(self.heap[0])
        
    def insert(self, val):
        ''' inserts a value into the heap at the correct position
        @param val -> the value that is to be inserted
        In this implementation the value must be a graph edge'''
        self.heap.append(val)
        self.heap[0] += 1
        index = self.heap[0] # since we are storing the length
        while (index != 1 and val[2] < self.heap[index//2][2] ):
            # store as a temp value
            temp = self.heap[index//2]
            self.heap[index//2] = val
            self.heap[index] = temp
            index = index // 2
            
    def extract_min(self):
        '''Extracts and returns the minimum element in the heap and then
        heapifies starting at index 1. In this implementation the minimum
        element is the element with the least edge weight stored in index 2
        >>>heap = MinHeap([[1,2,3], [3,2,1]])
        [3,2,1]
        '''
        min_value = self.heap[1]
        if self.heap[0] > 1:
            self.heap[1] = self.heap.pop() # get the value from the right-most leaf
            self.heap[0] -= 1
            self.heapify(1) # heapify at index 1
        else:
            min_value = self.heap.pop()
            # decrease heap size
            self.heap[0] -= 1
        return min_value
        
    def heapify(self, i):
        '''Calls heapifies the heap starting at index i
        @param i -> the index at which to heapify'''
        heap_size = self.heap[0]
        left = 2*i
        right = 2*i + 1
        min_value = i
        # make sure that left and right are in the limits of the heap array
        if (left <= heap_size and self.heap[left][2] < self.heap[i][2]):
            min_value = left
        if (right <= heap_size and 
            self.heap[right][2] < self.heap[min_value][2]):
            min_value = right
        if (min_value != i):
            temp = self.heap[min_value]
            self.heap[min_value] = self.heap[i]
            self.heap[i] = temp
            self.heapify(min_value)
            
def mst(n, edges):
    '''function that returns sum of MST edges using kruskals algorithm
    @param n -> number of vertices in the graph
    @param edges -> array with edges in the graph
    @returns -> the sum of the edges in the MST'''
    # create a visited array
    rsum = 0
    clusters = [0] * (n + 1)
    heap = MinHeap()
    # insert into heap
    for edge in edges:
        heap.insert(edge)
    for i in range(1, n+1):
        clusters[i] = [i]
    while not heap.is_empty():
        edge = heap.extract_min()
        vert_1, vert_2 = edge[0], edge[1] 
        if clusters[vert_1] != clusters[vert_2]:
            rsum += edge[2]
            new_clust = clusters[vert_1] + clusters[vert_2]
            for vertex in new_clust:
                clusters[vertex] = new_clust 
    return rsum
            

if __name__ == "__main__":
    n = 4
    edges = [[1, 2, 1], [3, 2, 150], [4, 3, 99], [1, 4, 100], [3, 1, 200]]
    result = mst(n, edges)
    print(edges)
    print(result)