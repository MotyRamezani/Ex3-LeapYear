import numpy as np

vec1 = np.array([ -1., 4., -9.])
mat1 = np.array([[ 1., 3., 5.], [7., -9., 2.], [4., 6., 8. ]])

print("****************************** Q.01 ******************************","\n")
vec2 = (np.pi/4) * vec1
print("vec2 = ",vec2,"\n")

print("****************************** Q.02 ******************************","\n")
vec2 = np.cos(vec2)
print("vec2 = ",vec2,"\n")

print("****************************** Q.03 ******************************","\n")
vec3 = vec1 + 2*vec2
print("vec3 = ",vec3,"\n")

print("****************************** Q.05 ******************************","\n")
vec4 = mat1*vec3
print("vec4 = ",vec4,"\n")

print("****************************** Q.06 ******************************","\n")
mat1.transpose()
print("Transpose of mat1 = ",mat1.transpose(),"\n")

print("****************************** Q.07 ******************************","\n")
np.linalg.det(mat1)
print("Determinant of mat1 = ",np.linalg.det(mat1),"\n")

print("****************************** Q.08 ******************************","\n")
sum(mat1.diagonal())
print("Trace of mat1 = ",sum(mat1.diagonal()),"\n")

print("****************************** Q.09 ******************************","\n")
vec1.min()
print("The smallest element in vec1 = ",vec1.min(),"\n")

print("****************************** Q.10 ******************************","\n")
np.where(vec1 == vec1.min())
print("The answer is 'where' function and the result is",np.where(vec1 == vec1.min()),"\n")

print("****************************** Q.11 ******************************","\n")
mat1.min()
print("The answer is 'min' expression and the result is",mat1.min(),"\n")

print("****************************** Q.12 ******************************","\n")

A=np.array([[17, 24, 1, 8, 15],[23, 5, 7, 14, 16],[ 4, 6, 13, 20, 22],[10, 12, 19, 21, 3],[11, 18, 25, 2, 9]])

column_sum = np.sum(A,axis = 0)
print("A's column sum is equal to =",column_sum)
column_sum.max()
print("The biggest element in column sum = ",column_sum.max())
column_sum.min()
print("The smallest element in column sum = ",column_sum.min(),"\n")

row_sum = np.sum(A,axis = 1)
print("A's row sum is equal to =",row_sum)
row_sum.max()
print("The biggest element in row sum = ",row_sum.max())
row_sum.min()
print("The smallest element in row sum = ",row_sum.min(),"\n")

diagonal_sum_1 = sum(np.diag(A))
print("A's diagonal sum is equal to =",diagonal_sum_1,"\n")

A_p = np.fliplr(A)
diagonal_sum_2 = sum(np.diag(A_p))
print("A's other diagonal sum is equal to =",diagonal_sum_2,"\n")

print("نتیجه میگیریم:")

if column_sum.max() == column_sum.min() == row_sum.max() == row_sum.min() == diagonal_sum_1 == diagonal_sum_2:
    print ("A is a Magic Square! *o*","\n")
else:
    print ("A is not a Magic Square! T^T","\n")
    
print("****************************** Q.13 ******************************","\n")    

M = np.random.rand(10,10)
print("Random Matrix =",M,"\n")

print("****************************** Q.14 ******************************","\n")

M = np.linspace(1,100,100).astype(int)
print("M =",M,"\n")

MUL = M[0:25].reshape([5,5])
print("MUL =",MUL,"\n")

MUR = M[25:50].reshape([5,5])
print("MUR =",MUR,"\n")

MLL = M[50:75].reshape([5,5])
print("MLL =",MLL,"\n")

MLR = M[75:101].reshape([5,5])
print("MLR =",MLR)