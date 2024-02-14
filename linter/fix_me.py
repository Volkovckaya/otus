""" First homework """
nums = [10, 15, 20]


def calculate_average(nums):
    """ Calculate some numbers"""
    total = sum(nums)
    count = len(nums)
    average = total / count
    return average

result = calculate_average(nums)
print("The average is:", result)
