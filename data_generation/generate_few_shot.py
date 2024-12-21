
import json
import random
from solve_24 import get_random_sol, get_sol, get_prob
from generate_success import construct_data


def get_few_shot_sol(nums):
    a = random.randint(0, 5)
    response = ''
    for _ in range(a):
        response += get_random_sol(nums)
        response += "This does not work. Let's try another way.\n"
    response += get_sol(nums)
    return response


if __name__ == "__main__":
    with open("../data/24.json", "r") as file:
        problems = json.load(file)

    easy = problems[:33]
    medium = problems[600:633]
    hard = problems[-34:]
    dataset = problems[33:600] + problems[633:-34]
    val_set = easy + medium + hard
    print(len(dataset))
    print(len(val_set))

    train = []
    for p in dataset:
        nums = [int(x) for x in p.split(' ')]
        assert len(nums) == 4
        prob = get_prob(nums)
        response = get_few_shot_sol(nums)
        train.append(construct_data(prob, response))
    with open("../data/train_few_shot.json", "w") as file:
        json.dump(train, file)

    test = []
    for p in val_set:
        nums = [int(x) for x in p.split(' ')]
        assert len(nums) == 4
        prob = get_prob(nums)
        test.append(construct_data(prob, ''))
    with open("../data/validation_few_shot.json", "w") as file:
        json.dump(test, file)