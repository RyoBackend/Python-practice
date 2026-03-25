def matrix_multiplication(row_matrix1,column_matrix1,matrix1,row_matrix2,column_matrix2,matrix2):
    result = []
    for i in range(row_matrix1) :
        temp_row = []
        for j in range(column_matrix2) :
            total = 0
            for k in range(column_matrix1 ) :
                total += matrix1[i][k] * matrix2[k][j]
            temp_row.append(total)
        result.append(temp_row)
    return result

def matrix_creation(row,column) :
    matrix = []
    for i in range(row) :
        temp=[]
        for j in range(column) :
            value = int(input(f'Enter the value for {i}{j} position : '))
            temp.append(value)
        matrix.append(temp)    
    return matrix
                 

if __name__ =="__main__" :

    row_matrix1 = int(input('Enter the no of rows for the matrix A : '))
    column_matrix1 = int(input('Enter the no of columns for the matrix A : '))
    print(f'You entered {row_matrix1} x {column_matrix1} matrix')

    row_matrix2 = int(input('Enter the no of rows for the matrix B : '))
    column_matrix2 = int(input('Enter the no of columns for the matrix B : '))
    print(f'You entered {row_matrix2} x {column_matrix2} matrix')

    if column_matrix1 != row_matrix2 :
        print('Error : The row of matrix A and column of Matrix B must be same ')

    else :
        matrix_a = matrix_creation(row_matrix1,column_matrix1)
        print('The matrix A is :')
        for r in matrix_a :
            print(r)
        
        matrix_b = matrix_creation(row_matrix2,column_matrix2)
        print('The matrix B is :')
        for r in matrix_b :
            print(r)

    result = matrix_multiplication(row_matrix1,column_matrix1,matrix_a,row_matrix2,column_matrix2,matrix_b)
    print('The result is : ')
    for r in result :
        print(r)
    
        



