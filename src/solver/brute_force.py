""" BruteForce Class , class and methods to resolve sudoku game with a change in resolution
	Author: Ana Salinas
 	Automation Class (Sudoku project) - 2013
"""
class BruteForce:
	algorithm_name = ''
	sudoku_matrix = []
	row = []
	column = []
	square = []
	elements = []
	def __init__(self,matrix):
		self.elements = ['1','2','3','4','5','6','7','8','9']
		self.sudoku_matrix = matrix

	def sum_sudoku_cells(self):
		pass
		#return sum_cells
		
	def multiply_sudoku_cells(self):
		pass
		#return multiply_cells

	def verify_contents_sudoku_matrix(self):
		"""
		This method verifies that the contain of sudoku game just contain numbers from 0 to 9, if letter is in any cell an error is returned
		"""
		num_elements = len(self.sudoku_matrix)
		count = 0

		for i in range(num_elements): 
			for j in range (num_elements):
				if self.sudoku_matrix[i][j] >= 0 and self.sudoku_matrix[i][j] <= 9:
					count += 1
		if count < 81:
			return "Error: matrix contents different value than numbers"
		else:
			return count

	def verify_sudoku_size(self):
		num_elements = len(self.sudoku_matrix)
		count = 0

		for i in range(num_elements): 
			for j in range (num_elements):
				count += 1
		if count < 81:
			return "Error: Sudoku does not have 81 cells"
		else:
			return count

	def verify_sudoku_filled(self):
		num_elements = len(self.sudoku_matrix)
		count = 0

		for i in range(num_elements): 
			for j in range (num_elements):
				if int(self.sudoku_matrix[i][j]) >= 1 and int(self.sudoku_matrix[i][j]) <= 9:
					count += 1
		if count == 81:
			return "Sudoku already filled"
		else:
			return count
		
	def validate_row(self, row):
		value = 1
		for i in range(len(row)):
			value *= row[i]
		if value == 362880:
			return True
		elif value > 362880 or value < 362880:
			return False
		
	def retrieve_columns(self, matrix,j_position):
		num_rows = len(matrix)

		column_num = []
		i = 0
		while i < num_rows:
			column_num.append(matrix[i][j_position])
			i += 1
		return column_num
	
	def retrieve_square(self, matrix, i_position, j_position):
		num_rows = len(matrix)
		square = []
		x = i_position
		y = j_position
		
		if x < 3:
			x_start = 0
			
		elif x < 6:
			x_start = 3
			
		elif x < 9:
			x_start = 6

		if y < 3:
			y_start = 0
			
		elif y < 6:
			y_start = 3
			
		elif y < 9:
			y_start = 6
		
		for i in range(x_start,x_start+3):
			for j in range(y_start,y_start+3):
				square.append(matrix[i][j])
			
		return square			
		

	def resolve_sudoku(self):
		num_elements = len(self.sudoku_matrix)
		count = 0
		for i in range(num_elements): 
			for j in range (num_elements):
				if int(self.sudoku_matrix[i][j]) == 0:
					value = self.fill_cell(self.sudoku_matrix[i], self.retrieve_columns(self.sudoku_matrix,j),self.retrieve_square(self.sudoku_matrix, i, j))
					if value is None:
						print "Error"
					
					else: 
						self.sudoku_matrix[i][j]=str(value)
					
		return self.sudoku_matrix

	def fill_cell(self, row, column, square):
		
		num_elements_row = len(row)
		num_elements_col = len (column)
		list_to_compare = ['1','2','3','4','5','6','7','8','9']
		
		used_values = set(row)|set(column)|set(square)
		available_values = set(list_to_compare) - used_values
		
		print available_values
		if (len(sorted(list(available_values)))) == 0:
			return None
		else:
			(sorted(list(available_values)))[0]
				
		
		
if __name__ == '__main__':
	ma2 = ['4','0','0','0','0','1','6','5','0'],\
         ['0','0','7','0','4','0','0','0','1'],\
         ['0','5','0','8','0','6','0','0','3'],\
         ['5','4','8','0','3','0','9','7','0'],\
         ['0','0','0','0','0','4','0','0','8'],\
         ['1','0','0','7','0','0','2','0','0'],\
         ['0','7','0','0','0','0','0','0','4'],\
         ['0','0','0','2','0','0','0','6','0'],\
         ['6','0','5','0','1','0','3','0','0']

	ma = ['0','0','0','0','0','0','0','0','0'],\
         ['0','0','0','0','0','0','0','0','0'],\
         ['0','0','0','0','0','0','0','0','0'],\
         ['0','0','0','0','0','0','0','0','0'],\
         ['0','0','0','0','0','0','0','0','0'],\
         ['0','0','0','0','0','0','0','0','0'],\
         ['0','0','0','0','0','0','0','0','0'],\
         ['0','0','0','0','0','0','0','0','0'],\
         ['0','0','0','0','0','0','0','0','0']
	var = BruteForce(ma)
	print var.resolve_sudoku()
	"""row = ['4','0','0','0','0','1','6','5','0']
	colum = ['0','5','0','8','0','6','0','0','3']
	square = ['0','5','0','8','0','6','0','0','3']
	print var.fill_cell(row,colum,square)
	
	var2 = ['4','0','3','0','0','1','6','5','0']
	print var2
	del var2[0]
	print var2"""
	
	