from collections import defaultdict

# Advent of Code - Day 1
# https://adventofcode.com/2018/day/1

def insert(count, numMap):
    numMap[count] = numMap[count] + 1
    if numMap[count] == 2:
        return False
    else:
        return True

def part1(input):    
    return(sum(input))

def part2(input):
    numMap = defaultdict(int)
    looking = True
    found = False
    count = 0
    iteration = 0

    while looking:
        if iteration > 1000000:
            print("Not found after 1 million iterations")
        for num in input:
            count = count + num
            if not insert(count, numMap):
                return(count) 

input = [int(i) for i in open("/home/noe/projects/aoc-2018/day1/input.txt","r").readlines()]
print("## AoC - Day 1 puzzle ##")
print("Resulting Frequency: ", part1(input))
print("1st Duplicate Frequency:", part2(input))