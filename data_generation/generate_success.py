
import random
import json
from solve_24 import get_prob, solve


def construct_data(problem, steps):
    return {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": problem
            },
            {
                "role": "assistant",
                "content": steps
            }
        ]
    }


if __name__ == "__main__":
    NUM_DATASET = int(input("Input number of data to be generated..."))
    SAVE_DIR = input("Input name of dataset...")
    SAVE_DIR = f"../data/{SAVE_DIR}"

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
