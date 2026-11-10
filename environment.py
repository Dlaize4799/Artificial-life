from config import ROWS, COLUMNS
import copy

class Environment:

    def __init__(self):

        # ROWS counts the number of rows present and hence how deep we can go (y-coordinate)
        # This may seem counter-intuitive ROWS associated with y? but remember it is number of rows:)
        self.food =  [   [0 for y in range(ROWS)] for x in range(COLUMNS)    ]  # Inner list represent a column
        
        for x in range(10, 20):
            for y in range(10, 20):
                self.food[x][y] = 3


        self.terrain = copy.deepcopy(self.food)
        #Terrain Initialiasation
        # 0 implies a barren land, doesnt produce food
        # 1 implies a moderate fertility producing around 0-2 food per cycle?
        # 2 implies a fertile land, 3-5 food per cycle?
        for x in range(COLUMNS):
            for y in range(ROWS):
                if x <= 20:
                    self.terrain[x][y] = 0

                elif x <= 40:
                    self.terrain[x][y] = 1

                else:
                    self.terrain[x][y] = 2