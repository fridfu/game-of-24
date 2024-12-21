import json

from solve_24 import get_prob, solve
from generate_success import construct_data
import random


def get_value_prompt(nums):
    nums_str = ' '.join(map(str, nums))
    return "Evaluate if given numbers can reach 24 (sure/likely/impossible): " + nums_str


train_value = []
for i in range(1000):
    nums = [random.randint(1, 13) for _ in range(3)]
    problem = get_value_prompt(nums)
    success, steps = solve(nums, [])
    answer = ''
    if success:
        answer = 'sure'
    else:
        success23, step = solve(nums, [], target=23)
        success25, step = solve(nums, [], target=25)
        if success23 or success25:
            answer = 'likely'
        else:
            answer = 'impossible'
            if sum(nums) > 30:
                answer = 'impossible. The numbers are too big.'
    train_value.append(construct_data(problem, answer))

for i in range(200):
    nums = [random.randint(1, 13) for _ in range(2)]
    problem = get_value_prompt(nums)
    success, steps = solve(nums, [])
    answer = ''
    if success:
        answer = 'sure'
    else:
        success23, step = solve(nums, [], target=23)
        success25, step = solve(nums, [], target=25)
        if success23 or success25:
            answer = 'likely'
        else:
            answer = 'impossible'
    train_value.append(construct_data(problem, answer))

with open("../data/train_value.json", "w") as file:
    json.dump(train_value, file)