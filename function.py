
def get_matrix(n,m,value):
    matrix = []
    for i in range(n):
        rep = [value]*n
        matrix.append(rep)

        return matrix







result1 = get_matrix(2, 2, 10)
result2 = get_matrix(5, 3, 42)
result3 = get_matrix(2, 4, 13)
print(result1*2)
print(result2*3)
print(result3*4)
