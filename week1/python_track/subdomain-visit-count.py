class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = {}
        for domain in cpdomains:
            number, website = domain.split()
            number = int(number)
            index = []
            count[website] = count.get(website, 0) + number
            for i, char in enumerate(website):
                if char == '.':
                    index.append(website[i+1:])
            for j in index:
                count[j] = count.get(j, 0) + number
        ans = []
        for key, value in count.items():
            s = str(value) + ' ' + key
            ans.append(s)

        return ans