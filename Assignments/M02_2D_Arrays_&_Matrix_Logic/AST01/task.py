#Task
from typing import List
def spiralMatrixIII(rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]: 
   directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
   result = [[rStart, cStart]]
   total_cells = rows * cols
    
   r, c = rStart, cStart
   step = 1
   d = 0
    
   while len(result) < total_cells:
      for _ in range(2):
         dr, dc = directions[d]
         for _ in range(step):
               r += dr
               c += dc
               if 0 <= r < rows and 0 <= c < cols:
                  result.append([r, c])
                  if len(result) == total_cells:
                     return result
         d = (d + 1) % 4
      step += 1
   

if __name__ == '__main__':
   rows,cols,rStart,cStart = map(int,input().split())
   print(spiralMatrixIII(rows,cols,rStart,cStart))
