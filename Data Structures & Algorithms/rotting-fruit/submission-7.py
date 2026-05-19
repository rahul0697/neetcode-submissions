class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = []
        for _ in range(rows):
            temp = [0]*cols
            visited.append(temp)

        q = deque()
        ans = 0
        print(rows, cols)

        for r in range(rows):
            for c in range(cols):
                print(r, c)
                if grid[r][c]==2:
                    q.append((r,c,0))
                    visited[r][c]=1

            # print(q)
        while q:
            r, c, minute = q.popleft()
            ans = max(minute, ans)
            print(r, c , minute)
            if r+1<rows and grid[r+1][c]==1 and visited[r+1][c]==0:
                q.append((r+1,c,minute+1))
                visited[r+1][c]=1
                grid[r+1][c]=2
            if r-1>=0 and grid[r-1][c]==1 and visited[r-1][c]==0:
                q.append((r-1, c, minute+1))
                visited[r-1][c]=1
                grid[r-1][c]=2
            if c+1<cols and grid[r][c+1]==1 and visited[r][c+1]==0:
                q.append((r, c+1,minute+1))
                visited[r][c+1]=1
                grid[r][c+1]=2
            if c-1>=0 and grid[r][c-1]==1 and visited[r][c-1]==0:
                q.append((r, c-1, minute+1))
                visited[r][c-1]=1
                grid[r][c-1]=2

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    return -1

        return ans

                