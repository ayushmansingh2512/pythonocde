from collections import deque

class Solution:
    def numIslands(self,grid):
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        count = 0


        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c] = '0' #Mark as visted

            while q:
                row , col = q.popleft()
                for  dr, dc in [(1,0), (-1,0) ,(0,1),(0,-1)]:
                    nr,nc = row + dr , col +dc
                    if 0 <= nr <rows and 0 <= nc < cols and grid[nr][nc] == '1':
                        grid[nr][nc] = '0' # mark as visted


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    bfs(r, c)
                    count += 1

        return count
grid = [
  ['1', '1', '0', '0', '0'],
  ['1', '1', '0', '0', '0'],
  ['0', '0', '1', '0', '0'],
  ['0', '0', '0', '1', '1']
]

s = Solution()
print (s.numIslands(grid))  # Output: 3
