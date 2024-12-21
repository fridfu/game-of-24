
import json
import random
from game24 import propose_prompt, value_prompt
from generate_success import construct_data

with open("../data/24.json", "r") as file:
    problems = json.load(file)

easy = problems[:33]
medium = problems[600:633]
hard = problems[-34:]
train = problems[33:600] + problems[633:-34]
val = easy + medium + hard

prompt = """
Solve {input} to get 24.
First, list some possible next steps.
Then, for each outcome, evaluate if the 3 numbers can reach 24.
Finally, give a solution to to the original problem.
"""
validation_mixed = [construct_data(prompt.format(input=x), '') for x in val]
with open("../data/validation_mixed1.json", "w") as file:
    json.dump(validation_mixed, file)

# propose_train = [construct_data(propose_prompt.format(input=x), '') for x in train]
# with open("../data/propose_infer.json", "w") as file:
#     json.dump(propose_train, file)

# value_problem = []
# for i in range(20):
#     nums = [str(random.randint(1, 13)) for _ in range(3)]
#     if i < 10:
#         print(nums)
#     value_problem.append(' '.join(nums))
# for i in range(10):
#     nums = [str(random.randint(1, 13)) for _ in range(2)]
#     if i < 10:
#         print(nums)
#     value_problem.append(' '.join(nums))
# value_train = [construct_data(value_prompt.format(input=x), '') for x in value_problem]
# with open("../data/value_infer_test.json", "w") as file:
#     json.dump(value_train, file)

# with open("../data/easy.json", "w") as file:
#     json.dump(easy, file)
# with open("../data/medium.json", "w") as file:
#     json.dump(medium, file)
# with open("../data/hard.json", "w") as file:
#     json.dump(hard, file)
# with open("../data/train_emh.json", "w") as file:
#     json.dump(train, file)
# with open("../data/validation_emh.json", "w") as file:
#     json.dump(validation, file)

# :33 33:600 600:633 633:-34 -34: