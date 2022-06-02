class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row=len(matrix[0])
        trans=[]
        for i in range(row):
            col=[]
            for j in matrix:
                col.append(j[i])
            trans.append(col)
        return trans
