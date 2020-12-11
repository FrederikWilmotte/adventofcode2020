# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 11: Seating System ---
# --- Part Two ---


def seats_occupied(seat_layout_file):
    occupied_seats = 0
    seat_layout_array = read_seat_layout(seat_layout_file)
    seat_layout = make_seat_layout_matrix(seat_layout_array)
    (seat_layout, occupancy_changed, occupied_seats) = occupy_seats(seat_layout, occupied_seats)
    while occupancy_changed:
        (seat_layout, occupancy_changed, occupied_seats) = occupy_seats(seat_layout, occupied_seats)
    return occupied_seats


def occupy_seats(seat_layout_old, occupied_seats):
    occupancy_changed = False
    rows = len(seat_layout_old)
    columns = len(seat_layout_old[0])
    seat_layout_border = [["." for _ in range(columns + 2)] for _ in range(rows + 2)]
    seat_layout_new = [["." for _ in range(columns)] for _ in range(rows)]
    for row in range(1, rows + 1):
        for column in range(1, columns + 1):
            seat_layout_border[row][column] = seat_layout_old[row - 1][column - 1]
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


def next_seat(seat_layout_border, row, column, direction):
    seat_found = False
    seat = "."
    check_row = row
    range_row_start = row
    range_row_end = len(seat_layout_border)
    range_row_step = 1
    step_row = 0
    check_column = column
    range_column_start = column
    range_column_end = len(seat_layout_border[0])
    range_column_step = 1
    step_column = 0
    if "N" in direction:
        check_row = row - 1
        range_row_end = 0
        range_row_step = -1
        step_row = -1
    if "S" in direction:
        check_row = row + 1
        range_row_start = row + 1
        step_row = 1
    if "W" in direction:
        check_column = column - 1
        range_column_end = 0
        range_column_step = -1
        step_column = -1
    if "E" in direction:
        check_column = column + 1
        range_column_start = column + 1
        step_column = 1
    while check_row in range(range_row_start, range_row_end, range_row_step) \
            and check_column in range(range_column_start, range_column_end, range_column_step) and not seat_found:
        if seat_layout_border[check_row][check_column] == "#" or seat_layout_border[check_row][check_column] == "L":
            seat_found = True
            seat = seat_layout_border[check_row][check_column]
        check_row += step_row
        check_column += step_column
    return seat, seat_found


def leave_occupied_seat(seat_layout_border, row, column):
    occupied_seats = 0
    leave_seat = False
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    while directions and not leave_seat:
        (seat, seat_found) = next_seat(seat_layout_border, row, column, directions[0])
        if seat_found and seat == "#":
            occupied_seats += 1
        if occupied_seats >= 5:
            leave_seat = True
        directions.pop(0)
    return leave_seat


def occupy_empty_seat(seat_layout_border, row, column):
    occupy_seat = True
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    while directions and occupy_seat:
        (seat, seat_found) = next_seat(seat_layout_border, row, column, directions[0])
        if seat_found and seat == "#":
            occupy_seat = False
        directions.pop(0)
    return occupy_seat


def make_seat_layout_matrix(seat_layout_array):
    rows = len(seat_layout_array)
    columns = len(seat_layout_array[0])
    seat_layout_matrix = [["." for _ in range(columns)] for _ in range(rows)]
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


print(seats_occupied("seat_layout"))
