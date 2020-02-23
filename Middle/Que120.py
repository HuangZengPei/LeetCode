class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:return 0
        rows = len(triangle)
        if rows == 1:return triangle[0][0]
        for row in range(1,rows):
            columns = len(triangle[row])
            for column in range(columns):
                if column == 0:
                    triangle[row][column] += triangle[row-1][column]
                elif column == columns-1:
                    triangle[row][column] += triangle[row-1][column-1]
                else:
                    triangle[row][column] += min(triangle[row-1][column-1],triangle[row-1][column])
        return min(triangle[-1])