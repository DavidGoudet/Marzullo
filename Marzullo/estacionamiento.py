def marzullo(ranges):
    table = []
    beststart, bestend = 0, 0
    for l,r in ranges:
        if (6 <= l <= 18 and 6 <= r <= 18 and l <= r):
            table.append((l,-1))
            table.append((r,+1))
   
            
            for i in range( len( table ) ):
                for k in range( len( table ) - 1, i, -1 ):
                    if ( table[k][0] < table[k - 1][0] ):
                        swap( table, k, k - 1 )
                    if ( table[k][0] == table[k - 1][0] ):
                        if ( table[k][1] > table[k - 1][1] ):
                            swap ( table, k, k - 1 )
          
            best = 0
            cnt = 0
            for i in range(len(table)):
                cnt = cnt - table[i][1]
                if cnt <= 10:            
                    if cnt > best:
                        best = cnt
                        beststart = table[i][0]
                        bestend   = table[i+1][0]
                else:
                    return False
        else:
            return False    
    return True                
            
   
def swap( A, x, y ):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp