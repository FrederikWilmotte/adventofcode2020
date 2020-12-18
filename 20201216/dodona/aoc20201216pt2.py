# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 16: Ticket Translation ---
# --- Part Two ---
# Dodona submission

import re


class TicketRule:
    def __init__(self, name, value_ranges, check, fields, unique_field):
        self.name = name
        self.value_ranges = value_ranges
        self.check = check
        self.fields = fields
        self.unique_field = unique_field


class Ticket:
    def __init__(self, fields, valid):
        self.fields = fields
        self.valid = valid


def identification(tickets_file, expression):
    multiple = 1
    (ticket_rules, tickets) = read_tickets_file(tickets_file, expression)
    (tickets) = flag_invalid_tickets(ticket_rules, tickets)
    (ticket_rules) = check_ticket_rules_fields(tickets, ticket_rules)
    (ticket_rules) = check_unique_ticket_rule(ticket_rules)
    for ticket_rule in ticket_rules:
        if ticket_rule.check:
            multiple *= tickets[0].fields[ticket_rule.unique_value]
    return multiple


def check_unique_ticket_rule(ticket_rules):
    all_unique = False
    while not all_unique:
        unique_field = -1
        for ticket_rule in ticket_rules:
            if len(ticket_rule.fields) == 1:
                unique_field = ticket_rule.fields[0]
                ticket_rule.unique_value = unique_field
        if unique_field >= 0:
            for ticket_rule in ticket_rules:
                if unique_field in ticket_rule.fields:
                    ticket_rule.fields.remove(unique_field)
        else:
            all_unique = True
    return ticket_rules


def check_ticket_rules_fields(tickets, ticket_rules):
    for ticket_rule in ticket_rules:
        field = 0
        while field < len(tickets[0].fields):
            rule_apply_ticket = True
            for ticket in tickets:
                if ticket.valid:
                    rule_apply_field = False
                    for range_value in ticket_rule.value_ranges:
                        range_split = range_value.split("-")
                        if int(range_split[0]) <= ticket.fields[field] <= int(range_split[1]):
                            rule_apply_field = True
                            break
                    if not rule_apply_field:
                        rule_apply_ticket = False
            if rule_apply_ticket:
                ticket_rule.fields.append(field)
            field += 1
    return ticket_rules


def flag_invalid_tickets(ticket_rules, tickets):
    for ticket in tickets:
        for ticket_field in ticket.fields:
            ticket_field_correct = False
            for ticket_rule in ticket_rules:
                for range_value in ticket_rule.value_ranges:
                    range_split = range_value.split("-")
                    if int(range_split[0]) <= ticket_field <= int(range_split[1]):
                        ticket_field_correct = True
                        break
            if not ticket_field_correct:
                ticket.valid = False
    return tickets


def read_tickets_file(tickets_file, expression):
    ticket_rules = []
    tickets = []
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
                ticket_rules.append(read_ticket_rule(ticket_line, expression))
            elif your_ticket_line:
                tickets.append(read_your_ticket(ticket_line))
            elif nearby_tickets_line:
                tickets.append(read_your_ticket(ticket_line))
    return ticket_rules, tickets


def read_ticket_rule(ticket_line, expression):
    fields = []
    ticket_line_split = ticket_line.split(": ")
    ranges = ticket_line_split[1].split(" or ")
    if re.search(expression, ticket_line_split[0]) is None:
        check = False
    else:
        check = True
    ticket_rule = TicketRule(ticket_line_split[0], ranges, check, fields, -1)
    return ticket_rule


def read_your_ticket(ticket_line):
    ticket_numbers = ticket_line.split(",")
    ticket_numbers = [int(_) for _ in ticket_numbers]
    ticket = Ticket(ticket_numbers, True)
    return ticket


def read_nearby_tickets(ticket_line):
    ticket_numbers = ticket_line.split(",")
    ticket_numbers = [int(_) for _ in ticket_numbers]
    ticket = Ticket(ticket_numbers, True)
    return ticket
