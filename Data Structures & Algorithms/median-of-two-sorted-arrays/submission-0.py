class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = len(nums1)
        y = len(nums2)
        if x > y:
            nums1, nums2 = nums2, nums1
            x, y = y, x
        
        lo, hi = 0, x
        while lo <= hi:
            midx = lo + (hi - lo)//2
            midy = (x + y + 1)//2 - midx

            maxleftx = float('-inf') if midx == 0 else nums1[midx-1]
            maxlefty = float('-inf') if midy == 0 else nums2[midy-1]

            minrightx = float('inf') if midx == x else nums1[midx]
            minrighty = float('inf') if midy == y else nums2[midy]
            
            if maxleftx <= minrighty and maxlefty <= minrightx:
                # we found the partition in the combined array
                if (x + y) % 2 == 0:
                    return (max(maxleftx, maxlefty) + min(minrightx, minrighty))/2.0
                else:
                    return max(maxleftx, maxlefty)
            elif maxleftx > minrighty:
                # value of midx is too far right. bring it to the left 
                hi = midx - 1
            else:
                # value of midx is too far left. bring it to right
                lo = midx + 1
        
        # there is a problem with our logic or the input is wrong
        raise Exception
        return -1
