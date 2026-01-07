max1 = float('-inf')  # max(A[i] + i)
        min1 = float('inf')   # min(A[i] + i)
        max2 = float('-inf')  # max(A[i] - i)
        min2 = float('inf')   # min(A[i] - i)

        for i in range(len(A)):
            val1 = A[i] + i
            val2 = A[i] - i

            max1 = max(max1, val1)
            min1 = min(min1, val1)

            max2 = max(max2, val2)
            min2 = min(min2, val2)

        return max(max1 - min1, max2 - min2)
