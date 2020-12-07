# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 7: Handy Haversacks ---
# --- Part One ---

def hold_shiny_gold(bag_rules):
    nr_bags_can_contain_shiny_gold_bag = 0
    rules_list = open(bag_rules, "r")
    clean_bag_rules = []
    for bag_rule in rules_list:
        bag_rule = clean_bag_rule(bag_rule)
        clean_bag_rules.append(bag_rule)
    search_bags = ["shiny gold"]
    while search_bags:
        for element in range(len(clean_bag_rules)):
            bags = clean_bag_rules[element].split(":")
            if bags[1].find(search_bags[0]) != -1:
                search_bags.append(bags[0])
                nr_bags_can_contain_shiny_gold_bag += 1
                clean_bag_rules[element] = "Processed:Processed"
        search_bags.pop(0)
    return nr_bags_can_contain_shiny_gold_bag


def clean_bag_rule(bag_rule):
    bag_rule = bag_rule.replace(" bags contain ", ":")
    bag_rule = bag_rule.replace(" bags", "")
    bag_rule = bag_rule.replace(" bag", "")
    bag_rule = bag_rule.replace("no other", "")
    bag_rule = bag_rule.replace(".", "")
    return bag_rule


print(hold_shiny_gold("bag_rules"))
