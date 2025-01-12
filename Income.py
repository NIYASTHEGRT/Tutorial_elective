def calculate_tax(income):
    if income <= 250000:
        return 0
    elif income <= 500000:
        return (income - 250000) * 0.05
    elif income <= 1000000:
        return (income - 500000) * 0.2 + 250000 * 0.05
    else:
        return (income - 1000000) * 0.3 + 500000 * 0.2 + 250000 * 0.05

