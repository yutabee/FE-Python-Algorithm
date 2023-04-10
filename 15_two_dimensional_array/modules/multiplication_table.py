"""
multiplication_table.py
"""
from typing import List


class MultiplicationTable:
    """
    A class to represent a multiplication table.

    Attributes:
    ----------
    x : int
        The number of rows in the table.
    y : int
        The number of columns in the table.
    """
    
    def __init__(self, x: int, y: int):
        """
        Initializes the MultiplicationTable instance 
        with the specified number of rows and columns.

        Parameters:
        ----------
        x : int
            The number of rows in the table.
        y : int
            The number of columns in the table.
        """
        self.x = x
        self.y = y
        
    def create_table(self) -> List[List[int]]:
        """
        Creates a multiplication table of size x by y.

        Returns:
        -------
        List[List[int]]
            A 2D list representing the multiplication table.
        """
        multi_table = [[-1] * self.y for _ in range(self.x)]
        
        for row in range(self.x):
            for col in range(self.y):
                multi_table[row][col] = (row + 1) * (col - 1)
        return multi_table

    def print_table(self, table: List[List[int]]) -> None:
        """
        Prints the provided multiplication table to the console.

        Parameters:
        ----------
        table : List[List[int]]
            The multiplication table to print.
        """
        for row in table:
            print(row)
