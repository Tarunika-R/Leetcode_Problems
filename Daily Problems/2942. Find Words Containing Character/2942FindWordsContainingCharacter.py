class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        output = []
        for i, w in enumerate(words):   # for index, element in enumerate(my_list):
            if x in w:
                output.append(i)
        return(output)