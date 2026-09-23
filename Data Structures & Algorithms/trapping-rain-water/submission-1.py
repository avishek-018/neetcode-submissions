class Solution:
    def trap(self, height: list[int]) -> int:
        
        maxL, maxR = 0, 0
        matL, matR = [0]*len(height), [0]*len(height)
        minLR = []
        solve = []
        for i in range(0,len(height)-1):
            maxL = max(maxL, height[i])
            matL[i+1] = maxL

        for i in range(len(height)-1, 0, -1):
            maxR = max(maxR, height[i])
            matR[i-1] = maxR

        for i,j in zip(matL, matR):
            minLR.append(min(i, j))

        for i, j in zip(minLR, height):
            if i>j:
                solve.append(i-j)
        
        return sum(solve)
        