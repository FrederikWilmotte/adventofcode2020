# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 7: Handy Haversacks ---
# --- Part Two ---

def shiny_gold_size(bag_rules):
    nr_bags_can_contain_shiny_gold_bag = 0
    rules_list = open(bag_rules, "r")
    clean_bag_rules = []
    for bag_rule in rules_list:
        bag_rule = bag_rule.replace("\n", "")
        bag_rule = clean_bag_rule(bag_rule)
        clean_bag_rules.append(bag_rule)
    search_bags = ["1:shiny gold"]
    while search_bags:
        search_bag_split = search_bags[0].split(":")
        search_bag_count = int(search_bag_split[0])
        search_bag_name = search_bag_split[1]
        for element in range(len(clean_bag_rules)):
            bags = clean_bag_rules[element].split(":")
            if bags[0] == search_bag_name:
                if bags[1] != "":
                    bags_contains = bags[1].split(",")
                    for bags_contain in bags_contains:
                        contain_bag_split = bags_contain.split(" ")
                        contain_bag_count = int(contain_bag_split[0])
                        contain_bag_name = contain_bag_split[1] + " " + contain_bag_split[2]
                        product = search_bag_count * contain_bag_count
                        nr_bags_can_contain_shiny_gold_bag += product
                        search_bags.append(str(product) + ":" + contain_bag_name)
        search_bags.pop(0)
    return nr_bags_can_contain_shiny_gold_bag


def clean_bag_rule(bag_rule):
    bag_rule = bag_rule.replace(" bags contain ", ":")
    bag_rule = bag_rule.replace(" bags", "")
    bag_rule = bag_rule.replace(" bag", "")
    bag_rule = bag_rule.replace("no other", "")
    bag_rule = bag_rule.replace(".", "")
    bag_rule = bag_rule.replace(", ", ",")
    return bag_rule


print(shiny_gold_size("bag_rules"))
