class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        n = len(B)
        
        if n < 3:
            return 0

        total_sum = sum(B)

        if total_sum % 3 != 0:
            return 0

        target = total_sum // 3
        current_sum = 0
        first_part_count = 0
        ways = 0

        for i in range(n - 1):
            current_sum += B[i]

            if current_sum == 2 * target:
                ways += first_part_count

            if current_sum == target:
                first_part_count += 1

        return ways
        
