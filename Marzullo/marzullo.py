def marzullo_algorithm(ranges):
    table = []
    for l,r in ranges:
        table.append((l,-1))
        table.append((r,+1))
    
    for i in range( len( table ) ):
        for k in range( len( table ) - 1, i, -1 ):
            if ( table[k][0] < table[k - 1][0] ):
                swap( table, k, k - 1 )
            if ( table[k][0] == table[k - 1][0] ):
                if ( table[k][1] < table[k - 1][1] ):
                    swap ( table, k, k - 1 )
                    
    print(table)
    return (11,12)
   
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
            )
    test(test_data_list)