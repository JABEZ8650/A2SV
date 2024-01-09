class Solution:
    def intervalIntersection(self, A, B):
        ans, i, j = [], 0, 0
        while i < len(A) and j < len(B):
            if A[i][1] >= B[j][0] and A[i][0] <= B[j][1]:
                ans.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
            if A[i][1] < B[j][1]: i += 1
            else: j += 1
        return ans