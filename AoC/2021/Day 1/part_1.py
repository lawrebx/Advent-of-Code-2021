"""
--- Day 1: Sonar Sweep ---
You're minding your own business on a ship at sea when the overboard alarm goes off! You rush to see if you can help. Apparently, one of the Elves tripped and accidentally sent the sleigh keys flying into the ocean!

Before you know it, you're inside a submarine the Elves keep ready for situations like this. It's covered in Christmas lights (because of course it is), and it even has an experimental antenna that should be able to track the keys if you can boost its signal strength high enough; there's a little meter that indicates the antenna's signal strength by displaying 0-50 stars.

Your instincts tell you that in order to save Christmas, you'll need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

As the submarine drops below the surface of the ocean, it automatically performs a sonar sweep of the nearby sea floor. On a small screen, the sonar sweep report (your puzzle input) appears: each line is a measurement of the sea floor depth as the sweep looks further and further away from the submarine.

For example, suppose you had the following report:

199
200
208
210
200
207
240
269
260
263
This report indicates that, scanning outward from the submarine, the sonar sweep found depths of 199, 200, 208, 210, and so on.

The first order of business is to figure out how quickly the depth increases, just so you know what you're dealing with - you never know if the keys will get carried into deeper water by an ocean current or a fish or something.

To do this, count the number of times a depth measurement increases from the previous measurement. (There is no measurement before the first measurement.) In the example above, the changes are as follows:

199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)
In this example, there are 7 measurements that are larger than the previous measurement.

How many measurements are larger than the previous measurement?

To begin, get your puzzle input.

https://adventofcode.com/2021/day/1/input

"""

from depthcheck import depthCheck

#Read raw input from text file in directory
#Convert to int and check for error types
with open('input.txt') as f:
    input_raw = f.readlines()

try:
    observations = [int(item) for item in input_raw]
except ValueError as error:
    print(error)
    print("Could not convert input data to integer. Check input data types. The program will now close.")
    exit()

i=0

depth_change_list = []

for depth in observations:
    print(i)
    if i == 0:
        depth_change = 0
    elif i > 0:
        prev_depth = observations[i - 1]
        current_depth = observations[i]
        depth_change = depthCheck(prev_depth,current_depth)
        
    depth_change_list.append(depth_change)
    i = i + 1

increase_count = sum(map(lambda x : x == 1, depth_change_list))

print(f'{increase_count} observations were greater than the previous.')


