class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        def gen():
            acc = 0
            yield acc
            for c in s:
                acc = acc^( 1<<(ord(c)-97))
                yield acc
		# prefix xor accumulator: if ith bit is zero - there was even number of chr(i+96); if it is one - odd.
        d=[c for c in gen()]
		# accumulate result with dull popcount()
        ans=[(bin(d[l]^d[r+1]).count("1")<=2*k+1) for l,r,k in queries]

        return ans