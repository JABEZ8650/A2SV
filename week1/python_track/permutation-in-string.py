class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mapper = {chr(i):0 for i in range(ord('a'),ord('z')+1)}
        def __mapper():
            nonlocal mapper
            for i in s1:
                mapper[i] += 1
        __mapper()
        def __verify(s):
            nonlocal mapper
            copy = mapper.copy()
            for i in s:
                if i not in copy.keys():
                    return False
                elif copy[i] == 0:
                    return False
                else:
                    copy[i] -= 1
            return True
        def __helper():
            nonlocal mapper
            window = len(s1)
            for i in range(len(s2)-len(s1)+1):
                if __verify(s2[i:i+window]):
                    return True
            return False
        return __helper()