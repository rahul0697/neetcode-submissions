class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = []
        for _ in range(rows):
            temp = [0]*cols
            visited.append(temp)
        ans = 0 

        def dfs(r, c):
            
            visited[r][c]=1

            if r+1<rows and grid[r+1][c]=="1" and visited[r+1][c]==0:
                dfs(r+1, c)
            if r-1>=0 and grid[r-1][c]=="1" and visited[r-1][c]==0:
                dfs(r-1, c)
            if  c+1<cols and grid[r][c+1]=="1" and visited[r][c+1]==0:
                dfs(r, c+1)
            if  c-1>=0 and grid[r][c-1]=="1" and visited[r][c-1]==0:
                dfs(r, c-1)
              





        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and visited[r][c]==0:
                    ans = ans + 1
                    dfs(r, c)

        return ans








        