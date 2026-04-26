
    def dls(node, target, depth, visited, path):
        if node == target:
            return path
        if depth == 0:
            return None
        r, c = node
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols
                    and grid[nr][nc] == 0
                    and (nr, nc) not in visited):
                visited.add((nr, nc))
                result = dls((nr,nc), target, depth-1,
                              visited, path + [(nr,nc)])
                if result is not None:
                    return result
                visited.remove((nr, nc))
        return None

    for depth in range(max_depth + 1):
        visited = {start}
        result = dls(start, target, depth, visited, [start])
        if result is not None:
            return depth, result
    return None, []


def solve(grid, start, target):
    rows, cols = len(grid), len(grid[0])
    depth, path = iddfs_maze(grid, start, target)
    if path:
        fmt = ', '.join(f'({r},{c})' for r,c in path)
        print(f"Path found at depth {depth} using IDDFS")
        print(f"Traversal Order: [{fmt}]")
    else:
        print(f"Path not found at max depth "
              f"{rows*cols} using IDDFS")
