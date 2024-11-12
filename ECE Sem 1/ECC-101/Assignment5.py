# Question 1

eqn1 = "8W + 6X + 2Y + 3Z = 20"
eqn2 = "3W + 8X + 4Y + 3Z = 24"
eqn3 = "5W + 2X + 6Y + 8Z = 12"
eqn4 = "9W + 2X + 3Y + 4Z = 14"

def getCoeffs(eqn):
    variables = ["W", "X", "Y", "Z"]
    arr = eqn.split(" ")
    coeffs = []
    for var in variables:
        for term in arr:
            if var in term:
                coeffs.append(int(term[:-1]))
    coeffs.append(int(arr[len(arr)-1]))
    return coeffs

def toRowEchelon():
    matrix = list(map(lambda eqn: getCoeffs(eqn), [eqn1, eqn2, eqn3, eqn4]))
    for i in range(4):
        leadI = matrix[i][i]
        matrix[i] = list(map(lambda x: x/leadI, matrix[i]))
        for j in range(i+1, 4):
            leadJ = matrix[j][i]
            newMatrix = []
            for x in range(5):
                matrix[j][x] = matrix[j][x] - leadJ*matrix[i][x]
    return matrix

def getValues():
    matrix = toRowEchelon()
    z = matrix[3][4]/matrix[3][3]
    y = (matrix[2][4] - matrix[2][3]*z)
    x = (matrix[1][4] - matrix[1][3]*z - matrix[1][2]*y)
    w = (matrix[0][4] - matrix[0][3]*z - matrix[0][2]*y - matrix[0][1]*x)
    return {'w': w, 'x': x, 'y': y, 'z': z}

print(getValues())

# Question 2

eqn1 = "8W + 6X + 2Y + 3Z = 20"
eqn2 = "3W + 8X + 4Y + 3Z = 24"
eqn3 = "5W + 2X + 6Y + 8Z = 12"
eqn4 = "9W + 2X + 3Y + 4Z = 14"

def getCoeffs(eqn):
    variables = ["W", "X", "Y", "Z"]
    arr = eqn.split(" ")
    coeffs = []
    for var in variables:
        for term in arr:
            if var in term:
                coeffs.append(int(term[:-1]))
    coeffs.append(int(arr[len(arr)-1]))
    return coeffs

def luDecompose(matrix):
    n = len(matrix)
    L = [[0]*n for _ in range(n)]
    U = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(i, n):
            U[i][j] = matrix[i][j]
            for k in range(i):
                U[i][j] -= L[i][k] * U[k][j]
        for j in range(i, n):
            if i == j:
                L[i][i] = 1
            else:
                L[j][i] = matrix[j][i]
                for k in range(i):
                    L[j][i] -= L[j][k] * U[k][i]
                L[j][i] /= U[i][i]
    
    return L, U

def forwardSubstitution(L, b):
    n = len(L)
    y = [0] * n
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i][j] * y[j]
    return y

def backwardSubstitution(U, y):
    n = len(U)
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = y[i]
        for j in range(i+1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]
    return x

def getValues():
    matrix = list(map(lambda eqn: getCoeffs(eqn), [eqn1, eqn2, eqn3, eqn4]))
    A = [row[:-1] for row in matrix]
    b = [row[-1] for row in matrix]
    L, U = luDecompose(A)
    y = forwardSubstitution(L, b)
    solution = backwardSubstitution(U, y)
    return {'w': solution[0], 'x': solution[1], 'y': solution[2], 'z': solution[3]}

print(getValues())
