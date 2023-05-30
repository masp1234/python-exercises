

def averager():
     sum = 0
     count = 0
     average = None
     
     while True:
        input = yield average
        sum += input
        count += 1
        
        average = sum/count


