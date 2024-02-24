class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        a, b, x, y, c = "", "", s[0], s[0], '1' 
        for i in s:
            if i != '9':
                x = i
                break
        if s[0] == '1':
            for i in s:
                if i not in ['0', '1']:
                    y = i
                    c = '0'
                    break
        for i in s:
            if i == x:
                a += '9'
            else:
                a += i
            if i == y:
                b += c
            else:
                b += i
        return int(a) - int(b)