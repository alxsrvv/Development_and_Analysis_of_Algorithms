class Node:
    def __init__(self, val, space=1, l=None, r=None):
        self.left = l
        self.right = r
        self.space=space
        self.v = val
        if self.v == 0:
            self.space=0

    def display(self):
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.v
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.v
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.v
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.v
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
        
class Tree:
    def __init__(self):
        self.root = None

    def getroot(self):
        print(self.root.v)

    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if node.left==None:
            node.left=Node(val)
        elif node.left.space==0 and node.right==None:
            node.right=Node(val)
        else:
            if node.left.space:
                self._add(val, node.left)
            elif node.right.space:
                self._add(val, node.right)
        self.isspace(node)

    def newadd(self, array):
        self._newadd(array, self.root)

    def _newadd(self, array, node):
        if node.v!=0:
            self._newadd(array, node.left)
            node.v=array[0]
            del array[0]
            self._newadd(array, node.right)

    def isspace(self, node):
        if node.left!=None and node.right!=None:
            if node.left.space==0 and node.right.space==0:
                node.space=0

    def clean(self):
        if(self.root != None):
            self._clean(self.root)

    def _clean(self, node):
        if(node != None):
            if node.left!=None and node.left.v==0:
                node.left=None
            if node.right!=None and node.right.v==0:
                node.right=None
            self._clean(node.left)
            self._clean(node.right)
        
    def pathsum(self, s):
        return self.path_sum(self.root, s)

    def path_sum(self, node, s, l=[], finalans=[]):
        if (sum(l)+node.v)==s:
            l.append(node.v)
            if l not in finalans:
                finalans+=[l]
            if node.left!=None:
                self.path_sum(node.left, s, [])
        else:
            l.append(node.v)
            l2=l.copy()
            if node.left != None:
                self.path_sum(node.left, s, l, finalans)
                self.path_sum(node.left, s, [], finalans)
            if node.right != None:
                self.path_sum(node.right, s, l2, finalans)
                self.path_sum(node.right, s, [], finalans)
        return finalans

with open("input_10b.txt") as f:
    file=f.read()
    file = list(map(int, file.split()))

    NewTree = Tree()
    for i in file:
        NewTree.add(i)
    print('INPUT:')
    NewTree.root.display()

    l=[]
    for i in file:
        if i!=0:
            l.append(i)
    l.sort()
    
    NewTree.newadd(l)
    NewTree.clean()
    print('\nOUTPUT:')
    NewTree.root.display()
    wanted=(int(input('\nWANTED PATHSUM: ')))
    pathsums = NewTree.pathsum(wanted)
    if len(pathsums)==0:
        print ("THERE IS NO WAY TO GET THIS SUM.")
    else:
        print ("WAYS TO GET THIS SUM:")
        for i in pathsums:
            i=list(map(str, i))
            print('-'.join(i))