class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        sum0 = 0

        for j in J:
            sum0 = sum0 + S.count(j)
        return sum0

# Below is tesing
sol = Solution()
print(sol.numJewelsInStones('aA', 'aAAbbbb'))        