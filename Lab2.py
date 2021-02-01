"""
Anthony Quinn
X00138635
01/02/2021
1D Lists - Lab 2
"""

salesmen_name = []
total_salesmen_sales = []
kitchen_counter = 1
total_sales = 0
overall_sales = 0

threshold_commission = 50000
commission_value = .15
total_commission = 0



print("-" * 50, "\n\t\t\tKitchen Sales System\n\n", "-" * 50)
number_of_salesmen = int(input("Number of Salesmen: "))

# Receiving inputs for sales and salesmen names:
for salesmen in range(number_of_salesmen):
    name = input("Name: ")
    salesmen_name.append(name)
    kitchens_sold = int(input("Number of kithens sold: "))
    for kitchen in range(kitchens_sold):
        price_of_kitchen = float(input("Price of kitchen {}:€".format(kitchen_counter)))
        kitchen_counter += 1
        total_sales += price_of_kitchen
        total_salesmen_sales.append(total_sales)
    if total_sales > threshold_commission:
        commission = (total_sales - 50000) * commission_value
        total_commission += commission
        print("Commision payable for " + name + "\t\t: €" + str(round(commission, 2)))
        overall_sales += total_sales
        total_sales = 0
    else:
        print("No commission payable for " + name)
        total_sales = 0
    kitchen_counter = 1
    print("-" * 50)

print("-" * 50, "\n" + "-" * 50)


print("{0:15}{1:25}".format("Employees", "Total Sales"))
for x, y in zip(salesmen_name, total_salesmen_sales):
    print('%-14s %-14s' % (x, y))
print("-" * 50, "\n\nTotal commission paid:€" + str(total_commission))
most_sales_index = total_salesmen_sales.index(max(total_salesmen_sales))
least_sales_index = total_salesmen_sales.index(min(total_salesmen_sales))
print("Highest sales made €" + str(max(total_salesmen_sales)) + " by employee: " + salesmen_name[most_sales_index])
print("Lowest sales made €" + str(min(total_salesmen_sales)) + " by employee: " + salesmen_name[least_sales_index])
print("Sales values in ascending order")
new_list = sorted(total_salesmen_sales)
for i in range(len(new_list)):
    print(new_list[i])



