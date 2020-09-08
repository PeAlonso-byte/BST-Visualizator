# https://leetcode.com/problems/recover-binary-search-tree/discuss/32539/Tree-arrayToBSTr-and-Visualizer-for-Python
import turtle
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return 'Node({})'.format(self.val)

###########################################################
#                       UTILITIES                         #
###########################################################

def arrayToBST(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else Node(int(val))
             for val in string.strip('[]{}').split(',')]
    arrayNodes = nodes[::-1]
    # print(arrayNodes)
    root = arrayNodes.pop()
    for node in nodes:
        if node:
            if arrayNodes: insert(root, arrayNodes.pop())
    return root

def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node)


###########################################################
#                   TRAVERSAL ALGORITHMS                  #
###########################################################

def inorder(node):
    if node: 
        inorder(node.left) 
        print(node.val) 
        inorder(node.right) 
def preorder(node):
    if node:
        print(node.val)
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.val)

############################################################
############################################################
    
# w is the width to draw the bst             
def drawtree(root, w):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else w

    def lineTo(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
    # node -> Node to draw
    # x, y -> Coord of the node
    # dx   -> Space between inline nodes.
    def draw(node, x, y, dx, bgColor, txtColor):
        if node:
            t.goto(x, y)
            lineTo(x-15, y-25)      
            t.fillcolor(bgColor)
            t.begin_fill()
            t.color(bgColor)
            t.circle(17)
            t.end_fill()
            t.color(txtColor)
            t.write(node.val, align='center', font=('Arial', 14, 'bold'))
            t.color(bgColor)
            # RECURSIVE DRAWING
            draw(node.left, x-dx, y-50, dx/2, bgColor, txtColor)
            lineTo(x-7, y-20)
            draw(node.right, x+dx, y-50, dx/2, bgColor, txtColor)
            
    t = turtle.Turtle()
    t.speed(2); turtle.delay(1)
    h = height(root)
    lineTo(0, 30*h)
    draw(root, 0, 30*h, 30*h, "green", "white")
    t.hideturtle()
    turtle.mainloop()

if __name__ == '__main__':
    #root = arrayToBST('[50,30,20,40,70,60,80,25,65,10,15,55,45]')
    root = arrayToBST('[27,14,10,19,35,31,42]')
    
    print("##### INORDER #####")
    inorder(root)
    print("##### PREORDER #####")
    preorder(root)
    print("##### POSTORDER #####")
    postorder(root)

    drawtree(root, -1)