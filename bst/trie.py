"""
Program for a challenge at hackerrank.com
We're going to make our own Contacts application! The application must perform two types of operations:

add name, where name is a string denoting a contact name. This must store name as a new contact in the application.
find partial, where partial is a string denoting a partial name to search the application for. 
It must count the number of contacts starting with partial and print the count on a new line.
"""
class Node:
    """Node class"""
    def __init__(self):
        self.children = {}
        self.valid = 0
        # store the number of children so we can count the number of
        # valid words faster
        self.num_children = 0
        
class Trie:
    """ a trie class, that allows insertion and lookup """
    def __init__(self):
        self.root = Node()

    def insert(self, name):
        ''' (self, str) -> None
        inserts a name as a trie
        '''
        current = self.root
        for letter in name:
            if current.children.get(letter) == None:
                node = Node() # create a new node
                current.children[letter] = node
            # update the number of children
            current.num_children += 1
            current = current.children[letter]
        current.valid = 1
        
    def search(self, name):
        """(self, str) -> int
        searches based on a string and returns
        the number of children that belong to the
        partial string """
        result = 0
        current = self.root
        for letter in name:
            find_node = current.children.get(letter)
            if find_node:
                current = find_node
            else:
                return 0
        # we found the right node
        return current.num_children + current.valid
        
        
if __name__ == "__main__":
    # main function
    tries = Trie()
    num = int(input().strip('\n'))
    for i in range(num):
        command = input().split()
        if command[0] == "add":
            tries.insert(command[1])
        elif command[0] == "find":
            print(tries.search(command[1]))
