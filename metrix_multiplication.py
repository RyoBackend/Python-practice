def metrix_multiplication(row,column,matrix1,matrix2):
    result = []
    for i in range(row):
        temp_row = []
        for j in range(column) :
            total = 0
            for k in range(column) :
                total += matrix1[i][k] * matrix2[k][j]
            temp_row.append(total)
        result.append(temp_row)
    return result

def matrix_creation(row,column) :
    
    matrix =[] 
    for i in range(row):
        temp = []
        for j in range(column) :
            elements = int(input(f'enter the values of {i+1} row and {j+1} column : '))
            temp.append(elements)
        matrix.append(temp)
    return matrix



while True :
    try :
        row= int(input('Enter the number of rows of  matrix :'))
        column= int(input('Enter thenumber of columns of  metrix :'))
        print("Enter the values for first metrix :")

        matrix_1 = matrix_creation(row,column)

        print('Matrix A : ')
        for r in matrix_1 :
            print(*r)
        
        print('Enter the values for second matrix :')

        matrix_2 = matrix_creation(row,column)

        print('Matrix B : ')

        for r in matrix_2 :
            print(*r)

        print("The result is : ")
        result = metrix_multiplication(row,column,matrix_1,matrix_2)
        for r in result :
            print(*r)
        break

    except ValueError :
        print('Error : Values must be an intiger')