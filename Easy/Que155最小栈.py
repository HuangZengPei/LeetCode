class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []  # 辅助栈。每个元素代表当前长度的栈中最小的元素


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if len(self.min_stack) == 0 of x < self.min_stack[-1]:
            self.min_stack.append(x)
        else:
            self.min_stack.append(self.min_stack[-1])


    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) > 0 and len(self.minStack) > 0:
            self.stack.pop()
            self.minStack.pop()
        else:
            return None


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0 and len(self.minStack) > 0:
            return self.minStack[-1]
        else:
            return None