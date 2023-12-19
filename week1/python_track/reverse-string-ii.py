class Solution:
    def reverseStr(self, s: str, k: int):

        def reverse_word(x): return x[::-1]

        final_string = ""
        if len(s) <= k:
            final_string = reverse_word(s)
            return final_string

        stack_non_reversed: list = []
        stack_reversed: list = []
        stack_final: list = []

        for i in range(0, len(s), 2*k):
            temp = s[i:i+k]
            stack_non_reversed.append(temp)

        for item in stack_non_reversed:
            stack_reversed.append(reverse_word(item))

        stack_non_reversed.clear()

        for i in range(k, len(s), 2*k):
            temp = s[i:i+k]
            stack_non_reversed.append(temp)

        for i, item in enumerate(stack_reversed):
            stack_final.append(item)
            if i > len(stack_non_reversed)-1:
                continue
            stack_final.append(stack_non_reversed[i])

        for item in stack_final:
            final_string += item

        return final_string