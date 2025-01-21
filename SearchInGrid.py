"""
https://leetcode.com/discuss/interview-question/390551/

Given a char grid (o represents an empty cell and x represents a target object) and an API getResponse which
would give you a response w.r.t. to your previous position. Write a program to find the object. You can move to any
position.

enum Response { HOTTER, // Moving closer to target COLDER, // Moving farther from target SAME, // Same distance
from the target as your previous guess EXACT; // Reached destination }

// Throws an error if 'row' or 'col' is out of bounds public Response getResponse(int row, int col) { // black box }
Example 1:

Input: [['o', 'o', 'o'], ['o', 'o', 'o'], ['x', 'o', 'o']]

Output: [2, 0] Example 2:

Input: [['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'],
['o', 'o', 'o', 'x', 'o'], ['o', 'o', 'o', 'o', 'o']]

Output: [4, 3]

Assumptions:

There is always one and only one object. If it's not the target object the 1st call would always give HOTTER as result,
otherwise EXACT.
TC: O(log(m) + log(n))
"""


class FindObjectInGrid:
    def __init__(self):
        print("Find object")

    def getResponse(self, grid, row, col):
        # Black box
        pass

    def findObject(self, grid):
        m = len(grid)
        n = len(grid[0])
        top = 0
        left = 0
        bottom = m - 1
        right = n - 1
        columnIndex = self.binarySearchCol(grid, left, right)
        rowIndex = self.binarySearchRow(grid, top, bottom)
        return [rowIndex, columnIndex]

    def binarySearchCol(self, grid, left, right):
        while left <= right:
            mid = left + (right - left) // 2
            i = 0
            j = mid
            if self.getResponse(grid, i, j) == 'Exact' or \
                    (self.getResponse(grid, i, j + 1) != 'Hotter' and self.getResponse(grid, i, j - 1) != 'Hotter'):
                return mid
            elif self.getResponse(grid, i, j) == 'Hotter':
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def binarySearchRow(self, grid, top, bottom):
        while top <= bottom:
            mid = top + (bottom - top) // 2
            i = mid
            j = 0
            if self.getResponse(grid, i, j) == 'Exact' or \
                    (self.getResponse(grid, i + 1, j) != 'Hotter' or self.getResponse(grid, i - 1, j) != 'Hotter'):
                return mid
            elif self.getResponse(grid, i, j) == 'Hotter':
                top = mid + 1
            else:
                bottom = mid - 1
        return -1
