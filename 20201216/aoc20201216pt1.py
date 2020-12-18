# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 16: Ticket Translation ---
# --- Part One ---

def error_rate(tickets_file):
    sum_error_tickets = 0
    (ranges, ticket_numbers) = read_tickets_file(tickets_file)
    for ticket in ticket_numbers:
        ticket_correct = False
        for range_total in ranges:
            range_split = range_total.split("-")
            if int(range_split[0]) <= ticket <= int(range_split[1]):
                ticket_correct = True
                break
        if not ticket_correct:
            sum_error_tickets += ticket
    return sum_error_tickets


def read_tickets_file(tickets_file):
    ranges = []
    ticket_numbers = []
    range_line = True
    your_ticket_line = False
    nearby_tickets_line = False
    tickets_output = open(tickets_file, "r").read().split("\n")
    for ticket_line in tickets_output:
        process_line = True
        if ticket_line == "your ticket:":
            range_line = False
            your_ticket_line = True
            nearby_tickets_line = False
            process_line = False
        elif ticket_line == "nearby tickets:":
            range_line = False
            your_ticket_line = False
            nearby_tickets_line = True
            process_line = False
        elif ticket_line == "":
            process_line = False
        if process_line:
            if range_line:
                ranges.append(read_range(ticket_line)[0])
                ranges.append(read_range(ticket_line)[1])
            elif your_ticket_line:
                read_your_ticket(ticket_line)
            elif nearby_tickets_line:
                nearby_tickets = read_nearby_tickets(ticket_line)
                for ticket in nearby_tickets:
                    ticket_numbers.append(ticket)
    ticket_numbers = [int(_) for _ in ticket_numbers]
    return ranges, ticket_numbers


def read_range(ticket_line):
    ticket_line = ticket_line[ticket_line.find(": ")+2:]
    ranges = ticket_line.split(" or ")
    return ranges


def read_your_ticket(ticket_line):
    return


def read_nearby_tickets(ticket_line):
    ticket_numbers = ticket_line.split(",")
    return ticket_numbers


print(error_rate("tickets"))
