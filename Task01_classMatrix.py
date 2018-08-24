from sys import stdin
import copy


class Matrix:
    def __init__(self, lis):
        self.lis = copy.deepcopy(lis)

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

exec(stdin.read())
