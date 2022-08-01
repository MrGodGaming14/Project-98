lwr_range_limit = int(input("Enter Lower Range Limit: "))
upr_range_limit = int(input("Enter Upper Range Limit: "))
DivisbleNumber = int(input("Enter the number to be divided: "))

for i in range(lwr_range_limit,upr_range_limit+1):
    if(i%DivisbleNumber==0):
        print(i)