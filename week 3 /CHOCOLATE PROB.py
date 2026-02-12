class Solution:
    def minDifference(self, arr, m):
        
        if m == 0 or len(arr) == 0:
            return 0
        
        arr.sort()
        n = len(arr)

        min_diff = float('inf')

        for i in range(n - m + 1):
            diff = arr[i + m - 1] - arr[i]
            min_diff = min(min_diff, diff)

        return min_diff
