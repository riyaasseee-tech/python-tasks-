
list_a = [10, 20, 30, 40]
list_b = [1, 2, 3, 4]

interleaved = []

for i in range(len(list_a)):
    interleaved.append(list_a[i])
    interleaved.append(list_b[i])

print("Interleaved list:", interleaved)



products = [
    ("Sensor", 4, 150.0),
    ("Cable", 12, 25.0),
    ("Board", 3, 800.0)
]

total_value = 0
low_stock = []

for product_name, quantity, unit_price in products:
    value = quantity * unit_price
    total_value += value

    print(f"{product_name}: Value = {value:.2f}")

    if quantity < 5:
        low_stock.append(product_name)

print("Low-stock products:", low_stock)
print(f"Total inventory value: {total_value:.2f}")


readings = [8, 10, 20, 35, 51, 40]

converted_readings = [
    round(c * 9 / 5 + 32, 1)
    for c in readings
    if 10 <= c <= 50
]

print("Converted readings:", converted_readings)



values = [4, 4, 4, 2, 2, 7, 7, 4, 4, 9]

compressed = []

if values:
    current_value = values[0]
    count = 1

    for i in range(1, len(values)):
        if values[i] == current_value:
            count += 1
        else:
            compressed.append((current_value, count))
            current_value = values[i]
            count = 1

    compressed.append((current_value, count))

print("Compressed list:", compressed)


sales = [10, 20, 30, 40, 50, 60]
k = 3

averages = []

for i in range(len(sales) - k + 1):
    window_sum = 0

    for j in range(i, i + k):
        window_sum += sales[j]

    average = window_sum / k
    averages.append(round(average, 2))

print("Window averages:", [f"{avg:.2f}" for avg in averages])


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(matrix)
rotated = []

for j in range(n):
    row = []

    for i in range(n - 1, -1, -1):
        row.append(matrix[i][j])

    rotated.append(row)

print("Rotated matrix:")

for row in rotated:
    print(*row)



matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

zigzag = []

for i in range(len(matrix)):
    if i % 2 == 0:
        zigzag.extend(matrix[i])
    else:
        zigzag.extend(matrix[i][::-1])

print("Zigzag list:", zigzag)


matrix = [
    [0, 0, 5, 0],
    [0, 8, 0, 0],
    [3, 0, 0, 6]
]

sparse = []

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] != 0:
            sparse.append((i, j, matrix[i][j]))

print(sparse)


matrix_a = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix_b = [
    [7, 8],
    [9, 10],
    [11, 12]
]

rows_a = len(matrix_a)
cols_a = len(matrix_a[0])
rows_b = len(matrix_b)
cols_b = len(matrix_b[0])

if cols_a != rows_b:
    print("Error: Matrix dimensions are incompatible.")
else:
    product = []

    for i in range(rows_a):
        row = []

        for j in range(cols_b):
            total = 0

            for k in range(cols_a):
                total += matrix_a[i][k] * matrix_b[k][j]

            row.append(total)

        product.append(row)

    print("Product matrix:")

    for row in product:
        print(*row)

    
matrix = [
    [3, 3],
    [1, 3],
    [2, 5],
    [4, 1]
]

rows = len(matrix)
cols = len(matrix[0])

dp = [[0] * cols for _ in range(rows)]
parent = [[None] * cols for _ in range(rows)]

dp[0][0] = matrix[0][0]

for i in range(1, rows):
    dp[i][0] = dp[i - 1][0] + matrix[i][0]
    parent[i][0] = (i - 1, 0)

for j in range(1, cols):
    dp[0][j] = dp[0][j - 1] + matrix[0][j]
    parent[0][j] = (0, j - 1)

for i in range(1, rows):
    for j in range(1, cols):
        if dp[i - 1][j] > dp[i][j - 1]:
            dp[i][j] = dp[i - 1][j] + matrix[i][j]
            parent[i][j] = (i - 1, j)
        else:
            dp[i][j] = dp[i][j - 1] + matrix[i][j]
            parent[i][j] = (i, j - 1)

path = []
i = rows - 1
j = cols - 1

while True:
    path.append(matrix[i][j])

    if parent[i][j] is None:
        break

    i, j = parent[i][j]

path.reverse()

print("Maximum path sum:", dp[rows - 1][cols - 1])
print("Path:", path)