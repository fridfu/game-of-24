
from itertools import permutations

def game_of_24(nums):
    def solve(nums, steps):
        if len(nums) == 1:
            if abs(nums[0] - 24) < 1e-6:  # Close enough to 24 to account for floating-point precision
                return True, steps
            return False, []

        num_str = [str(x) for x in nums]
        num_str = ', '.join(num_str)

        # Try all pairs of numbers and operations
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    # Remaining numbers after picking nums[i] and nums[j]
                    remaining = [nums[k] for k in range(len(nums)) if k != i and k != j]

                    for op, symbol in [(lambda x, y: x + y, '+'),
                                       (lambda x, y: x - y, '-'),
                                       (lambda x, y: y - x, '-'),
                                       (lambda x, y: x * y, '*'),
                                       (lambda x, y: x / y if y != 0 else None, '/'),
                                       (lambda x, y: y / x if x != 0 else None, '/')]:
                        result = op(nums[i], nums[j])
                        if result is not None:
                            a = str(nums[i]) if nums[i] >= 0 else f"({nums[i]})"
                            b = str(nums[j]) if nums[j] >= 0 else f"({nums[j]})"
                            next_steps = steps + [num_str, f"{a} {symbol} {b} = {result}"]
                            success, final_steps = solve(remaining + [result], next_steps)
                            if success:
                                return True, final_steps

        return False, []

    # Try all permutations of the input numbers
    for perm in permutations(nums):
        success, steps = solve(list(perm), [])
        if success:
            return steps

    return ["No solution"]

# Example usage
if __name__ == "__main__":
    nums = [1, 5, 2, 4]
    solution = game_of_24(nums)
    print(' --> '.join(solution))
