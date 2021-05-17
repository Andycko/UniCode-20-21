# This is by far not a perfect solution quite time heavy probably O(nlogn) not sure though

def calculate_capacity(input):
    map = [[0 for y in input] for x in range(max(input))]
    res = 0
    start, finish = 0, 0
    for index, val in enumerate(input):
        while val != 0:
            map[val-1][index] = 1
            val -= 1
    for x in map:
        start = x.index(1) if 1 in x else False
        while type(start) == int:
            x.pop(start)
            finish = x.index(1) if 1 in x else False
            if finish:
                res += finish - start
                start = finish
            else:
               break
            
    return res    
    
print(calculate_capacity([ 1, 4, 2, 1, 1, 2, 5, 3, 4 ]))