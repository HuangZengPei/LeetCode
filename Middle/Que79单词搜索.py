class Solution(object):
    
    directions = [(0,-1),(-1,0),(0,1),(1,0)]
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not word :return False
        m = len(board)
        n = len(board[0])
        
        def backtrack(board,word,index,x,y,marked,m,n):
            # 递归终止条件
            if index ==len(word) - 1:
                return board[x][y] == word[index]
                
            if board[x][y] == word[index]:
                marked[x][y] = True           # 先占柱位置，搜索不成功释放掉
                for direction in self.directions:
                    new_x = x + direction[0]
                    new_y = y + direction[1]
                    if 0 <= new_x < m and 0 <= new_y < n and \
                    not marked[new_x][new_y] and backtrack(board,word,index+1,new_x,new_y,marked,m,n):
                        return True
                marked[x][y] = False
            return False

        marked = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if backtrack(board,word,0,i,j,marked,m,n):
                    return True
        return False
        
        
        
        
                    
        