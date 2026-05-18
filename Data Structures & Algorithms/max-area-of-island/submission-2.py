class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        visited = []
        for _ in range(rows):
            temp = [0]*cols
            visited.append(temp)
        
        ans = 0
        self.count = 0

        def dfs(r, c):
            visited[r][c]=1
            self.count = self.count+1

            if r+1<rows and grid[r+1][c]==1 and visited[r+1][c]==0:
                dfs(r+1, c)
            if r-1>=0 and grid[r-1][c]==1 and visited[r-1][c]==0:
                dfs(r-1, c)
            if c+1<cols and grid[r][c+1]==1 and visited[r][c+1]==0:
                dfs(r, c+1)
            if c-1>=0 and grid[r][c-1]==1 and visited[r][c-1]==0:
                dfs(r, c-1)

        
        for r in range(rows):
            for c in range(cols):
                self.count = 0
                if grid[r][c]==1 and visited[r][c]==0:
                    dfs(r, c)
                    print(self.count)
                    ans = max(ans , self.count)

        return ans