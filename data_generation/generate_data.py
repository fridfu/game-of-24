
import random
import json
from solve_24 import get_prob, solve

NUM_DATASET = 1000
SAVE_DIR = '../data/validation.json'

def construct_data(question, answer):
    return {
        "id": "identity_0",
        "conversations": [
            {
                "from": "user",
                "value": question
            },
            {
                "from": "assistant",
                "value": answer
            }
        ]
    }

count = 0
data = []
while count < NUM_DATASET:
    nums = [random.randint(1, 20) for _ in range(4)]
    problem = get_prob(nums)
    success, steps = solve(nums)
    if success:
        data.append(construct_data(problem, steps))
        count += 1

with open(SAVE_DIR, 'w') as json_file:
    json.dump(data, json_file)

print(f"Successfully generated {count} examples. Writen to file {SAVE_DIR}.")
