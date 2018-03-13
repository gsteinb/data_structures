import time

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

def prims(n, edges, start):
    '''finds the weight of the MST starting at a specified vertex
    @param n-> number of vertices
    @param edges -> list of edges in the graph (these are directed edges,
    as prims will add the mirror edge to make it undirected)
    @param start-> the node at which to construct the MST
    >>>prims(5, [[1, 2, 3], [1, 3, 4], [4, 2, 6], [5, 2, 2]], 1)
    15
    '''
    visited = [0] * n 
    psum = 0
    # create an adjacency list
    adj = []
    for i in range(0, n+1):
        adj.append([])
    for edge in edges:
        adj[edge[0]].append(edge)
        # add the same edge to the end vertex
        new_edge = [edge[1], edge[0], edge[2]]
        # reverse the edges
        adj[new_edge[0]].append(new_edge)
    # create a MinHeap
    min_heap = MinHeap()
    # init MinHeap
    for edge in adj[start]:
        min_heap.insert(edge)
    visited[start - 1] = 1
 
    while not min_heap.is_empty():
        min_weight = min_heap.extract_min()
        # only runs if we have not visited the vertex
        if not visited[min_weight[1] - 1]:
            psum += min_weight[2]
            for edge in adj[min_weight[1]]:
                min_heap.insert(edge)
        # mark the vertex as visited
        visited[min_weight[1] - 1] = 1
    return psum

if __name__ == "__main__":
    start_time = time.time()
    print(prims(5, [[1, 2, 3], [1, 3, 4], [4, 2, 6], [5, 2, 2], [2, 3, 5], [3, 5, 7]], 1))
    print("{} seconds".format(time.time() - start_time))
