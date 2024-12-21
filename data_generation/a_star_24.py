import heapq

def heuristic(nums):
    return abs(sum(nums) - 24)

def a_star_to_cot(nums):
    # 优先队列存储状态，格式：(f(n), g(n), state, steps)
    pq = []
    heapq.heappush(pq, (0, 0, nums, []))

    while pq:
        _, g, current_nums, steps = heapq.heappop(pq)

        # 如果已经到达目标
        if len(current_nums) == 1 and abs(current_nums[0] - 24) < 1e-6:
            # 将步骤转化为 CoT 格式
            cot = []
            for i, step in enumerate(steps, 1):
                cot.append(f"Step {i}: {step}")
            return cot

        # 扩展当前状态
        for i in range(len(current_nums)):
            for j in range(len(current_nums)):
                if i != j:
                    remaining = [current_nums[k] for k in range(len(current_nums)) if k != i and k != j]

                    for op, symbol in [(lambda x, y: x + y, '+'),
                                       (lambda x, y: x - y, '-'),
                                       (lambda x, y: y - x, '-'),
                                       (lambda x, y: x * y, '*'),
                                       (lambda x, y: x / y if y != 0 else None, '/'),
                                       (lambda x, y: y / x if x != 0 else None, '/')]:
                        result = op(current_nums[i], current_nums[j])
                        if result is not None:
                            new_nums = remaining + [result]
                            new_steps = steps + [f"从 {current_nums} 中选 {current_nums[i]} 和 {current_nums[j]}，用 {symbol} 操作，得到 {result}，当前状态为 {new_nums}"]
                            h = heuristic(new_nums)
                            heapq.heappush(pq, (g + 1 + h, g + 1, new_nums, new_steps))

    return ["No solution"]

# 测试
nums = [1, 5, 2, 4]
cot_output = a_star_to_cot(nums)
for step in cot_output:
    print(step)
