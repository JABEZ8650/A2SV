class Solution:
    def numberOfWays(self, s: str) -> int:
        zeros = ones = 0
        before = []
        for i in range(len(s)):
            if s[i] == '0':
                before.append(ones)
                zeros += 1
            else:
                before.append(zeros)
                ones += 1
        zeros = ones = 0
        after = []
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                after.append(ones)
                zeros += 1
            else:
                after.append(zeros)
                ones += 1
        ans = 0
        for i, j in zip(before, after[::-1]):
            ans += i * j
        return ans