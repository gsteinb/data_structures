'''
Coding Challenge from hackerrank
Except for the GetHeight function code was written by team at hackerrank
and the user @vatsalchanana
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
    
    def getHeight(self,root):
        '''gets the height of BST where height is defined as the number of 
        edges between root and lowest leaf
        Node -> Int
        '''
        #Write your code here
        if not root:
            return -1
        left_height = 1 + self.getHeight(root.left)
        right_height = 1 + self.getHeight(root.right)
        result_height = left_height
        if right_height > result_height:
            result_height = right_height
        return result_height
        
T= [3,5,2,1,4,6,7]
myTree=Solution()
root=None
for i in range(len(T)):
        root=myTree.insert(root, T[i])
height=myTree.getHeight(root)
print(height)