employees = 5
employee_pps = []
employee_counter = 1
net_pay_list = []

total_employees_of_tax_a = 0
total_employees_of_tax_b = 0
total_employees_of_tax_c = 0
total_employees_of_tax_d = 0

total_tax_paid_b = 0
total_tax_paid_c = 0
total_tax_paid_d = 0

# thresholds
type_a_upper = 10000

type_b_lower = 10000
type_b_upper = 20000
type_b_tax = .30
type_b_allowance = 10000
type_b_employees = 0

type_c_lower = 20000
type_c_upper = 50000
type_c_tax = .35
type_c_allowance = 10000
type_c_employees = 0

type_d_lower = 50000
type_d_tax = .40
tax_allowance = 15000
type_d_employees = 0

tax_paid = 0
net_pay = 0

print ("-" * 50, "\n\t Welcome to Employee Tax Calculator")

for employee in range(employees):
    # receiving inputs
    pps = input("Employee PPS: ")
    employee_pps.append(pps)
    gross_pay = float(input("Enter employee {}'s gross pay: €".format(employee_counter)))
    employee_counter += 1
    print("-" * 50)
    print(pps + " has a gross pay of €" + str(gross_pay))
    # Calculating net pay and tax paid for each band type
    if gross_pay > type_b_lower and gross_pay <= type_b_upper:
        tax_paid = (gross_pay - type_b_allowance) * type_b_tax
        net_pay = gross_pay - tax_paid
        type_b_employees += 1
        total_tax_paid_b += tax_paid
        total_employees_of_tax_b += 1
    elif gross_pay > type_c_lower and gross_pay <= type_c_upper:
        tax_paid = (gross_pay - type_c_allowance) * type_c_tax
        net_pay = gross_pay - tax_paid
        type_c_employees += 1
        total_tax_paid_c += tax_paid
        total_employees_of_tax_c += 1
    elif gross_pay > type_d_lower:
        tax_paid = (gross_pay - tax_allowance) * type_d_tax
        net_pay = gross_pay - tax_paid
        type_d_employees += 1
        total_tax_paid_d += tax_paid
        total_employees_of_tax_d += 1
    else:
        tax_paid = 0
        net_pay = gross_pay
        total_employees_of_tax_a += 1
    net_pay_list.append(net_pay)
    print("Paid tax of €" + str(tax_paid) + " and has a net pay of €" + str(net_pay))
    print("-" * 50)

print("Employee\t\t\t Net Pay")
for x, y in zip(employee_pps, net_pay_list):
    print('%-20s %-20s' % (x, y))

print("-" * 50, "\n\n", "-" * 50)
print("Tax Type           Tax Paid")
print("B                  ", total_tax_paid_b)
print("C                  ", total_tax_paid_c)
print("D                  ", total_tax_paid_d)
print("Tax Type            Number")
print("A                  ", total_employees_of_tax_a)
print("B                  ", total_employees_of_tax_b)
print("C                  ", total_employees_of_tax_c)
print("D                  ", total_employees_of_tax_d)