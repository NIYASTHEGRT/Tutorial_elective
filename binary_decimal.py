binary_num = input("Enter a binary number: ")
decimal_val = 0

for i in range(len(binary_num)):
    bit = int(binary_num[i])

    decimal_val = decimal_val * 2 + bit


print("The decimal value is:", decimal_val)
