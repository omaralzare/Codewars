# https://www.codewars.com/kata/588417e576933b0ec9000045
def seats_in_theater(tot_cols, tot_rows, col, row):
    if tot_cols == tot_rows == col == row:
        return 0
    cols = tot_cols - (col - 1)
    rows = tot_rows - (row)
    return cols * rows
