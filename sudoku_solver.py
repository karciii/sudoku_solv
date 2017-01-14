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
    sudoku = list(map(int, sudoku)) #mapping to int in array 
    sudoku =  numpy.resize(sudoku, (9,9)) #changing 
  #  sudoku = numpy.array(range(81)).reshape((9, 9)) #reshaping string to 9x9 array shape
    print (sudoku) 
   

    

solve()