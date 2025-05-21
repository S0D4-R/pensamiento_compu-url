matrix_1 = [
 [0,0,0,0,0,0,0,1,1,0],
 [0,1,1,0,0,0,0,0,0,0],
 [0,1,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,1,1,0,0,0],
 [0,0,0,0,0,1,1,0,0,0],
 [0,0,1,1,0,0,0,0,0,0],
 [0,0,1,1,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,1,0],
]

def next_generation(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    
    new_matrix = []
    for _ in range(rows):
        new_row = []
        for _ in range(cols):
            new_row.append(0)
        new_matrix.append(new_row)

    
    for i in range(rows):
        for j in range(cols):
            live_neighbors = 0

            for x in range(max(0, i - 1), min(rows, i + 2)):
                for y in range(max(0, j - 1), min(cols, j + 2)):
                    if (x, y) != (i, j) and matrix[x][y] == 1:
                        live_neighbors += 1

            if matrix[i][j] == 1:
                if live_neighbors == 1 or live_neighbors == 2:
                    new_matrix[i][j] = 1
            else:
                if live_neighbors == 1:
                    new_matrix[i][j] = 1

    return new_matrix


n_generaciones = 10

 
current = matrix_1
for gen in range(n_generaciones):
    print(f"Generación {gen + 1}:")
    for row in current:
        line = ""
        for cell in row:
            line += str(cell)
        print(line)
    print()
    current = next_generation(current)