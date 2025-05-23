class Solution:
    def spiralOrder(self, matrix):
        res = []
        left , right = 0 , len(matrix[0])
        top , bottom =  0 , len(matrix)


        while left < right and top < bottom:
            #ger tevcery element form left and right
            for i in range(left,right):
                res.append(matrix[top][i])
            top += 1

            for i in range(top ,bottom):
                res.append(matrix[i] [right -1])
            left -= 1

            if not (left < right and top < bottom):
                break;

            for i in range(right-1 , left-1 , -1):
                res.append(matrix[bottom -1][i])
            bottom -= 1

            for i in range(bottom -1 , top -1 , -1):
                res.append(matrix[i][left])

        return res

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
s = Solution()
print(s.spiralOrder(matrix))

