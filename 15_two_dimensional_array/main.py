"""
main
"""
from modules.multiplication_table import MultiplicationTable

if __name__ == "__main__":
    mult_table = MultiplicationTable(9, 9)
    table = mult_table.create_table()
    mult_table.print_table(table)
