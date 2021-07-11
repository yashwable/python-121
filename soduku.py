"""Rules for validation

Data structure dimension: NxN where N > 0 and √N == integer
Rows may only contain integers: 1..N (N included)
Columns may only contain integers: 1..N (N included)
'Little squares' (3x3 in example above) may also only contain integers: 1..N (N included)"""


class Sudoku(object):
    def __init__(self, data):
        self.data = data
        
    def is_valid(self):
        print (self.data)
        sqrt = int (len(self.data)**(0.5))

        if sqrt **2 != len (self.data):
            return False 
        for i in range (len(self.data)):
            if len(self.data) != len(self.data[i]):
                return False 
            listrow=[]
            listcol=[]
            for j in range (len(self.data)):
                if (type(self.data[i][j]) != int):
                        return False 
                listrow.append (self.data[i][j])
                listcol.append (self.data[j][i])

            if sorted( listrow) != list (set(listrow)):
                return False 
            if sorted(listcol) != list (set(listcol)):
                return False 
            if sum (listrow ) != sum (listcol):
                return False 
        else : 
            return True

# Valid Sudoku
goodSudoku1 = Sudoku([
  [7,8,4, 1,5,9, 3,2,6],
  [5,3,9, 6,7,2, 8,4,1],
  [6,1,2, 4,3,8, 7,5,9],

  [9,2,8, 7,1,5, 4,6,3],
  [3,5,7, 8,4,6, 1,9,2],
  [4,6,1, 9,2,3, 5,8,7],
  
  [8,7,6, 3,9,4, 2,1,5],
  [2,4,3, 5,6,1, 9,7,8],
  [1,9,5, 2,8,7, 6,3,4]
])

goodSudoku2 = Sudoku([
  [1,4, 2,3],
  [3,2, 4,1],

  [4,1, 3,2],
  [2,3, 1,4]
])

# Invalid Sudoku
badSudoku1 = Sudoku([
  [0,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9]
])

badSudoku2 = Sudoku([
  [1,2,3,4,5],
  [1,2,3,4],
  [1,2,3,4],  
  [1]
])


sod = goodSudoku1
print (sod.is_valid())