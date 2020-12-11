# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 11: Seating System ---
# --- Part One ---
# Dodona submission


def occupied_seats(seat_layout_file):
    seats_occupied = 0
    seat_layout_array = read_seat_layout(seat_layout_file)
    seat_layout = make_seat_layout_matrix(seat_layout_array)
    (seat_layout, occupancy_changed, seats_occupied) = occupy_seats(seat_layout, seats_occupied)
    while occupancy_changed:
        (seat_layout, occupancy_changed, seats_occupied) = occupy_seats(seat_layout, seats_occupied)
    return seats_occupied


def occupy_seats(seat_layout_old, occupied_seats):
    occupancy_changed = False
    rows = len(seat_layout_old)
    columns = len(seat_layout_old[0])
    seat_layout_border = [["." for y in range(columns + 2)] for x in range(rows + 2)]
    seat_layout_new = [["." for y in range(columns)] for x in range(rows)]
    for row in range(1, rows + 1):
        for column in range(1, columns + 1):
            seat_layout_border[row][column] = seat_layout_old[row - 1][column- 1]
    for row in range(1, rows + 1):
        for column in range(1, columns + 1):
            if seat_layout_border[row][column] == '.':
                seat_layout_new[row - 1][column - 1] = '.'
            elif seat_layout_border[row][column] == "L":
                if occupy_empty_seat(seat_layout_border, row, column):
                    seat_layout_new[row - 1][column - 1] = "#"
                    occupied_seats += 1
                    occupancy_changed = True
                else:
                    seat_layout_new[row - 1][column - 1] = "L"
            elif seat_layout_border[row][column] == "#":
                if leave_occupied_seat(seat_layout_border, row, column):
                    seat_layout_new[row - 1][column - 1] = "L"
                    occupied_seats -= 1
                    occupancy_changed = True
                else:
                    seat_layout_new[row - 1][column - 1] = "#"
    return seat_layout_new, occupancy_changed, occupied_seats


def leave_occupied_seat(seat_layout_border, row, column):
    leave_seat = False
    occupied_seats = 0
    for check_row in range(row - 1, row + 2):
        for check_column in range(column - 1, column + 2):
            if not(check_row == row and check_column == column):
                if seat_layout_border[check_row][check_column] == "#":
                    occupied_seats += 1
    if occupied_seats >= 4:
        leave_seat = True
    return leave_seat

def occupy_empty_seat(seat_layout_border, row, column):
    occupy_seat = True
    for check_row in range(row - 1, row + 2):
        for check_column in range(column - 1, column + 2):
            if not(check_row == row and check_column == column):
                if seat_layout_border[check_row][check_column] == "#":
                    occupy_seat = False
    return occupy_seat


def make_seat_layout_matrix(seat_layout_array):
    rows = len(seat_layout_array)
    columns = len(seat_layout_array[0])
    seat_layout_matrix = [["." for y in range(columns)] for x in range(rows)]
    for row in range(0, rows):
        for column in range(0, columns):
            seat_layout_matrix[row][column] = seat_layout_array[row][column]
    return seat_layout_matrix


def read_seat_layout(seat_layout_file):
    seat_layout_output = open(seat_layout_file, "r")
    seat_layout_array = []
    for seat_row in seat_layout_output:
        seat_layout_array.append(seat_row.replace("\n", ""))
    return seat_layout_array