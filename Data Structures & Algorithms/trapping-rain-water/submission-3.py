class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height)-1
        maxL, maxR = height[left], height[right]
        area = 0

        while left<right:
            if maxL<=maxR:
                left+=1

                area+=max(0, maxL-height[left])
                maxL = max(maxL, height[left])
            else:
                right-=1
                area+=max(0, maxR-height[right])
                maxR = max(maxR, height[right])
            

        
            
        return area
        