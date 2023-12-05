class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        #creat a dictionary numbers as key and words as a value
        dicti={}
        for i in range(len(s)):
            dicti[indices[i]]=s[i]

        #sort the dictionary by key
        sorted_dict=dict(sorted(dicti.items()))
        
        #ceate a string for output
        output_str=""

        #putting the values in string
        for i in range(len(s)):
            output_str+=str(sorted_dict[i])
        return output_str