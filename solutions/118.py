
METHOD = "generate"

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            if i == 0:
                result.append([1])
                continue
            row = [1]
            prev_row = result[i-1]
            for j in range(1,i):
                row.append(prev_row[j] + prev_row[j-1])
            row.append(1)
            result.append(row)
        return result