
import random


def random_solve(nums):
    steps = []

    while len(nums) > 1:
        # Randomly select two different indices
        i, j = random.sample(range(len(nums)), 2)
        a, b = nums[i], nums[j]

        # Randomly choose an operation
        op, symbol = random.choice([
            (lambda x, y: x + y, '+'),
            (lambda x, y: x - y if x >= y else None, '-'),
            (lambda x, y: x * y, '*'),
            (lambda x, y: x // y if y != 0 and x % y == 0 else None, '/')
        ])

        result = op(a, b)
        if result is None:
            continue  # Invalid operation, retry

        # Update the list of numbers
        nums = [nums[k] for k in range(len(nums)) if k != i and k != j] + [result]

        # Record the step
        steps.append(f"Select {a} and {b}, perform {a} {symbol} {b} = {result}. Remaining numbers: {nums}.")

        # Check if we reached the target
        if len(nums) == 1 and nums[0] == 24:
            return True, steps

    # If we exit the loop, no solution was found
    return False, steps


def solve(nums, steps, target=24):
    if len(nums) == 1:
        if nums[0] == target:
            return True, steps
        return False, steps

    # Try all pairs of numbers and operations
    last_steps = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue

            # Remaining numbers after picking nums[i] and nums[j]
            remaining = [nums[k] for k in range(len(nums)) if k != i and k != j]

            for op, symbol in [(lambda x, y: x + y, '+'),
                               (lambda x, y: x - y if x >= y else None, '-'),
                               (lambda x, y: x * y, '*'),
                               (lambda x, y: x // y if y != 0 and x % y == 0 else None, '/')]:
                result = op(nums[i], nums[j])
                if result is None:
                    continue

                new_nums = remaining + [result]
                current_step = (f"Select {nums[i]} and {nums[j]}, "
                            f"perform {nums[i]} {symbol} {nums[j]} = {result}. "
                            f"The remaining numbers are {new_nums}."
                            )
                new_steps = steps + [current_step]

                success, final_steps = solve(new_nums, new_steps, target)
                last_steps = final_steps
                if success:
                    return True, final_steps

    return False, last_steps

def get_prob(nums):
    return f"Solve {str(nums)} to get 24."


def get_random_sol(nums):
    success = True
    final_steps = []
    while success:
        success, final_steps = random_solve(nums)
        # if not success:
        #     final_steps.append("This does not work.")
    return '\n'.join(final_steps)


def get_sol(nums):
    success, final_steps = solve(nums, [])
    if success:
        final_steps.append("We found the solution!")
    else:
        final_steps.append("This does not work.")
    return '\n'.join(final_steps)

# Example usage
if __name__ == "__main__":
    nums = [100, 5, 2, 4]
    problem = get_prob(nums)
    random_sol = get_random_sol(nums)
    solution = get_sol(nums)
    print(problem)
    print(random_sol)
    print(solution)
