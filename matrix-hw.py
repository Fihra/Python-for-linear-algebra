import numpy as np

#create 3 matrices: 2 x 2, 2x2, 3x2
# compute scalar-matrix multiplication
# add all pairs of matrices

m1 = np.array([[4, 5],
              [7, 3]])

m2 = np.array([[2, 8],
              [9, 12]])

m3 = np.array([[7, 14],
              [3, 5],
              [11, 10]])


output = np.zeros((2,2))
output2 = np.zeros((2,2))
output3 = np.zeros((3,2))

print("Create 3 Matrices")
print("Matrice 1")
print(m1)
print("Matrice 2")
print(m2)
print("Matrice 3")
print(m3)

for i in range(len(m1)):
    for j in range(len(m1[i])):
        output[i][j] = m1[i][j] * m2[i][j]

print("Compute scalar-matrix multiplication")
print(output)

print("Add all pairs of matrices")

print("m1 + m2")
for i in range(len(m1)):
    for j in range(len(m1[i])):
        output2[i][j] = m1[i][j] + m2[i][j]

print(output2)



print("m1 + m3")
# for i in range(len(m3)):
#     print(m3[i])
#     for j in range(len(m3[i] - 1)):
#         if(j >= len(m3)):
#             output3[i][j] = m3[i][j]
#         else:
#             output3[i][j] = m1[i][j] + m3[i][j]
for i,j in enumerate(m3):
    print(m1[i])
    print(m3[i])
    # print("j: " + str(j))

# print(output3)