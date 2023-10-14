class Solution:
    def minEatingSpeed(self, piles, h):
        l=1
        r=max(piles)
        while l<r:
            mid=(l+r)//2
            c=0
            for j in piles:
                c+=((j-1)//mid)+1
            if c>h:
                l=mid+1
            else:
                r=mid
        return l