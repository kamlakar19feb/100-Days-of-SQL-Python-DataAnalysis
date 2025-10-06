Matrix addition using nested lists

Input: two 2×2 matrices → Output: sum of matrices

matrix1=[]
matrix2=[]
for i in range(0,2):
  row1=list(map(int, input("Enter 2 space separated numbers for row1: ").split()))
  matrix1.append(row1)
print(matrix1)
for j in range(0,2):
  row2=list(map(int, input("Enter 2 space separated numbers for row2: ").split()))
  matrix2.append(row2)
print(matrix2)
sum_matrix=[]
for i in range(0,2):
  row_sum=[]
  for j in range(0,2):
    row_sum.append(matrix1[i][j]+matrix2[i][j])
  sum_matrix.append(row_sum)
print(sum_matrix)
