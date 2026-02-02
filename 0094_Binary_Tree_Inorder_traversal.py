class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], []
        curr = root
        
        while curr or stack:
            # 1. Go as deep as possible to the left
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # 2. Pop the last node (Left/Root)
            curr = stack.pop()
            res.append(curr.val)
            
            # 3. Now move to the right child
            curr = curr.right
            
        return res
