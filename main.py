Monthly_gross_salary = float(input("Enter the monthly gross salary:\n"))


Vacation_pay = input("Is Vacation pay applicable, Y or N:\n").lower()
if Vacation_pay == "y":
    Vacation_pay = float(input("Enter the vacation pay:\n"))
else:
    Vacation_pay = 0


Thirteenth_month_pay = input("Is 13th month pay applicable, Y or N:\n").lower()
if Thirteenth_month_pay == "y":
    Thirteenth_month_pay = float(input("Enter the 13th_month_pay:\n"))
else:
    Thirteenth_month_pay = 0


Employee_Benefit_Budget = input("Is Employee benefit budget applicable, Y or N:\n").lower()
if Employee_Benefit_Budget == "y":
    Employee_Benefit_Budget = float(input("Enter employee benefit budget:\n"))
else:
    Employee_Benefit_Budget = 0


Thirty_percent_rule = input("Is 30% ruling applicable, Y or N:\n").lower()


#Pension_contribution:
Gross_salary = Monthly_gross_salary * 12 + Employee_Benefit_Budget
if (Gross_salary - 14017) * 0.05 > 4386:
    Pension_contribution = 4386
else:
    Pension_contribution = (Gross_salary - 14017) * 0.05
Total_income = Gross_salary - Pension_contribution


#Taxable_income:
if Thirty_percent_rule == "y" :
    Tax_free_allowance = 0.3 * Total_income
    Total_taxable_income = Total_income - Tax_free_allowance
else:
    Total_taxable_income = Total_income


#Tax & national insurance:
# Personal income tax
if Total_taxable_income >= 35129:
    Slab_1 = 35129
    Tax_1 = 0.0945 * Slab_1
else:
    Tax_1 = 0.0945 * Total_taxable_income
    Tax_2 = 0
    Tax_3 = 0

if 35129 < Total_taxable_income <= 68507:
    Slab_2 = Total_taxable_income - 35129
    Tax_2 = 0.371 * Slab_2
    Tax_3 = 0

if Total_taxable_income > 68507:
    Slab_3 = Total_taxable_income - 68507
    Tax_3 = 0.495 * Slab_3

Personal_income_tax = Tax_1 + Tax_2 + Tax_3

#National insurance
if Total_taxable_income > 35472:
    Social_security = 0.2765 * 35472
else:
    Social_security = 0.2765 * Total_taxable_income


#Credits:
#Employee tax credit
if Total_taxable_income <= 10108:
    Emp_tax_credit = 0.04581 * Total_taxable_income
elif 10108 < Total_taxable_income <= 21835:
    Emp_tax_credit = 463 + 0.28712 * (Total_taxable_income - 10108)
elif 21835 < Total_taxable_income <= 35652:
    Emp_tax_credit = 3837 + 0.02663 * (Total_taxable_income - 21835)
elif 35652 < Total_taxable_income <= 105375:
    Emp_tax_credit = 4205 - 0.06 * (Total_taxable_income - 35652)
else:
    Emp_tax_credit = 0


#General tax credit
if Total_taxable_income <= 21043:
    Gen_tax_credit = 2837
elif 21043 < Total_taxable_income <= 68507:
    Gen_tax_credit = 2837 - 0.05977 * (Total_taxable_income - 21043)
else:
    Gen_tax_credit = 0

Total_income_tax = Personal_income_tax + Social_security - Emp_tax_credit - Gen_tax_credit
Total_net_income = Total_income - Total_income_tax
print("Total net income per year =",Total_net_income)

Base_pay_per_month =  Total_net_income / 12
print("Base pay per month= ",Base_pay_per_month)

Payment_May = Base_pay_per_month + Vacation_pay * 0.505
print("Payment in May =",Payment_May)

Payment_December = Base_pay_per_month + Thirteenth_month_pay * 0.505
print("Payment in December =",Payment_December)