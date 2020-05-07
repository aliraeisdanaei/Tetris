# Author Ali Raeisdanaei
import random
import queue


class Tetrominoe:

    # each four bits are a row in an array of the shaped
    # 0's are empty spaces, 1's are the shapes
    possible_Tetrominoes = [
        0b0000001101100000,
        0b0000011000110000,
        0b0000001001110000,
        0b0000011001100000,
        0b0100010001100000,
        0b0100010011000000,
        0b0100010001000100
    ]

    # always returns a returns a random tetromino
    def __init__(self):
        self.number = Tetrominoe.possible_Tetrominoes[random.randint(
            0, len(Tetrominoe.possible_Tetrominoes) - 1)]

    # this function turns the tetromino 90 degrees clockwise by the number of times specified
    # turns the array right by bitwise operation
    def turnRight(self, number):
        if (number == 0):
            return self.number

        self.number = self.getCol_asRow(0) | self.getCol_asRow(
            1) | self.getCol_asRow(2) | self.getCol_asRow(3)
        return self.turnRight(number - 1)

    # gets the values of a specific row (indexed from 0)
    def getRow(self, indexRow) -> int:
        mask = 0b1111
        # the 0th row is the first row to occur that is why we subtract by 3
        mask = mask << ((3 - indexRow) * 4)
        return self.number & mask

    # gets the values of a specific col (indexed from 0)
    def getCol(self, indexCol) -> int:
        if(indexCol == 0):
            mask0 = 0x1111
            return self.number & mask0
        if (indexCol == 1):
            mask1 = 0x2222
            return self.number & mask1
        if (indexCol == 2):
            mask2 = 0x4444
            return self.number & mask2
        if (indexCol == 3):
            mask3 = 0x8888
            return self.number & mask3

    # pushes all of the columns into a specific row
    def getCol_asRow(self, indexCol) -> int:
        pass

    def __repr__(self):
        return self.number


class Game:

    def __init__(self, level):
        # the walls and floor of the game surface is also included in the matrix
        self.matrix = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] for j in range(21)]
        # the floor
        self.matrix[20] = [1 for k in range(12)]

        self.level = level

        # init the next queue
        self.next_Tetr = queue.Queue()
        self.next_Tetr.put(Tetrominoe)
        self.next_Tetr.put(Tetrominoe)
        self.next_Tetr.put(Tetrominoe)

    def gameStart(self):
        pass

    def collision_Left(self) -> bool:
        pass

    def collison_right(self) -> bool:
        pass

    def collison_down(self) -> bool:
        pass

    # returns a Tetrominoe whenever one is dequed another is immediately enqued
    def tetr_deque(self) -> Tetrominoe:
        tmp = self.next_Tetr.get()
        self.next_Tetr.put(Tetrominoe)
        return tmp


new_game = Game(1)
