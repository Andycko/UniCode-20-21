
def validate(input, input2):
        if len(input) == len(input2):
            
            # create hashmap from input - letter:number of occurances
            # loop through second input and check if there are the same letters
            # if yes than decrement from map and remove from input2
            # if no check if there is letter + - 1 in the map
                # if there is, then remove from map and from input2

            from collections import Counter

            in_map = Counter(input)
            for char in input2:
                if in_map[char]:
                    in_map[char] -= 1
                    input2.replace(char,'')
                elif in_map[chr(ord(char) + 1)]:
                    in_map[chr(ord(char) + 1)] -= 1
                    input2.translate({ord(char) + 1: None})
                elif in_map[chr(ord(char) - 1)]:
                    in_map[chr(ord(char) - 1)] -= 1
                    input2.translate({ord(char) - 1: None})
                else:
                    return False

            return True
        else:
            return False
        

print(validate('CAT','SAD'))