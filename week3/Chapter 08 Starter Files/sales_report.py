sales = [[1540.0, 2010.0, 2450.0, 1845.0], # Region 1
        [1130.0, 1168.0, 1847.0, 1491.0], # Region 2
        [1580.0, 2305.0, 2710.0, 1284.0], # Region 3
        [1105.0, 4102.0, 2391.0, 1576.0]] # Region 4 

print("Sales Report\n")

print("Region   Q1      Q2      Q3      Q4")

total = 0
sales_by_region = list()
sales_by_quarter = list()

for r in range(4):
        row = str(r+1)
        by_region = 0
        by_quarter = 0

        for q in range(4):
                row += "   "+str(sales[r][q])
                by_region += sales[r][q]
                by_quarter += sales[q][r]
                total += sales[r][q]
                
        
        sales_by_region.append(by_region)
        sales_by_quarter.append(by_quarter)
        print(row)

print("\nSales by region")
print("Region 1: "+str(sales_by_region[0]))
print("Region 2: "+str(sales_by_region[1]))
print("Region 3: "+str(sales_by_region[2]))
print("Region 4: "+str(sales_by_region[3]))

print("\nSales by quarter")
print("Quarter 1: "+str(sales_by_quarter[0]))
print("Quarter 2: "+str(sales_by_quarter[1]))
print("Quarter 3: "+str(sales_by_quarter[2]))
print("Quarter 4: "+str(sales_by_quarter[3]))

print("\nTotal annual sales, all regions: $"+str(total))