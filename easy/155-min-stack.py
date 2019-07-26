
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
#  https://leetcode.com/problems/min-stack/


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

        self._update_min()

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()

        self._update_min()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min

    def _update_min(self):
        try:
            self.min = min(self.stack)
        except ValueError:
            pass


class MinStack2(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None
        self.action_pop = 0
        self.action_push = 1

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        self._update_min(x, self.action_push)

    def pop(self):
        """
        :rtype: None
        """
        n = self.stack.pop()
        self._update_min(n, self.action_pop)

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min

    def _update_min(self, n: int, action: int):
        if action == self.action_push:
            if not self.min or self.min > n :
                self.min = n
        elif action == self.action_pop:
            if self.min and self.min == n:
                try:
                    self.min = min(self.stack)
                except ValueError:
                    pass
            else:
                self.min = n


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
