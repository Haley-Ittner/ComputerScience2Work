import unittest
'''
    This method assumes the solution is a list of tuples such as:
    [(0, 1), (1, 3), (2, 0), (3, 2)]
'''
'''
def print_board(solution):
    length = len(solution)
    print("for:", length)
    print('-' * length)

    if solution == []:
        print("no solution found")
    else:
        for i in range(length):
            for j in range(length):
                if (i, j) in solution:
                    print("Q", end="")
                else:
                    print(".", end="")
            print()

    print('-' * length)
    '''
'''
    Given the location of two queens, find if they are safe
    from each other.
'''
def safe((x1, y1), (x2, y2)):
    if x1 == x2: return False
    if y1 == y2: return False
    if abs(x2-x1) == abs(y2-y1): return False
    return True

def solve_queens(row, size, placed):
    print("At row:", row, "With queens at ", placed)
    '''
      if the row is greater than the size of the board, we're done
    '''
    if row == size:
        return placed

    # not a good place for the recursive call:
    # if columns > 7:
        # solve_queens(row, 0, placed)
    '''
    go through the columns in this row
        go through all the already placed queens and see if
            placing a new queen at (row, column) is safe
            '''
    for column in range(size):
        new_queen = (row, column)
        print("checking:", new_queen)
        good = True
        for queen in placed:
            print("checking against:",  queen)
            good &= safe(new_queen, queen)

        if good:
            placed.append(new_queen)
            print ("Good placement, so queens at:", placed)
            tmp = solve_queens(row + 1, size, placed)
            if not tmp:
                placed.pop()
            else:
                return placed

        # no need for an else as the first queen is safe against an empty
        # board
        # else:
            # placed.append(new_queen)
            # print("queen is at ", placed)
            # return solve_queens(row + 1, columns, placed)
        '''
        if it is
            place it at (row, column)
            if not solve_queens(row+1)
                remove row and column
                '''
    # don't need any of this
    # bad, worse = placed.pop(-1)
    # print("Bad row: ", bad, "Bad column: ", worse)
    # return solve_queens(bad, worse + 1, placed)

class test_queens_problem(unittest.TestCase):
    def test_safe(self):
        self.assertEquals(safe((1,1),(1,1)), False)
    def test_safeness(self):
        self.assertEquals(safe((1,1),(2,3)), True)
    def test_8_queens(self):
        self.assertEquals(solve_queens(0, 8, []), [(0,0),(1,4),(2,7),(3,5),(4,2),(5,6),(6,1),(7,3)])
    def test_1_queen(self):
        self.assertEquals(solve_queens(0,1,[]), [(0,0)])
    def test_2_queens(self):
        self.assertEquals(solve_queens(0,2,[]), None)
    def test_3_queens(self):
        self.assertEquals(solve_queens(0,3,[]), None)
    def test_4_queens(self):
        self.assertEquals(solve_queens(0,4,[]), [(0,1),(1,3),(2,0),(3,2)])
    def test_5_queens(self):
        self.assertEquals(solve_queens(0,5,[]), [(0,0),(1,2),(2,4),(3,1),(4,3)])
    def test_6_queens(self):
        self.assertEquals(solve_queens(0,6,[]), [(0,1),(1,3),(2,5),(3,0),(4,2),(5,4)])
    def test_10_queens(self):
        self.assertEquals(solve_queens(0,10,[]), [(0,0),(1, 2),(2, 5),(3, 7),(4, 9),(5, 4),(6, 8),(7, 1),(8, 3),(9, 6)])