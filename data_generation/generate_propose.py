import json

from solve_24 import get_prob
from generate_success import construct_data
import random

def generate_possible_steps(inputs):
    assert len(inputs) == 4, "Input must contain exactly four integers."

    # Store possible results and descriptions
    results = []

    # Iterate over all pairs of inputs and their operations
    for i in range(len(inputs)):
        for j in range(i + 1, len(inputs)):
            if i != j:
                remaining = [inputs[k] for k in range(len(inputs)) if k != i and k != j]

                # Addition
                results.append(
                    (f"{inputs[i]} + {inputs[j]} = {inputs[i] + inputs[j]}", remaining + [inputs[i] + inputs[j]]))

                # Subtraction
                if inputs[i] >= inputs[j]:
                    a, b = inputs[i], inputs[j]
                else:
                    a, b = inputs[j], inputs[i]
                results.append(
                    (f"{a} - {b} = {a - b}", remaining + [a - b]))

                # Multiplication
                results.append(
                    (f"{inputs[i]} * {inputs[j]} = {inputs[i] * inputs[j]}", remaining + [inputs[i] * inputs[j]]))

                # Division (only if denominator is non-zero)
                if inputs[j] != 0 and inputs[i] % inputs[j] == 0:
                    results.append((f"{inputs[i]} / {inputs[j]} = {inputs[i] // inputs[j]}",
                                    remaining + [inputs[i] // inputs[j]]))
                if inputs[i] != 0 and inputs[j] % inputs[i] == 0:
                    results.append((f"{inputs[j]} / {inputs[i]} = {inputs[j] // inputs[i]}",
                                    remaining + [inputs[j] // inputs[i]]))

    seen = set()
    trimmed_results = []
    for (a, b) in results:
        if a not in seen:
            seen.add(a)
            trimmed_results.append((a, b))

    f = lambda x: abs(sum(x[1]) - 24)
    results = sorted(trimmed_results, key=f)
    # Generate output
    problem = get_prob(inputs) + " List possible next steps."
    output = "Possible next steps:\n"
    for operation, new_list in results[:8]:
        output += f"{operation} (left: {' '.join(map(str, map(int, new_list)))})\n"

    return construct_data(problem, output)

train_propose = []
for _ in range(1200):
    nums = [random.randint(1, 13) for _ in range(4)]
    train_propose.append(generate_possible_steps(nums))
with open("../data/train_propose.json", "w") as file:
    json.dump(train_propose, file)
