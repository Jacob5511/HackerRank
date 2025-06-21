grid = [list(map(int, input().split())) for _ in range(20)]

max_product = 0

for i in range(20):
    for j in range(20):
        if j + 3 < 20:
            prod = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
            if prod > max_product:
                max_product = prod

        if i + 3 < 20:
            prod = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
            if prod > max_product:
                max_product = prod

        if i + 3 < 20 and j + 3 < 20:
            prod = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
            if prod > max_product:
                max_product = prod

        if i + 3 < 20 and j - 3 >= 0:
            prod = grid[i][j] * grid[i+1][j-1] * grid[i+2][j-2] * grid[i+3][j-3]
            if prod > max_product:
                max_product = prod

print(max_product)
