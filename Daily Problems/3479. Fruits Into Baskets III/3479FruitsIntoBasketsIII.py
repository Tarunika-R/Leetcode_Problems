class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        n = len(baskets)
        m = int(math.sqrt(n))
        section = (n + m - 1) // m
        count = 0
        maxV = [0] * section

        for i in range(n):
            maxV[i // m] = max(maxV[i // m], baskets[i])

        for fruit in fruits:
            unset = 1
            for sec in range(section):
                if maxV[sec] < fruit:
                    continue
                choose = 0
                maxV[sec] = 0
                for i in range(m):
                    pos = sec * m + i
                    if pos < n and baskets[pos] >= fruit and not choose:
                        baskets[pos] = 0
                        choose = 1
                    if pos < n:
                        maxV[sec] = max(maxV[sec], baskets[pos])
                unset = 0
                break
            count += unset
        return count