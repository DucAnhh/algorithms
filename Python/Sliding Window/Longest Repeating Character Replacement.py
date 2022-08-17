class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # the solution of video
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            print(count)
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]]) # maxf is the number of the most frequence character

            if (r - l + 1) - maxf > k: # the valid condition: len(sliding window) - maxf < k
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res

s = "CCBABBA"
k = 1
a = Solution()
print(a.characterReplacement(s, k))