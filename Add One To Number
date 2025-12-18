class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):

        i = 0
        while i < len(A) and A[i] == 0:
            i += 1
        A = A[i:] if i < len(A) else [0]  

       
        n = len(A)
        carry = 1 
        for i in range(n - 1, -1, -1):
            total = A[i] + carry
            A[i] = total % 10
            carry = total // 10

        if carry:
            A.insert(0, carry)

        return A
