from sys import stdin
import copy


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = copy.deepcopy(matrix1)
        self.matrix2 = copy.deepcopy(matrix2)


class Matrix:
    def __init__(self, lis):
        self.lis = list(copy.deepcopy(lis))

    def __str__(self):
        strRet = ''
        for i in range(len(self.lis)):
            for j in range(len(self.lis[i])):
                if j == len(self.lis[i]) - 1 and i != len(self.lis) - 1:
                    strRet += str(self.lis[i][j]) + '\n'
                elif j == len(self.lis[i]) - 1 and i == len(self.lis) - 1:
                    strRet += str(self.lis[i][j])
                else:
                    strRet += str(self.lis[i][j]) + '\t'
        return strRet

    def size(self):
        return len(self.lis), len(self.lis[0])

    def __add__(self, other):
        newLis = []
        t = []
        if len(self.lis) == len(other.lis):
            if len(self.lis[0]) == len(other.lis[0]):
                for i in range(len(self.lis)):
                    for j in range(len(self.lis[i])):
                        t.append(self.lis[i][j] + other.lis[i][j])
                    newLis.append(t)
                    t = []
            else:
                raise MatrixError(matrix1=Matrix(self.lis),
                                  matrix2=Matrix(other.lis))
        else:
            raise MatrixError(matrix1=Matrix(self.lis),
                              matrix2=Matrix(other.lis))
        return Matrix(newLis)

    def __mul__(self, other):
        newLis = copy.deepcopy(self.lis)
        if isinstance(other, int) or isinstance(other, float):
            for i in range(len(self.lis)):
                for j in range(len(self.lis[i])):
                    newLis[i][j] = self.lis[i][j] * other
        return Matrix(newLis)

    __rmul__ = __mul__

    def transpose(self):
        tmatrix = list(zip(*self.lis))
        self.lis = tmatrix
        return Matrix(tmatrix)

    def transposed(self):
        tmatrix = list(zip(*self.lis))
        return Matrix(tmatrix)

exec(stdin.read())
