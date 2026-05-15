class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        r = len(grid)
        c = len(grid[0])
        visited = [[0]*c for _ in range(r)]

        
        count = 0
        def dfs(i , j):
            visited[i][j]=1
            
            if i+1<r and grid[i+1][j]=='1' and visited[i+1][j]==0:
                dfs(i+1, j)
            if j-1>=0 and grid[i][j-1]=='1' and visited[i][j-1]==0:
                dfs(i, j-1)
            if i-1>=0 and grid[i-1][j]=='1' and visited[i-1][j]==0:
                dfs(i-1, j)
            if j+1<c and grid[i][j+1]=='1' and visited[i][j+1]==0:
                dfs(i, j+1)






        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1' and visited[i][j]==0:
                    count = count + 1
                    dfs(i,j)

        return count
