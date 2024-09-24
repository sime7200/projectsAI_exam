variables = [(r, c) for r in range(9) for c in range(9)]
domains = {
    (r, c): {1, 2, 3, 4, 5, 6, 7, 8, 9} for r in range(9) for c in range(9)
}

# Esempio di griglia iniziale con alcuni numeri già inseriti
initial_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Aggiorna i domini in base alla griglia iniziale
for r in range(9):
    for c in range(9):
        if initial_grid[r][c] != 0:
            domains[(r, c)] = {initial_grid[r][c]}

# Definisci gli edges (vincoli) per il sudoku
edges = []
for r in range(9):
    for c in range(9):
        for k in range(9):
            if k != c:
                edges.append(((r, c), (r, k)))  # Stessa riga
            if k != r:
                edges.append(((r, c), (k, c)))  # Stessa colonna

        # Stesso blocco 3x3
        block_row, block_col = 3 * (r // 3), 3 * (c // 3)
        for i in range(block_row, block_row + 3):
            for j in range(block_col, block_col + 3):
                if (i, j) != (r, c):
                    edges.append(((r, c), (i, j)))

print("Edges:", edges)
