def calculate_tax(income):
    if income <= 250000:
        return 0
    elif income <= 500000:
        return (income - 250000) * 0.05
    elif income <= 1000000:
        return (income - 500000) * 0.2 + 250000 * 0.05
    else:
        return (income - 1000000) * 0.3 + 500000 * 0.2 + 250000 * 0.05

def main():
    print("Income Tax Calculator\n")
    try:
        income = float(input("Please enter your annual income in INR: "))
        tax_amount = calculate_tax(income)
        print(f"\nYour total tax liability is ₹{tax_amount:.2f}.")
    except ValueError:
        print("Error: Invalid input. Enter a numeric value for income.")

if __name__ == "__main__":
    main()
