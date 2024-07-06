def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

input_nums = input("Enter numbers separated by spaces: ").split()
nums = list(map(int, input_nums))
if contains_duplicate(nums):
    print("True.")
else:
    print("False.")

# Enter numbers separated by spaces: 1 2 2 4 
# True.
# return true if any value appears at least twice in the array, otherwise  return false
