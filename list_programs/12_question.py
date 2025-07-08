# best time to buy stock and sell - I

def max_profit_1(nums):
    max_arr = []
    max_so_far = float("-inf")
    for i in range(len(nums)-1, -1, -1):
        if nums[i] > max_so_far:
            max_so_far = nums[i]
        max_arr.append(max_so_far)
    max_arr.reverse()
    profit = 0
    for i in range(len(nums)):
        if max_arr[i] - nums[i] > profit:
            profit = max_arr[i] - nums[i]
    return profit
  
def max_profit_2(nums):
    max_profit = 0
    min_price = float("inf")
    for i in range(0, len(nums)):
        if min_price > nums[i]: min_price = nums[i]
        profit = nums[i] - min_price
        max_profit = max(profit, max_profit)
    return max_profit

nums = [7,6,4,3,1]
profit = max_profit_2(nums)
print(profit)