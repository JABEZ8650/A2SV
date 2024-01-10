from itertools import groupby, zip_longest


class Solution:
	"""
	Time:   O(max(n, m))
	Memory: O(1)
	"""

	def isLongPressedName(self, name: str, typed: str) -> bool:
		for (a, a_gr), (b, b_gr) in zip_longest(groupby(name), groupby(typed), fillvalue=(None, None)):
			if a != b or sum(1 for _ in a_gr) > sum(1 for _ in b_gr):
				return False
		return True


class Solution:
	"""
	Time:   O(max(n, m))
	Memory: O(1)
	"""

	def isLongPressedName(self, name: str, typed: str) -> bool:
		return all(
			a == b and sum(1 for _ in a_gr) <= sum(1 for _ in b_gr)
			for (a, a_gr), (b, b_gr) in zip_longest(groupby(name), groupby(typed), fillvalue=(None, None))
		)