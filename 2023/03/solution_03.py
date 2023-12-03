import re

with open("input_03.txt", "r") as f:
    matrix = f.read().splitlines()

    rows = len(matrix)
    cols = len(matrix[0])
    
    mask = [[0 for col in range(cols)] for row in range(rows)]

    for r, row in enumerate(matrix):
        for c, _ in enumerate(row):
            if re.match("[^\.\d]", matrix[r][c]):
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        mask[i][j] = 1

    parts_sum = 0
    
    for r, row in enumerate(matrix):
        matches = re.finditer("\d+", row)

        for m in matches:
            overlap = False
            for c in range(m.start(), m.end()):
                if mask[r][c]:
                    overlap = True
                    break

            if overlap:
                parts_sum += int(m[0])

    print(parts_sum)
