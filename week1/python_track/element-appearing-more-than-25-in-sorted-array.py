class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return arr[0]
        result = 0
        percent = int(len(arr) * 0.25)
        count_map = {}

        for i in arr:
            count_map[i] = count_map.get(i, 0) + 1

        for key, count in count_map.items():
            if count > percent:
                result = key

        return result