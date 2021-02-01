employees = 5
employee_pps = []
employee_counter = 1


# thresholds
type_a_upper = 10000

type_b_lower = 10000
type_b_upper = 20000
type_b_tax = .30

type_c_lower = 20000
type_c_upper = 50000
type_c_tax = .35

type_d_lower = 50000
type_d_tax = .40
tax_allowance = 15000

tax_paid = 0
net_pay = 0

print ("-" * 50, "\n\t Welcome to Employee Tax Calculator")

for employee in range(employees):
    pps = input("Employee PPS: ")
    gross_pay = float(input("Enter employee {}'s gross pay: €".format(employee_counter)))
    print("-" * 50)
    print(pps + " has a gross pay of €" + str(gross_pay))
    if gross_pay > type_b_lower and gross_pay <= type_b_upper:
        tax_paid = gross_pay * type_b_tax
        net_pay = gross_pay - tax_paid

    print("Paid tax of €" + str(tax_paid) + " and has a net pay of €" + str(net_pay))