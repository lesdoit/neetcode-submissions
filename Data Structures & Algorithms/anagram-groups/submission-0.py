import copy as c

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        copy = []
        for idx, s in enumerate(strs): 
            copy.append([s, idx])
        
        for pair in copy: 
            sorted_s = "".join(sorted(list(pair[0])))
            pair[0] = sorted_s
        
        copy.sort(key=lambda x: x[0])

        i = 1
        ans = [] 
        curr = [copy[0]]
        while i < len(copy): 
            if copy[i][0] == copy[i-1][0]: 
                curr.append(copy[i])
            else:
                ans.append([strs[idx] for idx in [ curr[i][1] for i in range(len(curr))]])
                curr = [copy[i]]
            i += 1
        
        ans.append([strs[idx] for idx in [ curr[i][1] for i in range(len(curr))]])
        return ans
