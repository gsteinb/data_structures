import sys


'''
levelOrder which was written by github user gsteinb for the coding challenge at hackerrank
code prints the levelOrder of a BST where the Node class and the rest of Solution was written
by the team at hackerrank
'''
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
    
    def levelOrder(self,root):
        #Write your code here
        queue = [root]
        rstr = ''
        while queue:
            node = queue.pop(0)
            rstr += str(node.data) + ' '
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print(rstr)
        
T= [3,5,4,7,2,1]
myTree=Solution()
root=None
for i in range(len(T)):
    data= T[i]
    root=myTree.insert(root,data)
myTree.levelOrder(root)
