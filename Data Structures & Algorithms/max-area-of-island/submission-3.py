class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        rows = len(grid)
        cols = len(grid[0])
        visited=[]
        for _ in range(rows):
            temp = [0]*cols
            visited.append(temp)
        ans = 0
        def bfs(r, c, count):
            
            q = deque()
            visited[r][c]=1
            q.append((r, c))
            
            while q:
                row, col = q.popleft()
                count = count+1

                if row+1<rows and grid[row+1][col]==1 and visited[row+1][col]==0:
                    visited[row+1][col]=1
                    q.append((row+1, col))

                if row-1>=0 and grid[row-1][col]==1 and visited[row-1][col]==0:
                    visited[row-1][col]=1
                    q.append((row-1, col))

                if col+1<cols and grid[row][col+1]==1 and visited[row][col+1]==0:

                    visited[row][col+1]=1
                    q.append((row, col+1))
                if col-1>=0 and grid[row][col-1]==1 and visited[row][col-1]==0:

                    visited[row][col-1]=1
                    q.append((row, col-1))

            return count

        for r in range(rows):
            for c in range(cols):
                if visited[r][c]==0 and grid[r][c]==1:
                    count = bfs(r, c, 0)
                    ans = max(ans, count)

        return ans
