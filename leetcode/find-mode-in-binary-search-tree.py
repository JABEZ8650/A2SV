
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        # Initialize variables
        self.mode_count = 0
        self.current_val = None
        self.current_count = 0
        self.mode_list = []
        
        def update_mode_list(val):
            if self.current_count > self.mode_count:
                self.mode_count = self.current_count
                self.mode_list = [val]
            elif self.current_count == self.mode_count:
                self.mode_list.append(val)
        
        def traverse(node):
            if node is None:
                return
            traverse(node.left)
            if node.val == self.current_val:
                self.current_count += 1
            else:
                update_mode_list(self.current_val)
                self.current_val = node.val
                self.current_count = 1
            traverse(node.right)
        traverse(root)
        update_mode_list(self.current_val)
        return self.mode_list
    



