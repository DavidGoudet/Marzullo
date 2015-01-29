def marzullo_algorithm(ranges):
    table = []
    for l,r in ranges:
        table.append((l,-1))
        table.append((r,+1))
    print(table)
    for i in range( len( table ) ):
        for k in range( len( table ) - 1, i, -1 ):
            if ( table[k][0] < table[k - 1][0] ):
                swap( table, k, k - 1 )
            if ( table[k][0] == table[k - 1][0] ):
                if ( table[k][1] < table[k - 1][1] ):
                    swap ( table, k, k - 1 )
    print(table)         
    best = 0
    cnt = 0
    for i in range(len(table) - 1):
        cnt = cnt - table[i][1]
        if cnt > best:
            best = cnt
            beststart = table[i][0]
            bestend   = table[i+1][0]
    return (beststart, bestend)                
    
   
def swap( A, x, y ):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp    
    
           
def test(data_list):
    for data in data_list:
        result = marzullo_algorithm(data['input']) 
        if not result == data['expected']:
            print ('test failed input=', data['input'], 'expected=', data['expected'], 'actual=', result)
            return
    print ('test suceeded')
 
if __name__ == "__main__":
    test_data_list = (
        {'input' : ((8,12),(11,13),(10,12),(12,15),(13,14)), 'expected' : (11,12)},
        {'input' : ((8,12),(11,13),(14,15)), 'expected' : (11,12)},
        {'input' : ((8,9),(8,12),(10,12)), 'expected' : (8,9)},
        {'input' : ((8,12),(9,10),(11,13),(10,12)), 'expected' : (11,12)},
        {'input' : ((8,12),(9,10),(11,13),(14,15)), 'expected' : (9,10)},
        {'input' : ((11,15),(8,15),(9,11),(10,14),(11,14),(9,10),(9,13),(12,15),(8,11),(14,15)), 'expected' : (12,13)})
            
    test(test_data_list)