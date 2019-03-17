class Solution:
    def Find(self,target,array):
        arrlen=len(array)
        col=len(array[0])-1
        if array>0 and col >=1:
            row=0
            while row < arrlen and col >=0:
                if array[row][col]<target:
                    row = row+1
                elif array[row][col]>target:
                    col =col-1
                else:
                    return True
            return False
        else:
            return False
