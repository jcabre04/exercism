class Matrix:
    def __init__(self, matrix_string):
        rows = matrix_string.split("\n")
        self.matrix = []
        for row in rows:
        	row = list(map(int, row.split(" ")))
        	self.matrix.append(row)

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        column = []
        for row in self.matrix:
        	column.append(row[index - 1])
        return column
