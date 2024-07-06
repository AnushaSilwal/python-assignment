dec =int(input("Enter the decimal number:"))
binary =""
while dec>0:
     binary=str(dec%2)+binary
     dec=dec//2

print("binary equvalence of your number is:",binary)

# Enter the decimal number:10
# binary equvalence of your number is: 1010