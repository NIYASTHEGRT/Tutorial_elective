principal = float(input("Enter the principal amount: "))
time = int(input("Enter the time period (in years): "))
rate = float(input("Enter the rate of interest: "))


total_interest = (principal * time * rate) / 100
total_amount = principal + total_interest


print("Total Interest:", total_interest)
print("Total Amount:", total_amount)


for year in range(1, time + 1):
    yearly_interest = (principal * year * rate) / 100
    yearly_amount = principal + yearly_interest
    print("Year", year, ": Interest =", yearly_interest, ", Total Amount =", yearly_amount)
