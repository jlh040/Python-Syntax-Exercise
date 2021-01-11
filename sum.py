def sum_nums(nums):
    """Given list of numbers, return sum of those numbers.

    For example:
      sum_nums([1, 2, 3, 4])

    """  

    

    sum = 0
    for num in nums:
      sum += num
    
    return sum

#Test case
print("sum_nums returned", sum_nums([1, 2, 3, 4]))
