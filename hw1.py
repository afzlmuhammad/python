import random

rice_price = 45      
sugar_price = 40     
oil_price = 130      

rice_qty = 3         
sugar_qty = 2.5      
oil_qty = 1.8        

rice_total = rice_price * rice_qty       
sugar_total = sugar_price * sugar_qty    
oil_total = oil_price * oil_qty          

print("Rice total  : Rs", rice_total)
print("Sugar total : Rs", sugar_total)
print("Oil total   : Rs", oil_total)

total_bill = rice_total + sugar_total + oil_total
print("\nTotal bill:", total_bill)

total_bill_int = int(round(total_bill))   
total_bill_str = str(total_bill_int)      
print("Total bill as integer:", total_bill_int)
print("Total bill as string :", "Rs" + total_bill_str)

delivery_charge = random.randint(5, 10)
print("Delivery charge: Rs", delivery_charge)

final_bill = total_bill_int + delivery_charge
print("Final bill (with delivery): Rs", final_bill)