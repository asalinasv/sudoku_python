class SudokuScorer:

    def __init__(self,matrix):
        self.matrix = matrix

    def start(self):
        """Returns the scorer"""
        print "Your actual score is:"
        count = 0
        for i in self.matrix:
            for j in i:
                if(j==0):
                    count += 1
        return self.scorer(count)

    def scorer(self,count):
        """Construct the score"""
        if(count==0):
            res = 500
            print "500"
            print "Congratulations!!! You won"
            return res
        else:
            res = 500 - count*10
            print res
            return res