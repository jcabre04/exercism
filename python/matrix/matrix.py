class Matrix:
    def __init__(self, matrix_string):
        rows = matrix_string.splitlines()
        self.matrix = [[int(num) for num in row.split(" ")] for row in rows]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        column = []
        for row in self.matrix:
        	column.append(row[index - 1])
        return column
