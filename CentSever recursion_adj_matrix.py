import numpy as np
import sys




table = np.array([['1', '0', '0',],
                  ['0', '0', '0',],
                  ['0', '0', '1',]])
counter=[0]
print('starting:')
print(table)

def fill(CentServer, i, j, symbol):
    
    if CentServer[i, j] != symbol:
        originalSymbol = CentServer[i, j]
        
        #return "Finished count %s" % counter
        
        def r(i, j):
            counter[0]+=1
            if i < 0 or i >= CentServer.shape[0] or j < 0 or j >= CentServer.shape[1]:
                # out of bounds
                return
            #change the symbol if r or c is adjacent 
            if CentServer[i,j] == originalSymbol:
                CentServer[i,j] = symbol
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    r(i+di, j+dj)
                    
           
                
        r(i, j)
        
      
    return CentServer
       

limit = sys.getrecursionlimit()

print('full update o servers:')
print(fill(table, 1, 1, '1'))
print("Recursion Limit:", limit," || number of days: ", counter[0])
