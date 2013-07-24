

class SudokuScorer:


    def __init__(self,matrix):
        self.matrix = matrix

    def start(self):
        count = 0
        for i in self.matrix:
            for j in i:
                if(j==0):
                    count += 1
        print count
        return self.scorer(count)

    def scorer(self,count):
        if(count==0):
            res = 500
            print "500"
            print "Congratulations!!! You won"
            return res
        else:
            res = 500 - count*10
            print res
            return res

    def start1(self):
        print self.matrix
        #SudokuTimer(True).timer()
        self.start()

ash= \
        [0,0,3,0,2,0,6,0,0],\
        [0,9,0,3,0,5,0,0,1],\
        [0,0,1,8,0,6,4,0,0],\
        [0,0,8,1,0,2,9,0,0],\
        [7,0,0,0,0,0,0,0,8],\
        [0,0,6,7,0,8,2,0,0],\
        [0,0,2,6,0,9,5,0,0],\
        [8,0,0,2,0,3,0,0,9],\
        [0,0,5,0,1,0,3,0,0]

#sud = SudokuScorer(ash)
#sud.start1()