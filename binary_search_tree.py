class Tree():
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    # insert new node at the correct position
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Tree(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Tree(data)
        else:
            self.data = data
            
    def findMinVal(self):
        if self.left:
            return self.left.findMinVal()
        else:
            return self.data

    def findMaxVal(self):
        if self.right:
            return self.right.findMaxVal()
        else:
             return self.data
            
    def delete(self, data):
        
        print(self.data)
        
        if not self :
            return None
            
        if self.data == data:            
            if not self.left and not self.right:
                return None
            elif not self.left and self.right:
                return self.right
            elif not self.right and self.left:
                return self.left
            elif self.right and self.left:
                pnt = self.right
                # find min value node in right child tree
                while pnt.left:
                    pnt = pnt.left
                self.data = pnt.data
                self.right = self.right.delete(self.data)
        
        elif data < self.data:
            self.left = self.left.delete(data)
            
        elif data > self.data:
            self.right = self.right.delete(data)
            
        return self
        
    def searchVal(self, data):
        
        if self.data == data:
            return self
        
        elif self.left and self.data < data:
            return self.left.searchVal(data)
        
        elif self.right and self.data > data:
            return self.right.searchVal(data)
        
        else:
            return None
    
    def printPreorder(self):
        print(self.data)
        if self.left:
            self.left.printPreorder()
        if self.right:
            self.right.printPreorder()
            
    def printInorder(self):
        if self.left:
            self.left.printInorder()
        print(self.data)
        if self.right:
            self.right.printInorder()
            
    def printPostorder(self):
        if self.left:
            self.left.printPostorder()
        if self.right:
            self.right.printPostorder()
        print(self.data)
        
    def printAllPaths(self):
        pass
    
    def checkIfBst(self):
        pass

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
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


# Example Usage
root = Tree(25)
root.insert(20)
root.insert(36)
root.insert(10)
root.insert(22)
root.insert(30)
root.insert(40)
root.insert(5)
root.insert(12)
root.insert(28)
root.insert(38)
root.insert(48)

# root.printPreorder()

# root.printInorder()

# root.printPostorder()

# print(root.findMinVal())

# print(root.findMaxVal())

# root.display()

root.delete(36)
root.display()
root.insert(36)
root.display()
root.delete(36)
root.display()
