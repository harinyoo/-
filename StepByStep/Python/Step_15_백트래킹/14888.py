import sys

N = int(input())
nums = list(map(int, sys.stdin.readline().split()))
ops = list(map(int, sys.stdin.readline().split()))
result_list = []


def calculator(result, idx, add, sub, mul, div):
    if idx == N:
        result_list.append(result)
        return

    if add != 0:
        calculator(result+nums[idx], idx+1, add-1, sub, mul, div)
    if sub != 0:
        calculator(result-nums[idx], idx+1, add, sub-1, mul, div)
    if mul != 0:
        calculator(result*nums[idx], idx+1, add, sub, mul-1, div)
    if div != 0:
        calculator(-(-result // nums[idx]) if result < 0 else result // nums[idx], idx+1, add, sub, mul, div-1)


calculator(nums[0], 1, ops[0], ops[1], ops[2], ops[3])
print(max(result_list))
print(min(result_list))
