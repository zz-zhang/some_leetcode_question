'''
if target and arr have the same items, by swaping adjacent items (like bubble sorting), arr could be target
'''

class Solution:
    def canBeEqual(self, target, arr):
        target = sorted(target)
        arr = sorted(arr)
        for item1, item2 in zip(target, arr):
            if item1 != item2:
                return False
        return True
        