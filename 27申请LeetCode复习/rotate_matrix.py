class Solution:
    #48变体，逆时针旋转matrix
    #1 2 3    3 6 9
    #4 5 6 -> 2 5 8
    #7 8 9    1 4 7
    def rotate_matrix(self, matrix):
        #先沿着左下到右上的对角线反转
        n = len(matrix)
        for i in range(n):
            for j in range(0, n-i):
                matrix[i][j], matrix[n-i-1][n-j-1] = matrix[n-i-1][n-j-1], matrix[i][j]

        #每行reverse
        for row in range(n):
            matrix[row].reverse()

        return matrix

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    s = Solution()
    result = s.rotate_matrix(matrix)
    for i in range(len(result)):
        print(matrix[i])

