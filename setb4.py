def is_happy(n):
    seen = set()  
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n)) 
    return n == 1
num = int(input("Enter a number to check if it's happy: "))
if is_happy(num):
    print(f"{num} is a happy number.")
else:
    print(f"{num} is not a happy number.")
#output :
#Enter a number to check if it's happy: 23
#23 is a happy number.
# 2^2 + 3^2= 10
# 1^2 + 0^2= 1
#Those numbers for which this process ends in 1 are happy.