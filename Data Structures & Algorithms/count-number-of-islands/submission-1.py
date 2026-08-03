class Solution:
    def is_safe ( self , i, j ,n, m ):
        return 0 <= i < n and 0 <= j < m

    def start_grinding(self, i ,j, n , m):
        print("function_call")
        p = 0
        self.grid[i][j] = "0"
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        for dir in directions:
            x = i + dir[0]
            y = j + dir[1]

            if self.is_safe(x , y, n, m ) and self.grid[x][y] == "1":
                self.start_grinding( x ,y, n , m)
            
            
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        n = len(grid)
        m = len(grid[0])
        no_of_islands = 0
        for i in range (0,n):
            for j in range (0,m):
                #print(f"N { n }, M { m } ")
                #print(grid[0])
                #print(grid[1])
                #print(grid[2])
                #print("")
                if self.grid[i][j] == "1":
                    no_of_islands = no_of_islands + 1
                    self.start_grinding( i, j , n, m)
                    
        return no_of_islands

