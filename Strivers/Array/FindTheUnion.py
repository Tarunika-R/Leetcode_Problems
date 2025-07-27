class Solution:
    def unionArray(self, nums1, nums2):
        list = []
        for i in range(len(nums1)): 
            if nums1[i] not in list:
                list.append(nums1[i])
        for j in range(len(nums2)):
            if nums2[j] not in list:
                list.append(nums2[j])
        return sorted(list)

        # # Alternatively, using set for union
        # return sorted(set(nums1 + nums2))
def main():
    nums1 = [3, 4, 6, 7, 9, 9]
    nums2 = [1, 5, 7, 8, 8]
    solution = Solution()
    result = solution.unionArray(nums1, nums2)
    print(result)

if __name__ == "__main__":
    main()
