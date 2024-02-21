class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sums = [sum(line) for line in accounts]
        return max(sums)