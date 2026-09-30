# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        if not root:
            return []
        #Base Case
        if not root.left and not root.right:
            return [str(root.val)]

        ans=[]
        for left_path in self.binaryTreePaths(root.left):
            ans.append(f"{root.val}->{left_path}")

        for right_path in self.binaryTreePaths(root.right):
            ans.append(f"{root.val}->{right_path}")

        return ans

        