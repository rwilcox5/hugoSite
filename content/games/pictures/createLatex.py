sudoku = "123456789"
rowStr = "\setrow "
for i in sudoku:
	if i == ".":
		rowStr+="{ }"
	else:
		rowStr += "{"+i+"}"
print(rowStr)