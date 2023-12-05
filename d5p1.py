seeds = []
#Contains a array of tuples which is each line, so steps[0] is every seed-to-soil line where the tuple is (destination range start, source range start, range length)
#if given value is inside source range start to range length, then return the difference between source range start and destination range start plus source range start - input value
""""
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48
seed 79 is in the range 50-98 thereby it returns 81 because 52 - 50 = 2, is input + 2
14 is not in range so return 14
55 is in range so return 57
13 is not in range so return 13
"""
steps = []
def main():
    with open ("input5.txt", "r") as input:
        s = input.readline()
        for x in s[6:].split(" "):
            if x != "":
                seeds.append(int(x))
        step_iteration = -1
        line_array = []
        for line in input:
            if ":" in line:
                step_iteration += 1
                if len(line_array) > 0:
                    steps.append(line_array)
                line_array = []
            elif len(line) != 1:
                temp = line.split(" ")
                data = (int(temp[0]), int(temp[1]), int(temp[2]))
                line_array.append(data)
        steps.append(line_array)

    step_iterations = 7
    for iteration in range(step_iterations):
        for seed_index in range(len(seeds)):
            return_value = find_correspondent(seeds[seed_index], steps[iteration])
            seeds[seed_index] = return_value
    print(min(seeds))

def find_correspondent(source, destinations):
    #first step, sources is seeds, destinations is all the seed-to-soil-number maps
    for destination in destinations:
        destination_range = destination[0]
        source_range = destination[1]
        length = destination[2]
        difference = destination_range - source_range
        if source >= source_range and source <= source_range + length:
            return source+difference
    return source
            

if __name__ == "__main__":
    main()
