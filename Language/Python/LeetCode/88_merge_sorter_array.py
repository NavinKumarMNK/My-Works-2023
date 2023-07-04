class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        m = m-1
        n = n-1
        t = m + n + 1
        while n >= 0 and m>=0:
            if nums1[m] < nums2[n]:
                nums1[t] = nums2[n]
                n-=1
            else:
                nums1[t] = nums1[m]
                m-=1
            t-=1
        
        while n >=0:    
            nums1[t] = nums2[n]
            n-=1 
            t-=1
        else:
            while m >=0:
                nums1[t] = nums1[m]
                m-=1
                t-=1