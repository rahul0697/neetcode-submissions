class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows = len(grid)
        cols = len(grid[0])
        visited = []
        for _ in range(rows):
            temp = [0]*cols
            visited.append(temp)

        
        val = -1
        def bfs(r, c):

            q = deque()
            q.append((r,c,0))
            visited[r][c]=1

            while q:
                (r, c, level) = q.popleft()
                
                if grid[r][c]==0:
                    return level

                if r+1<rows and grid[r+1][c]!=-1 and visited[r+1][c]==0:
                    q.append((r+1, c, level+1))
                    visited[r+1][c]=1
                if r-1>=0 and grid[r-1][c]!=val and visited[r-1][c]==0:
                    q.append((r-1, c, level+1))
                    visited[r-1][c]=1
                if c+1<cols and grid[r][c+1]!=val and visited[r][c+1]==0:
                    q.append((r, c+1, level+1))
                    visited[r][c+1]=1
                if c-1>=0 and grid[r][c-1]!=val and visited[r][c-1]==0:
                    q.append((r, c-1, level+1))
                    visited[r][c-1]=1

                



        for r in range(rows):
            for c in range(cols):
                if  grid[r][c]==2147483647:
                    grid[r][c] = bfs(r, c)
                for i in range(rows):
                    for j in range(cols):
                        visited[i][j]=0




