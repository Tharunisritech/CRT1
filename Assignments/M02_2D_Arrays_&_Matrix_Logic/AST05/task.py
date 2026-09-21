from typing import List
def diagonalBoundarySum(arr):
    n = len(arr)
    elements = set()
    
    for i in range(n):
        elements.add((0, i))
        elements.add((n - 1, i))
        elements.add((i, 0))
        elements.add((i, n - 1))
        elements.add((i, i))
        elements.add((i, n - 1 - i))
        
    return sum(arr[r][c] for r, c in elements)

if __name__ == '__main__':
    n = int(input())
    mat = []
    for i in range(n):
        mat.append(list(map(int, input().split())))
    print(diagonalBoundarySum(mat))