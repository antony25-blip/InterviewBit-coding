class Solution:
	# @param A : string
	# @return a strings
	def longestPalindrome(self, A):
        def expand(l,r):
            while l>-1 and r<len(A) and A[l]==A[r]:
                l-=1
                r+=1
            return A[l+1:r]
        ms=A[0]
        for i in range(len(A)):
            p1=expand(i,i)
            if len(p1)>len(ms):
                ms=p1
            p2=expand(i,i+1)
            if len(p2)>len(ms):
                ms=p2
        return ms
                
