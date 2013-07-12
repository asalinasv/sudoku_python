import copy
class Backtracking:
    def __init__(self,matrix,dimension):
        self.matrix = matrix
        self.backup_matrix = copy.deepcopy(matrix)
        self.dimension = dimension
        self.block=Block()


    def solve_backtracking(self, matrix):
        '''Solve the sudoku using backtracking algorithmn'''
        c=0
        r=0
        self.matrix = matrix
        value =1
        while r < self.dimension:
            while c < self.dimension:
                if self.matrix[r][c] == 0:
                    while value <= self.dimension:
                        '''Verify if value existd on block and row or in column'''
                        if self.block.validate_block(self.matrix,value,r,c) and \
                            self.validate_row(self.matrix,value,r,c)  and \
                            self.validate_column(self.matrix,value,r,c):
                            self.matrix[r][c]=value
                            print "MATRIX[%i][%i] = %i" % (r,c,value)
                            value = 11 #the number 11 is assigned to end the loop
                        else:
                            print "Exists a FALSE"
                            value += 1
                        #value+=1
                        if value == 10:
                            #'''if value equals to 10 means that wa unable o solve de sudoku line, must back to test with other number '''
                            #aqui aumentar codigo ojojojo no existe solucion
                            #print "the value is 10000000000000000"
                            print "values ENVIADOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOS"

                            print "row and column",r,c

                            #self.matrix,value,self.row_b,self.col_b
                            value, r, c = self.back_previous_solution(self.matrix, r, c)
                            continue

                value=1
                c+=1
            c=0
            r+=1
            #print '\n'

        print "****************************************************"
        return self.matrix

    def back_previous_solution(self,matrix,row_b,column_b):
        self.matrix = matrix
        self.col_b = column_b
        self.row_b = row_b
        self.col_b = self.col_b - 1

        if self.row_b > 0 and self.col_b == -1:
           '''to verify if can be back a previous row, the column is updated to max dimension '''
           self.row_b -= 1
           self.col_b = self.dimension - 1
           #value = self.matrix[self.row_b][self.col_b]


        value = self.matrix[self.row_b][self.col_b]
        if self.backup_matrix[self.row_b][self.col_b] == 0: #ojo aumentar vuando queremos retornar una fila ojoj
           #value = self.matrix[self.row_b][self.col_b]
            self.matrix[self.row_b][self.col_b]=0

            if value >= 9 and self.col_b >= 0:
                '''According to value and position of column a position and value are returned'''
                print "the value is GREATER THAN 9"
                value,self.row_b,self.col_b = self.back_previous_solution(self.matrix, self.row_b, self.col_b)
                return(value,self.row_b,self.col_b)
            elif value < 9 and self.col_b >= 0:
                value += 1

                print "row, column:", self.row_b, self.col_b
                print "the ORIGINAL matrix:", self.backup_matrix[self.row_b][self.col_b]
                print "****************---------++++++++++++++++**********************///////////"
                print "the new matrix:", self.matrix[self.row_b][self.col_b]
                print "self back matrxi is equal to 0"
                print self.matrix
                return(value,self.row_b,self.col_b)
            else:
                 print"The sudoku cannot be solved totally"
                 return(11,self.dimension,self.dimension)


        elif self.backup_matrix[self.row_b][self.col_b] <> 0 and self.col_b >= 0:
            '''When the initial sudoku has a number different to 0 on square'''
            print "self bacck matrix is differente to 0"
            print "row, column:", self.row_b, self.col_b
            print "the original matrix:", self.backup_matrix[self.row_b][self.col_b]
            print "****************---------++++++++++++++++**********************///////////"
            print "the new matrix:", self.matrix[self.row_b][self.col_b]
            #self.col_b = self.col_b - 1# ojojo
            if self.row_b > 0 and self.col_b == 0:
               '''to verify if can be back a previous row, the column is updated to max dimension '''
               self.row_b -= 1
               self.col_b = self.dimension - 1
               value = self.matrix[self.row_b][self.col_b]

            value,self.row_b,self.col_b = self.back_previous_solution(self.matrix,self.row_b,self.col_b)
            return(value,self.row_b,self.col_b)

        else:
            print "The matrix cannot be solved"
            return(11,self.dimension,self.dimension)


    def validate_row(self,matrix,value,post_row,post_column):
        '''verify if the same number that value exists on row '''
        column=0
        while column<9:
            if matrix[post_row][column] == value and column != post_column:
                #print "the column is: %i"%column
                return False # The value exist in row
            column+=1
        return True

    def validate_column(self,matrix,value, post_row,post_column):
        '''verify if the same number that value exists on column'''
        row=0
        while row<9:
            if matrix[row][post_column] == value and row != post_row: # post_row give the row of a
                #print "the row is: %i"%row
                return False # The value exist in row
            row+=1
        return True

class Block(Backtracking):
    def __init__(self):
        pass

    def validate_block(self,matrix,value,post_row,post_column):
        post_init= self.get_initial_positions_for_block(post_row,post_column)
        post_row_end=post_init[0] + 2
        post_column_end=post_init[1] + 2
        row=post_init[0]
        column=post_init[1]
        while row<=post_row_end:
            while column<=post_column_end:
                if column == 8 or column == 7 or column == 6:
                    print "row,column (%i, %i)"% (row,column)
                    print "value = %i"%value
                    print "matrix :%i" % matrix[row][column]

                if value == matrix[row][column] and row!=post_row and column!=post_column:
                    # print value
                    # print "row,column (%i, %i)"% (row,column)
                    print "FALSE"
                    return False
                column+=1
            column=post_init[1]
            row+=1
        print "TRUE"
        return True

    def get_initial_positions_for_block(self,post_row,post_column):
        '''get the initial position in x and y for the block according the row and column entered'''
        self.x=self.define_position_of_block(post_row)
        self.y=self.define_position_of_block(post_column)
        # print "x is: %i"% x
        # print "y is: %i"% y
        position = (self.x, self.y)
        # print "the values:"
        # print position [1]
        return position

        # if x==1:
        #   return x + y -1

        # elif x==2:
        #   return x + y + 1
        # else:
        #   return x + y + 3


    def define_position_of_block(self,position):
        '''Return the position of block according to one cordinate'''
        if position < 3:
            return 0
        elif position > 2 and position < 6:
            return 3
        else:
            return 6


# default_matrx= \
#         [4,0,0,0,0,0,8,0,5], \
#         [0,3,0,0,0,0,0,0,0], \
#         [0,0,0,7,0,0,0,0,0], \
#         [0,2,0,0,0,0,0,6,0], \
#         [0,0,0,0,8,0,4,0,0], \
#         [0,0,0,0,1,0,0,0,0], \
#         [0,0,0,6,0,3,0,7,0], \
#         [5,0,0,2,0,0,0,0,0], \
#         [1,0,4,0,0,0,0,0,0]

# matrix = Backtracking(default_matrx,9)
# block = Block()
# result = block.validate_block(default_matrx,4,3,2)
# #result_comp = assertEqual(True, result)
# print "the reuslt is: ", result

# result = block.get_initial_positions_for_block(4,2)
# print "THE POSITION ARE 3,0",result

# result = block.define_position_of_block(2)
# print "THE cordinate is :",result
