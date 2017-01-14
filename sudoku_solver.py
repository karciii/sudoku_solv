import numpy




def file_open(file):

    with open(file) as file:   #file reading
        lines = file.readlines()
        
    print (lines) 

   #numpy.fromstring('1 2'', dtype=string, sep=',')


#file_open("sudoku17.txt")

def solve():

    sudoku = "000000010400000000020000000000050407008000300001090000300400200050100000000806000"   #1st line for test
    print(sudoku)
    print(list (sudoku))  #parsing string 

    print (numpy.zeros((9, 9)))   #numpy arrady declaration
    

solve()