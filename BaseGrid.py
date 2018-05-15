'''
Created on 8 Oct 2017

@author: Thomas
'''
import GUIFrame
import tkinter as tk

from _ast import Num
BASENUM = set(range(10))
POSSIBLENUM = set(range(1,10))

ResultsFromFrame = []

class SudokuError(Exception):
    # Base class for all custom exceptions in Sudoku solver
    pass

class NoValidNumber(SudokuError):
    #class used in checking correct setting of row, column or square values
    def __init__(self, Num):
        self.Num = Num
    def __str__(self):
        return "Error occurred because %s is no valid number" %self.Num

class DoubleNum(SudokuError):
    #class used in checking correct setting of row, column or square values
    def __init__(self,Num, Serie):
        self.Num = Num
        self.Serie = Serie
    def __str__(self):
        return "Error occurred because %s occurs double in %s" %(self.Num, self.Serie)

class Point:
    '''
    classdocs
    '''
    PossibleNum = set(range(0,10))
    
    def __init__(self):
        self.Value = 0
    
    def GetPointValue(self):
        return self.Value
        
    def SetPointValue(self, NewValue):
        self.Value = NewValue
        
    def GetPossibleNum(self):
        return self.PossibleNum

    def RemovePossibleNum(self, NumToRemove):
        self.PossibleNum = self.PossibleNum - set(NumToRemove)
                
        
class Matrix:
    
    Width = 9
    Height = 9
    
    def __init__(self):
        self.Grid = [[Point() for i in range(self.Width)] for j in range(self.Height)]
        
    def PrintMatrix(self):
        for row in self.Grid:
            print(row)
    
    def GetGridPoint(self, x, y):
        return self.Grid[y][x]
    
    #Get numbers in row, where row is based upon position of given point
    def GetRowNumBasePoint(self, PointPos):
        y = PointPos[1]
        for i in range(self.Width):
            ResultRow = [self.Grid[y][i].GetPointValue() for i in range(self.Width)]
        return ResultRow
    
    #Get numbers in column, where column is based upon position of given point   
    def GetColumnNumBasePoint(self, PointPos): 
        x = PointPos[0]
        for i in range(self.Height):
            ResultColumn = [self.Grid[i][x].GetPointValue() for i in range(self.Height)]
        return ResultColumn
    
    #Get numbers in square, where square is based upon position of given point  
    def GetSquareNumBasePoint(self, PointPos):
        xMod , yMod = int(PointPos[0]//3//(1/3)), int(PointPos[1]//3//(1/3))
        xModEnd, yModEnd = xMod+3, yMod+3
        ResultSquare = [self.Grid[i][j].GetPointValue() for i in range(yMod, yModEnd) for j in range(xMod, xModEnd)]
        
        '''
        for i in range(yMod, yModEnd):
            for j in range(xMod, xModEnd):
                ResultSquare = ResultSquare + "%s" %self.Grid[i][j].GetPointValue()
        '''
        
        return ResultSquare
            
#Checks if a series of numbers from either row, column or square, has no false numbers or duplicates
def CheckSerie(Serie):        
   
    CheckDupli = set()
    for i in Serie:
        #Checking if all number from Series are present in BASENUM
        if i in BASENUM:
            #Number from Serie is present in BASENUM
            pass
        else:
            raise NoValidNumber(i)
        
        #Checking if no duplicate numbers are present in Series, ignore duplicate zero's
        if i == 0:
            pass
        elif not (i in CheckDupli):
            # i is not in CheckDupli, and needs to be added
            CheckDupli.add(i)
        else:
            raise DoubleNum(i, Serie)
            
            
    
def GetPosBasePoint(Row, Column, Square):
    zero = set([0])
    RowPossibleNum = POSSIBLENUM - (set(Row)-zero)
    ColumnPossibleNum = POSSIBLENUM - (set(Column)-zero)
    SquarePossibleNum = POSSIBLENUM - (set(Square)-zero)
    
    TotalPossibleNum = set.intersection(RowPossibleNum, ColumnPossibleNum, SquarePossibleNum)
      
    print("Possible Numbers in row are: %s" %RowPossibleNum)
    print("Possible Numbers in column are: %s" %ColumnPossibleNum)
    print("Possible Numbers in square are: %s" %SquarePossibleNum)
    print("Total of possible numbers is: %s" %TotalPossibleNum)
    


   
TestRow = [0,0,0,1,2,3,0,0,0]   
TestColumn=[9,8,7,0,0,0,0,0,0]
TestSquare=[0,0,0,0,0,0,1,5,6]

root = tk.Tk()
GUIFrame.Example(root).pack(side="top", fill="both", expand=True)
root.mainloop()


#CheckSerie(TestRow)

#GetPosBasePoint(TestRow, TestColumn, TestSquare)
            
'''
TestPoint = Point()

print(TestPoint.GetPointValue())

TestPoint.SetPointValue(88)

print(TestPoint.GetPointValue())

print(TestPoint.GetPossibleNum())
TestPoint.RemovePossibleNum([9,7,5,3])
print(TestPoint.GetPossibleNum())

TestMatrix = Matrix()
#TestMatrix.PrintMatrix()
print("Point on certain position of grid: %s" %TestMatrix.GetGridPoint(0, 0))
CertainPoint = TestMatrix.GetGridPoint(0, 0)
print("Base Value %s" %CertainPoint.GetPointValue())
TestMatrix.GetGridPoint(1, 1).SetPointValue(1)
TestMatrix.GetGridPoint(4, 1).SetPointValue(2)
TestMatrix.GetGridPoint(3, 3).SetPointValue(3)
TestMatrix.GetGridPoint(3, 4).SetPointValue(4)
TestMatrix.GetGridPoint(3, 5).SetPointValue(5)
print("After Change: %s" %TestMatrix.GetGridPoint(2, 2).GetPointValue())
print("Possible Numbers Base %s" %CertainPoint.GetPossibleNum())
CertainPoint.RemovePossibleNum([1,2,3])
print(CertainPoint.GetPossibleNum())
print("resulting row values: %s" %TestMatrix.GetRowNumBasePoint([0,1]))
print("resulting column values: %s" %TestMatrix.GetColumnNumBasePoint([3,0]))

print("Square results: %s" %TestMatrix.GetSquareNumBasePoint([4,4]))




'''