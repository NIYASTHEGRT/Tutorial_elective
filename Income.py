print("---------------------\nIncome Tax Calculator\n---------------------")
gross_sal=int(input("Enter the total earned income:"))
deduc=int(input("Enter the total deductions:"))
tax_income=gross_sal-deduc
print("\nTaxable Income: ",tax_income)
print("\nTaxable Income : ",tax_income)
if(tax_income<=300000):
    base=0
    rate=0
elif(300000<tax_income<=700000):
    exc_inc=tax_income-300000
    base=0
    rate=0.05
elif(700000<tax_income<=1000000):
    exc_inc=tax_income-700000
    base=20000
    rate=0.1
elif(1000000<tax_income<=1200000):
    exc_inc=tax_income-1000000
    base=50000
    rate=0.15
elif(1200000<tax_income<=1500000):
    exc_inc=tax_income-1200000
    base=80000
    rate=0.2
elif(1500000<tax_income):
    exc_inc=tax_income-1500000
    base=140000
    rate=0.3

income_tax=base+(exc_inc*rate)
