class Node:
    def __init__(self):
        self.children = {}
        self.valid = 0
        self.num_children = 0
        
class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, name):
        current = self.root
        for letter in name:
            if current.children.get(letter) == None:
                node = Node() # create a new node
                current.children[letter] = node
            current.num_children += 1
            current = current.children[letter]
        current.valid = 1
        
    def search(self, name):
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
    tries = Trie()
    num = int(input().strip('\n'))
    for i in range(num):
        command = input().split()
        if command[0] == "add":
            tries.insert(command[1])
        elif command[0] == "find":
            print(tries.search(command[1]))
