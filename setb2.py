nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
single_number = 0
for num in nums:
    single_number ^= num
print(f"The single number in the array is: {single_number}")

# output :
# Enter numbers separated by spaces: 1 2 2 3 3 
# The single number in the array is: 1