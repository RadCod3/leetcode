# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flattened_list = self.flatten(nestedList)
        self.i = 0
        self.n = len(self.flattened_list)

    def flatten(self, nestedList):
        temp = []
        for num in nestedList:
            if num.isInteger():
                temp.append(num.getInteger())
            else:
                temp += self.flatten(num.getList())
        return temp

    def next(self) -> int:
        self.i += 1
        return self.flattened_list[self.i - 1]

    def hasNext(self) -> bool:
        if self.i < self.n:
            return True
        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
