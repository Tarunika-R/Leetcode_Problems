class Solution(object):
    def maximumSwap(self, num):
        num_list = list(str(num))
        
        last = {int(n): i for i, n in enumerate(num_list)}
        
        for i in range(len(num_list)):
            for d in range(9, int(num_list[i]), -1):
                if last.get(d, -1) > i:
                    num_list[i], num_list[last[d]] = num_list[last[d]], num_list[i]
                    return int(''.join(num_list))
        
        return num        