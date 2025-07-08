class Solution:
    def robotWithString(self, s):
        t = []         # robot's stack
        result = []    # final written string
        n = len(s)
        
        min_suffix = [''] * n
        min_suffix[-1] = s[-1]
        for i in range(n - 2, -1, -1):
            min_suffix[i] = min(s[i], min_suffix[i + 1])
        
        i = 0
        for c in s:
            t.append(c)
            while t and (i == n - 1 or t[-1] <= min_suffix[i + 1]):
                result.append(t.pop())
            i += 1
        
        while t:
            result.append(t.pop())
        
        return ''.join(result)
