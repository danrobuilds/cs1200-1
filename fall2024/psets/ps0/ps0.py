#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        """
        :param root: the root of the binary tree
        """
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        """
        :param: the key associated with the vertex of the binary tree
        """
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None


#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):

    if not v:
        return 0

    left = calculate_sizes(v.left)
    right = calculate_sizes(v.right)

    v.size = left + right + 1

    return v.size
    
    pass 


#
# Problem 1c
#

# Input: a positive integer t, 
# ...BTvertex v, the root of a BinaryTree of size n >= 1
# Output: BTvertex, descendent of v such that its size is between 
# ... t and 2t (inclusive)
# Runtime: O(h) 

def FindDescendantOfSize(t, v):

    if v.left and v.left.size >= t and v.left.size <= 2*t:
        return v.left

    if v.right and v.right.size >= t and v.right.size <= 2*t:
        return v.right

    if v.left and v.left.size >= t:
        res = FindDescendantOfSize(t, v.left)
    elif v.right and v.right.size >= t:
        res = FindDescendantOfSize(t, v.right)
    
    if res:   
        return res
    else:
        return None

    pass 