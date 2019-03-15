visited = set()

def solve(matrix, start, end):

    global visited

    visited.add(start)

    x, y = start
    a, b = end 

    if start == end:
        return True
    
    possible_next = [(x + dx, y + dy) for dx in [-1, 0, 1] 
                                      for dy in [-1, 0, 1] 
                                      if (dx, dy) != (0, 0) and 
                                          x + dx >= 0 and y + dy >= 0]

    possible = []
    for x, y in possible_next:
        if  x < len(matrix[0]) and y < len(matrix)  \
            and matrix[x][y] and not (x, y) in visited:
            possible.append((x, y))

    for next_cell in possible:
        if solve(matrix, next_cell, end):
            return True       
    
    return False

# Case for matrix with solution

matrix = [
[True, False, True],
[True, False, True],
[True, True, True]
]

start = (0, 0)
end = (0, 2) 

assert solve(matrix, start, end) is True

# Case for matrix without solution

matrix = [
[True, False, True],
[True, False, True],
[True, False, True]
]

start = (0, 0)
end = (0, 2) 

assert solve(matrix, start, end) is False