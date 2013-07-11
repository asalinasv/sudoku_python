class NorvigAlgorithm:
    def __init__(self):
        self.digits   = '123456789'
        self.rows     = 'ABCDEFGHI'
        self.cols     = self.digits
        self.squares  = self.cross(self.rows, self.cols)
        self.unitlist = ([self.cross(self.rows, c) for c in self.cols] +
                    [self.cross(r, self.cols) for r in self.rows] +
                    [self.cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
        self.units = dict((s, [u for u in self.unitlist if s in u])
                     for s in self.squares)

        self.peers = dict((s, set(sum(self.units[s],[]))-set([s]))
                     for s in self.squares)

    def getsquares(self):
        return self.squares

    def getunitlist(self):
        return self.unitlist

    def count_squares(self):
        return len(self.squares)

    def count_sublines(self):
        return len(self.unitlist)

    def count_units(self):
        for s in self.squares:
            return len(self.units[s])

    def count_peers(self):
        for s in self.squares:
            return len(self.peers[s])

    def near_units(self,unit):
        return self.units[unit]

    def near_peers(self,peer):
        return self.peers[peer]

    def cross(self, A, B):
        "Cross product of elements in A and elements in B."
        return [a+b for a in A for b in B]

    def parse_grid(self,grid):
        """Convert grid to a dict of possible values, {square: digits}, or
        return False if a contradiction is detected."""
        ## To start, every square can be any digit; then assign values from the grid.
        values = dict((s, self.digits) for s in self.squares)
        if self.grid_values(grid)==False:
            print "Norvig algorithm is receiving an input different of 81 characters"
            return False
        else:
            for s,d in self.grid_values(grid).items():
                if d in self.digits and not self.assign(values, s, d):
                    return False ## (Fail if we can't assign d to square s.)
            return values
    
    def grid_values(self,grid):
        "Convert grid into a dict of {square: char} with '0' or '.' for empties."
        chars = [c for c in grid if c in self.digits or c in '0.']
        if len(chars) == 81:
            return dict(zip(self.squares, chars))
        else:
            print "Norvig algorithm is receiving an input different of 81 characters"
            return False

    def assign(self,values, s, d):
        """Eliminate all the other values (except d) from values[s] and propagate.
        Return values, except return False if a contradiction is detected."""
        other_values = values[s].replace(d, '')
        if all(self.eliminate(values, s, d2) for d2 in other_values):
            return values
        else:
            return False

    def eliminate(self,values, s, d):
        """Eliminate d from values[s]; propagate when values or places <= 2.
        Return values, except return False if a contradiction is detected."""
        if d not in values[s]:
            return values ## Already eliminated
        values[s] = values[s].replace(d,'')
        ## (1) If a square s is reduced to one value d2, then eliminate d2 from the peers.
        if len(values[s]) == 0:
            return False ## Contradiction: removed last value
        elif len(values[s]) == 1:
            d2 = values[s]
            if not all(self.eliminate(values, s2, d2) for s2 in self.peers[s]):
                return False
        ## (2) If a unit u is reduced to only one place for a value d, then put it there.
        for u in self.units[s]:
            dplaces = [s for s in u if d in values[s]]
            if len(dplaces) == 0:
                return False ## Contradiction: no place for this value
            elif len(dplaces) == 1:
                # d can only be in one place in unit; assign it there
                if not self.assign(values, dplaces[0], d):
                    return False
        return values

    def display(self,values):
        "Display these values as a 2-D grid."
        if values==False:
            print "Norvig algorithm is receiving an input different of 81 characters"
            return False
        else:
            width = 1+max(len(values[s]) for s in self.squares)
            line = '+'.join(['-'*(width*3)]*3)
            for r in self.rows:
                print ''.join(values[r+c].center(width)+('|' if c in '36' else '')
                              for c in self.cols)
                if r in 'CF': print line
            print
            return True

    ################ Search ################

    def solve(self,grid):
        return self.search(self.parse_grid(grid))

    def search(self,values):
        "Using depth-first search and propagation, try all possible values."
        if values is False:
            return False ## Failed earlier
        if all(len(values[s]) == 1 for s in self.squares):
            return values ## Solved!
        ## Chose the unfilled square s with the fewest possibilities
        n,s = min((len(values[s]), s) for s in self.squares if len(values[s]) > 1)
        return self.some(self.search(self.assign(values.copy(), s, d)) \
                        for d in values[s])

    ################ Utilities ################

    def some(self,seq):
        "Return some element of seq that is true."
        for e in seq:
            if e: return e
        return False


norvig = NorvigAlgorithm()
grid1 = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
grid2 = '44....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
grid3 = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5..1382'
grid3 = '003020600090305001001806400008102900700000008006708200002609500800203009005010300'
a1 = norvig.solve(grid3)
a2 = norvig.parse_grid(grid3)

#print norvig.cross('ABCDEFGHI','123456789')
#print norvig.solve(grid2)
norvig.display(a1)
norvig.display(a2)




