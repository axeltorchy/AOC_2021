import utils

inputfile = utils.INPUT_DIR / "day6.txt"
#inputfile = utils.INPUT_DIR / "day6_example.txt"

with open(inputfile, 'r') as fh:
    line = fh.readline().strip().split(",")

# Initialize lanternfishs
delay = 7
additional_delay = 2

fish = [0 for i in range(delay + additional_delay)]
for x in line:
    fish[int(x)] += 1

N_days = 256

def number_of_fish(fish):
    return sum(fish)

print(number_of_fish(fish), fish)
for i in range(N_days):
    N_births = fish[0]
    for j in range(1, delay + additional_delay):
        fish[j - 1] = fish[j]
    fish[delay + additional_delay - 1] = N_births
    fish[delay - 1] += N_births
    print(number_of_fish(fish), fish)

print(f"Total number of fish after {N_days}: {number_of_fish(fish)}")
