# At first seemed like an easy challenge, however I soon
# realized it's gonna be a bit more tricky with the edge cases

def calculate_difference(input):
    from itertools import permutations
    all_nums = []
    for x in list(map(list,permutations(input, len(input)))):
        if x[0] != 0:
            all_nums.append(int("".join(map(str,x))))
        else:
            x.append(x.pop(0))
            all_nums.append(int("".join(map(str,x))))
    return max(all_nums) - min(all_nums)


print(calculate_difference([ 9,100,1,0,222 ]) == 922211000 - 100012229)