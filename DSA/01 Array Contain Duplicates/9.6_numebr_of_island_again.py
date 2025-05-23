import collections

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        rows , cols = len(grid) , len(grid[0])
        visit = set()
        island = 0

        
        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            
            while q:
                row , col = q.popleft()
                direction = [[1,0] , [-1,0] ,[0,1] , [0,-1]]
                for dr , dc in direction:
                    r , c = row + dr , col + dc

                    if (r in range(rows) and
                        c in range(cols) and 
                        grid[r][c] == "1" and 
                        (r ,c ) not in visit):
                        q.append((r,c))
                        visit.add((r,c))
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    island += 1

        return island




                                              
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

sol = Solution()
print(sol.numIslands(grid))  # Output: 3

