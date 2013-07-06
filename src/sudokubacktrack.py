
class Backtracking:
	def __init__(self,matrix,dimension):
		self.matrix = matrix
		self.dimension = dimension
		self.block=Block()


	def solve_backtracking(self):#,matrix):
		'''Solve the sudoky using backtracking algorithmn'''
		c=0
		r=0
		value =1		
		while r< self.dimension:
			while c < self.dimension:
				if self.matrix[r][c]==0:
					while value<=self.dimension:
						'''Verify if values does not exist on block and row also in column'''
						if self.block.validate_block(self.matrix,value,r,c) and \
							self.validate_row(self.matrix,value,r,c)  and \
							self.validate_column(self.matrix,value,r,c):
							self.matrix[r][c]=value
							#print "MATRIX[%i][%i] = %i" % (r,c,value)
							value=11
						else:
							# print "Exists a FALSE"
							value+=1	
	
				value=1
				c+=1
			c=0
			r+=1
		return 	self.matrix

	def validate_row(self,matrix,value,post_row,post_column):
		'''verify if the same number that value exists on row '''
		column=0	
		while column<9:
			if matrix[post_row][column] == value and column != post_column:
				return False # The value exist in row
			column+=1	
		return True	

	def validate_column(self,matrix,value, post_row,post_column):
		'''verify if the same number that value exists on column'''
		row=0
		while row<9:
			if matrix[row][post_column] == value and row != post_row: # post_row give the row of a
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
				if value == matrix[row][column] and row!=post_row and column!=post_column:
					# print value
					# print "row,column (%i, %i)"% (row,column)
					# print "FALSE"
					return False
				column+=1
			column=post_init[1]
			row+=1
		return True

	def get_initial_positions_for_block(self,post_row,post_column):
		'''get the initial position in x and y for the block according the row and column entered'''
		self.x=self.define_position_of_block(post_row)
		self.y=self.define_position_of_block(post_column)
		position = (self.x, self.y)
		return position


	def define_position_of_block(self,position):
		'''Return the position of block according to one cordinate'''
		if position < 3:
			return 0
		elif position > 2 and position < 6:
			return 3
		else:
			return 6



