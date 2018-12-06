from collections import defaultdict 

# Advent of Code - Day 2
# https://adventofcode.com/2018/day/2

def countTwice(sentence):
  lineMap = defaultdict(int)
  for char in sentence:
    lineMap[char] = lineMap[char] + 1
  for char in lineMap:
    if lineMap[char] == 2:
      return 1
  return 0

def countThree(sentence):
  lineMap = defaultdict(int)
  for char in sentence:
    lineMap[char] = lineMap[char] + 1
  for char in lineMap:
    if lineMap[char] == 3:
      return 1
  return 0

def part1():
  text = []
  twice = 0
  three = 0
  for input in open("input.txt"): text.append(input.strip("\n"))
  for line in text:
    sentence = []
    for char in line:
      sentence.append(char)
    twice = twice + countTwice(sentence)
    three = three + countThree(sentence)
  print("Checksum: ", twice * three)

def part2():
  text = []
  word = []
  looking = True
  for input in open("input.txt"): text.append(input.strip("\n"))
  for idx, line in enumerate(text):
    if looking:
      original = []
      for char in line: original.append(char)
      # print("ORIGINAL  :", original)
      for x in range(idx+1, len(text)):
        offset = 0
        comparison = []
        for char in text[x]: comparison.append(char)
        # print(" ")
        # print("COMPARISON:", comparison)

        for y, letter in enumerate(original):
          if letter != comparison[y]:
            offset = offset + 1
            # print(" OFFSET: ", offset)

        if offset == 1:
          for z, letter in enumerate(original):
            if letter == comparison[z]: word.append(letter)
          print("Common letters: ",''.join(word))
          looking = False
          break
  if looking: print("Common letters not found.")
  

print("### Advent of Code - Day 2 puzzle ###")
part1()
part2()