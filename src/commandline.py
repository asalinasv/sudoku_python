class CommandLine:
    def __init__(self):
        pass

    """Definitions for command line reading and solving"""

    def reading_command_line():
        if raw_input('Please insert a string with 81 characters to play the sudoku game : \n'):
            return True

    def validate_size_command_line():
        a = raw_input('Please insert a string with 81 characters to play the sudoku game : \n')
        b = 0
        for x in a:
            b += 1
        print b
        return b

    def validate_values_command_line():
        a = raw_input('Please insert a string with 81 characters to play the sudoku game : \n')
        validos = '1','2','3','4','5','6','7','8','9','0'
        for x in a:
            if x not in validos:
                return False
        return True