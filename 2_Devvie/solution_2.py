# After sending in my first solution I have realized
# that I didn't need to create the 'map' - 2D array
# at all, as it would have been enough to save (x,y,z)
# coordinates with 'z' being the direction and then
# I could do the same start vs finish checking

def devvie(input):

    
    # start position will be [0,0,0]
    # 0 - up
    # 1 - right
    # 2 - bottom
    # 3 - left

        def move(position):
            '''
            Takes the current position - (x,y,z) and based on z - direction
            makes a move with x or y
            '''
            if(position[2] == 0):
                position[1] += 1
            if(position[2] == 1):
                position[0] += 1
            if(position[2] == 2):
                position[1] -= 1
            if(position[2] == 3):
                position[0] -=1
            
            return position
    
    
        position = [0,0,0]
    
        for x in input:
            # set last position
            if (x == 'R'):
                # turning right and changing direction
                position[2] = (position[2] + 1) % 4
            elif (x == 'L'):
                # turning right and changing direction
                position[2] = (position[2] - 1) % 4
            elif (x == 'F'):
                # going forward then make a move
                position = move(position)
                
        # this will be the returned value with the number of steps made
        countBack = 0
    
        while(position[0] != 0 or position[1] != 0):
            # while position is not equal to initial position find way back
            if (position[0] > 0 and position[2] != 3):
                # if x is bigger than 0 and direction is not left
                if(position[2] == 0):
                    # if direction is up, turn to the left by 1
                    position[2] = 3
                else:
                    # else turn to the right by 1
                    position[2] = (position[2] + 1) % 4    
                countBack += 1
            elif (position[0] > 0 and position[2] == 3):
                # if x is bigger than 0 and direction is left, add x to counter and set x = 0
                countBack += position[0]
                position[0] = 0
    
            elif (position[0] < 0 and position[2] != 1):
                # if x is smaller than 0 and direction is not right
                if(position[2] == 0):
                    # if direction is up, turn to the right by 1
                    position[2] = 1
                else:
                    # else turn to the left by 1
                    position[2] = (position[2] - 1) % 4    
                countBack += 1
            elif (position[0] < 0 and position[2] == 1):
                # if x is smaller than 0 and direction is right, add absolute(x) to counter and set x = 0
                countBack += abs(position[0])
                position[0] = 0
            
            
            elif (position[1] > 0 and position[2] != 2):
                # if y is bigger than 0 and direction is not bottom
                if(position[2] == 1):
                    # if direction is right, turn to the right by 1
                    position[2] = 2
                else:
                    # else turn to the left by 1
                    position[2] = (position[2] - 1) % 4    
                countBack += 1
            elif (position[1] > 0 and position[2] == 2):
                # if y is bigger than 0 and direction is bottom, add y to counter and set y = 0
                countBack += position[1]
                position[1] = 0
    
            elif (position[1] < 0 and position[2] != 0):
                # if y is smaller than 0 and direction is not up
                if(position[2] == 3):
                    # if direction is left, turn to the right by 1
                    position[2] = 0
                else:
                    # else turn to the left by 1
                    position[2] = (position[2] - 1) % 4    
                countBack += 1
            elif (position[1] < 0 and position[2] == 1):
                # if y is smaller than 0 and direction is right, add absolute(y) to counter and set y = 0
                countBack += abs(position[1])
                position[1] = 0 
    
        return countBack
    
if __name__ == '__main__':
    print(devvie("FFxFsdLLa"))
