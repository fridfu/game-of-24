
def solve(nums, steps='', depth=1):
    if len(nums) == 1:
        if nums[0] == 24:
            return True, steps + "We found the solution!"
        return False, []

    num_str = [str(x) for x in nums]
    num_str = ', '.join(num_str)

    # Try all pairs of numbers and operations
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
                new_step = (f'Step {depth}: Select {nums[i]} and {nums[j]}, '
                            f'perform {nums[i]} {symbol} {nums[j]} = {result}. '
                            f'The remaining numbers are {remaining + [result]}.\n')
                next_steps = steps + new_step
                success, final_steps = solve(remaining + [result], next_steps, depth + 1)
                if success:
                    return True, final_steps

    return False, []


def get_prob(nums):
    return f"Solve {nums} to get 24."

def get_sol(nums):
    success, steps = solve(list(nums))
    if success:
        return steps
    return "No solution."


# Example usage
if __name__ == "__main__":
    nums = [1, 5, 2, 4]
    problem = f"Solve {nums} to get 24."
    solution = get_sol(nums)
    print(solution)

