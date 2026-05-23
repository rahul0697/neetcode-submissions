class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        visited = []
        for _ in range(rows):
            temp = [0]*cols
            visited.append(temp)

        self.val = False
        def dfs(r, c , i, res):

            
            if res==word:
                print(res)
                self.val=True

            if r+1<rows and i+1<len(word) and board[r+1][c]==word[i+1] and visited[r+1][c]==0:
                visited[r+1][c]=1
                dfs(r+1, c, i+1,res+word[i+1])
                visited[r+1][c]=0

            if r-1>=0 and i+1<len(word) and board[r-1][c]==word[i+1] and visited[r-1][c]==0:
                visited[r-1][c]=1
                dfs(r-1, c, i+1, res+word[i+1])
                visited[r-1][c]=0

            if c+1<cols and i+1<len(word) and board[r][c+1]==word[i+1] and visited[r][c+1]==0:
                visited[r][c+1]=1
                dfs(r, c+1, i+1,  res+word[i+1])
                visited[r][c+1]=0

            if c-1>=0 and i+1<len(word) and board[r][c-1]==word[i+1] and visited[r][c-1]==0:
                visited[r][c-1]=1
                dfs(r, c-1,i+1, res+word[i+1])
                visited[r][c-1]=0

            
            
            







        for r in range(rows):
            for c in range(cols):
                if board[r][c]==word[0]:
                    visited[r][c]=1
                    dfs(r, c, 0 ,word[0])
                    visited[r][c]=0

        return self.val