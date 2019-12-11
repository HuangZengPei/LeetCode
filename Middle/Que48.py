class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        原地旋转图像
        """
        n = len(matrix[0])
        # 首先转置矩阵
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        # 之后将每一行再反转
        for i in range(n):
            matrix[i].reverse()
