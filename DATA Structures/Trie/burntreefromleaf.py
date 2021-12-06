class TreeNode:
    def __init__(self, x) -> None:
        self.val = x
        self.left = None
        self.right = None

class Info:
    def __init__(self):
        self.ldepth = 0
        self.rdepth = 0
        self.contains = False
        self.time = -1

class Solution:
    res = 0
    
    def calcTime(self, node, info, target):
        if not node:
            return info
        
        if not node.left and not node.right:
            if node.val == target:
                info.contains = True
                info.time = 0
            return info
        
        leftinfo = Info()
        leftinfo = self.calcTime(node.left, leftinfo, target)

        rightinfo = Info()
        rightinfo = self.calcTime(node.right, rightinfo, target)

        if node.left and leftinfo.contains:
            info.time = leftinfo.time + 1
        else:
            info.time = -1
        
        if info.time == -1:
            if node.right and rightinfo.contains:
                info.time = rightinfo.time + 1
            else:
                info.time = -1
        
        info.contains = (node.left and leftinfo.contains) or (node.right and rightinfo.contains)
        info.ldepth = 0 if (not node.left) else (1 + max(leftinfo.ldepth, leftinfo.rdepth))
        info.rdepth = 0 if (not node.right) else(1 + max(rightinfo.ldepth, rightinfo.rdepth))

        if info.contains:
            if node.left and leftinfo.contains:
                self.res = max(self.res, info.time + info.rdepth)
            if node.right and rightinfo.contains:
                self.res = max(self.res, info.time + info.ldepth)

        return info

    def solve(self, root, target):
        info = Info()
        self.calcTime(root, info, target)
        return self.res

if __name__ == '__main__':
    # Construct tree shown in the above example
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.left.left.left = TreeNode(8)
    root.left.right.left = TreeNode(9)
    root.left.right.right = TreeNode(10)
    root.left.right.left.left = TreeNode(11)
 
    # Target Leaf Node
    target = 11
 
    # Print min time to burn the complete tree
    s = Solution()
    print(s.solve(root, target))