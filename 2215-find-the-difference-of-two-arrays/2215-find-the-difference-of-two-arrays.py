class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        answer = [[],[]]
        n1 =len(nums1)
        n2 = len(nums2)
        n = max(n1,n2)
        for i in range(n):
            if i < n1 and nums1[i] not in answer[0] and nums1[i] not in nums2:
                answer[0].append(nums1[i])
            if i < n2 and nums2[i] not in answer[1] and nums2[i] not in nums1:
                answer[1].append(nums2[i])
                
        return answer