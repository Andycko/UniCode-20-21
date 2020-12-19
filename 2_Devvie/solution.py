# !!! OLD AND UNEFFECTIVE SOLUTION - SEE SOLUTION_2.PY !!!

# In this challange I went straight for python,
# as I have realized that it will be probably a lot
# easier and faster to complete challanges in.

# As for this challange I have thought about ways to solve it
# and the one I decided to go with, was to create a 2D array 
# which will record the 'map' of the directions where Devvie went
# and then compare the final x,y coordinates and direction with the
# initial x,y coordinates and get back accordingly 

def devvie(input):
        import numpy as np
        from copy import deepcopy

        class Direction:
            '''
            Class for a datatype 'Direction' which can be only
            'N', 'E', 'S', W'

            Has a method 'turn' which takes only +90 or -90 degrees
            as it is the only I needed at the moment
            '''
            _registry = []

            def __init__(self, pos, defVal = 'N', start = False, finish = False):
                self._registry.append(self)

                self.default = ['N','E','S','W']
                self.dir = self.default[self.default.index(str(defVal))]
                self.start = start
                self.finish = finish 
                self.pos = pos

            def turn(self,val):
                currentIndex = self.default.index(self.dir)
                if(val == 90):
                    self.dir = self.default[(currentIndex + 1) % 4]
                elif(val == -90):
                    self.dir = self.default[(currentIndex - 1) % 4]
                return self

            def __str__(self):
                return str(self.dir)

            def __repr__(self):
                return self.dir

        class LastInput:
            '''
            Class for a datatype LastInput, which I created to have
            a object with 'x' and 'y' properties, so I don't need to have
            separate variables
            '''
            def __init__(self,x,y):
                self.x = x
                self.y = y

            def __str__(self):
                return '[' + str(self.x) + ',' + str(self.y) +']'

        def addBorder(arr, symbol, lastInput, initInput, lastDir):
            '''
            This function was made so when Devvie moves on the map,
            the 2D numpy array indexes never run out of range.
            It adds a row of free spaces to whichever direction
            Devvie moves

            @attributes
            arr - 2D array
            symbol - symbol that represents free spaces
            lastInput - lastInput object 
            lastDir - Direction object which holds the last direction Devvie went
            '''
            if(str(lastDir) == 'N'):
                arr = np.insert(arr,0,symbol,axis=0)
                lastInput.x += 1
                initInput.x += 1
            if(str(lastDir) == 'S'):
                arr = np.insert(arr,len(arr)-1,symbol,axis=0)
            if(str(lastDir) == 'E'):
                arr = np.insert(arr,0,symbol,axis=1)
                lastInput.y += 1
                initInput.y += 1
            if(str(lastDir) == 'W'):
                arr = np.append(arr, [[symbol] for x in range(len(arr))], axis=1)

            return arr, lastInput, initInput

        # initialize variables
        initInput = LastInput(0,0)
        initDir = Direction(pos = initInput, start = True) 
        map = np.array([[initDir,'.'],['.','.']])
        lastInput = deepcopy(initInput)


        for x in input:
            # this for loop is for building the map with Devvies directions
            if (x == 'R'):
                # turning right and changing on map
                map[lastInput.x, lastInput.y] = map[lastInput.x, lastInput.y].turn(-90)
            elif (x == 'L'):
                # turning left and changing on map
                map[lastInput.x, lastInput.y] = map[lastInput.x, lastInput.y].turn(90)
            elif (x == 'F'):
                # going forward
                map, lastInput, initInput = addBorder(map,'.',lastInput, initInput, map[lastInput.x, lastInput.y])
                lastDir = map[lastInput.x, lastInput.y]

                # based on the Devvie's direction makes the move forward on the map
                if(str(lastDir) == 'N'):
                    lastInput.x -= 1
                    map[lastInput.x, lastInput.y] = Direction(defVal = lastDir, pos = deepcopy(lastInput))
                if(str(lastDir) == 'S'):
                    lastInput.x += 1
                    map[lastInput.x, lastInput.y] = Direction(defVal = lastDir, pos = deepcopy(lastInput))
                if(str(lastDir) == 'E'):
                    lastInput.y -= 1
                    map[lastInput.x, lastInput.y] = Direction(defVal = lastDir, pos = deepcopy(lastInput))
                if(str(lastDir) == 'W'):
                    lastInput.y += 1
                    map[lastInput.x, lastInput.y] = Direction(defVal = lastDir, pos = deepcopy(lastInput))
    
        # Label last input on the map as the finish location and save as a new obj
        map[lastInput.x, lastInput.y].finish = True
        finishObj = map[lastInput.x, lastInput.y]

        # Debug: print(map)

        for obj in Direction._registry:
            # find start object and save it
            if (obj.start):
                startObj = obj

        # this will be the returned value with the number of steps made
        countBack = 0

        while not (startObj.pos.x == finishObj.pos.x and startObj.pos.y == finishObj.pos.y):
            # loop for going back to the starting position
            if (startObj.pos.y < finishObj.pos.y and str(finishObj) != 'E'):
                if (str(finishObj) == 'N'):
                    finishObj.turn(90)
                else:
                    finishObj.turn(-90)
                countBack += 1
            elif (startObj.pos.y < finishObj.pos.y and str(finishObj) == 'E'):
                finishObj.pos.y -= 1
                countBack += 1

            elif (startObj.pos.y > finishObj.pos.y and str(finishObj) != 'W'):
                if (str(finishObj) == 'N'):
                    finishObj.turn(-90)
                else:
                    finishObj.turn(90)
                countBack += 1
            elif (startObj.pos.y > finishObj.pos.y and str(finishObj) == 'W'):
                finishObj.pos.y += 1
                countBack += 1

            if (startObj.pos.y == finishObj.pos.y and startObj.pos.x < finishObj.pos.x and str(finishObj) != 'N'):
                if (str(finishObj) == 'W'):
                    finishObj.turn(90)
                else:
                    finishObj.turn(-90)
                countBack += 1
            elif (startObj.pos.y == finishObj.pos.y and startObj.pos.x < finishObj.pos.x and str(finishObj) == 'N'):
                finishObj.pos.x -= 1
                countBack += 1

            elif (startObj.pos.y == finishObj.pos.y and startObj.pos.x > finishObj.pos.x and str(finishObj) != 'S'):
                if (str(finishObj) == 'W'):
                    finishObj.turn(-90)
                else:
                    finishObj.turn(90)
                countBack += 1
            elif (startObj.pos.y == finishObj.pos.y and startObj.pos.x > finishObj.pos.x and str(finishObj) == 'S'):
                finishObj.pos.x += 1
                countBack += 1        

        return countBack

if __name__ == '__main__':
    print(devvie("FFxFsdLLa"))
