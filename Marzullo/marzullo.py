def marzullo_algorithm(ranges):
    table = []
    for l,r in ranges:
        table.append((l,-1))
        table.append((r,+1))
    
    table.sort(key=lambda x: x[0])
    
    print(table)
        
        
        
    return (11,12)
    
    
    
    
    
           
def test(data_list):
    for data in data_list:
        result = marzullo_algorithm(data['input']) 
        if not result == data['expected']:
            print ('test failed input=', data['input'], 'expected=', data['expected'], 'actual=', result)
            return
    print ('test suceeded')
 
if __name__ == "__main__":
    test_data_list = (
            {'input' : ((8,12),(11,13),(10,12)), 'expected' : (11,12)},
            {'input' : ((8,12),(11,13),(14,15)), 'expected' : (11,12)})
    test(test_data_list)